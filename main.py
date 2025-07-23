#!/usr/bin/env python

import requests
import yaml

from providers.generic_provider import GenericProvider
from providers.provider_config import ProviderConfig
from providers.provider_factory import ProviderFactory

#Aim for positive stuff only, no politics, no hate, no violence, no NSFW
MAGIC_WORDS = [
    "life",
    "prosperity",
    "luck",
    "fertility",
    "wealth",
    "numerology",
    "health",
    "healing",
    "fortune",
    "strength",
    "wisdom",
    "courage",
    "love",
    "peace",
    "happiness",
    "joy",
    "compassion",
    "justice",
    "courage",
    "honor",
    "bravery",
    "friendship"
    "kindness",
    "peace",
    "harmony",
    "mystery",
    "magic",
    "adventure",
    "exploration",
    "discovery",
    "imagination",
    "creativity",
    "inspiration"
]

SITE_PROMPT_TEMPLATE: str = "Read the page at {} and analyze it for the following: a word count of the page summary, the most frequently occurring noun, one possible target audience."
LINK_PROMPT_TEMPLATE: str = "Link the number {} to mythology, legends or folklore associated with at least one of the following words: {}. Summarize the first result into a one word answer. If no link can be found, tell me the name of your favorite mythological animal."
CONSPIRACY_PROMPT_TEMPLATE: str = "Write me a short conspiracy theory about {} using {} for {}"

SITE_INFO_SCHEMA = {
    "type": "OBJECT",
    "properties": {
        "summaryWordCount": { "type": "NUMBER" },
        "mostFrequentNoun": { "type": "STRING" },
        "targetAudience": { "type": "STRING" }
    }
}

def run(provider: GenericProvider) -> None:
    url: str = input("Please enter a URL: ")

    #Validate URL
    try:
        requests.utils.requote_uri(url)
        urlValidationResponse = requests.request("GET", url)
        if urlValidationResponse.status_code != 200:
            print(f"Error: Unable to access URL (status code {urlValidationResponse.status_code})")
            return
    except Exception as e:
        print(f"Error: Unable to access URL")
        return

    #Base prompt to extract site info
    siteInfo: dict = provider.submitPromptForJson(SITE_PROMPT_TEMPLATE.format(url), SITE_INFO_SCHEMA)

    #Make sure we have enough info to continue
    if siteInfo.get("summaryWordCount") < 10 or siteInfo.get("mostFrequentNoun") is None or siteInfo.get("targetAudience") is None:
        print("Error: Unable to extract enough information from the site to generate a conspiracy theory.")
        return

    #Get the base mythology/legend to work from
    mythology: str = provider.submitPromptForText(LINK_PROMPT_TEMPLATE.format(siteInfo.get("summaryWordCount"), ", ".join(MAGIC_WORDS)))

    #Generate the conspiracy theory
    conspiracy: str = provider.submitPromptForText(CONSPIRACY_PROMPT_TEMPLATE.format(siteInfo.get("targetAudience"), mythology, siteInfo.get("mostFrequentNoun")))

    print(f"\nHere's a conspiracy theory for you:\n{conspiracy}\n")

    rerun: str = input("Would you like to enter another URL? (y/n): ").strip().lower()
    if rerun != 'y':
        goodbye()

def goodbye() -> None:
    print("Goodbye, I hope you had fun!")
    exit(0)

#
#Program entry point
#

#Load provider config
with open("config.yaml", "r") as file:
    rawConfig = yaml.safe_load(file)

config = ProviderConfig(rawConfig.get("name", ""), rawConfig.get("model", ""), rawConfig.get("api_key", ""))

try:
    provider = ProviderFactory.create_provider(config)
except ValueError as e:
    print(f"Error: {e}")
    exit(1)

print("Let the show begin!")

#Loop forever until the user quits
while True:
    try:
        run(provider)
    except KeyboardInterrupt:
        print()
        goodbye()
