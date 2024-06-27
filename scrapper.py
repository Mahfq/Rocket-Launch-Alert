from dotenv import load_dotenv
from bs4 import BeautifulSoup
from datetime import datetime
import requests
import os
import re

dotenv_path = ".env"
load_dotenv(dotenv_path)

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
URL = os.getenv("URL_WEBSITE")

def extract_image_url(style_tags):
    tab_image_url = []
    pattern = re.compile(r'background:\s*url\((.*?)\)\s*center top no-repeat')
    for style in style_tags:
        matches = pattern.findall(style.string)
        if matches:
            tab_image_url.append(matches)
    return tab_image_url

def scrape_url(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'lxml')

        mission_name_elements = soup.find_all("h5", class_="header-style")
        mission_date_elements = soup.find_all("div", class_="mdl-card__supporting-text")
        style_tags = soup.find_all('style')
        mission_image_elements = extract_image_url(style_tags)

        missions = []
        for name, date, image in zip(mission_name_elements, mission_date_elements, mission_image_elements):
            mission_name = name.text.strip()
            mission_date = date.text.strip().split('\n')[0]
            missions.append((mission_name, mission_date, image))
        return missions

    except requests.exceptions.RequestException as e:
        print("Échec de la requête HTTP :", e)

def is_today(date_str):
    try:
        if "NET" in date_str:
            return False
        launch_date = datetime.strptime(date_str, "%a %b %d, %Y %H:%M %Z")
        today = datetime.today()
        return launch_date.date() == today.date()
    except ValueError:
        return False

def send_discord_message(webhook_url, message, image_url):
    data = {"content": message,"embeds": [ {"image": {"url": image_url[0]}} ]}
    response = requests.post(webhook_url, json=data)
    if response.status_code == 204:
        print("Message envoyé avec succès.")
    else:
        print(f"Erreur lors de l'envoi du message : {response.status_code}, {response.text}")

upcoming_launches = scrape_url(URL)
if upcoming_launches:
    for mission, date, image_url in upcoming_launches:
        if is_today(date):
            message = f"🚀 Un lancement est prévu aujourd'hui ! 🚀\n\n**Mission :** {mission}\n📅 **Date :** {date}"
            send_discord_message(DISCORD_WEBHOOK_URL, message, image_url)