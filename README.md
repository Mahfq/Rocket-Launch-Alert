Rocket Launch Notifier
Rocket Launch Notifier is a Python application that scrapes a website to retrieve upcoming rocket launch information. It notifies users via Discord webhook messages about today's scheduled rocket launches, including mission details and associated images.

Features
Web Scraping: Utilizes BeautifulSoup for parsing HTML and extracting mission names, dates, and background image URLs.
Date Checking: Determines if a launch is scheduled for today based on scraped date information.
Discord Integration: Sends formatted messages to a specified Discord webhook URL, including mission details and images.
