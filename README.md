# Rocket Launch Notifier

Rocket Launch Notifier is a Python application that scrapes a website to retrieve upcoming rocket launch information. It notifies users via Discord webhook messages about today's scheduled rocket launches, including mission details and associated images.

## Features

- **Web Scraping**: Utilizes BeautifulSoup for parsing HTML and extracting mission names, dates, and background image URLs.
  
- **Date Checking**: Determines if a launch is scheduled for today based on scraped date information.
  
- **Discord Integration**: Sends formatted messages to a specified Discord webhook URL, including mission details and images.

- ---

## Setup

### Prerequisites

- Python 3.x installed on your system.
- Required Python packages: `dotenv`, `beautifulsoup4`, `requests`.

### Installation

Clone the repository:

```bash
git clone https://github.com/your/repository.git
cd RocketLaunchNotifier

### Install dependencies:

```bash
pip install -r requirements.txt

Create a .env file in the project directory and add your Discord webhook URL and the URL of the website you want to scrape:

```bash
DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/your_webhook_url
URL_WEBSITE=https://example.com/launches

### Usage
Run the script to check for upcoming rocket launches and send notifications to Discord:

```bash
python scrapper.py (windows) or python3 scrapper.py (linux)

