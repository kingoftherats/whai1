import requests
import json

from providers.generic_provider import GenericProvider

class GeminiProvider(GenericProvider):
    """
    This class implements the Google Gemini generative AI provider.
    """

    ENDPOINT: str = "https://generativelanguage.googleapis.com/v1beta/models/{}:generateContent"

    def __init__(self, config):
        """
        Initializes a new GeminiProvider instance.

        Args:
            config (ProviderConfig): The configuration for the Gemini generative AI provider.
        """
        
        super().__init__(config)

    def __getCommonRequestBody(self, prompt: str) -> dict:
        return {
            "contents": [
                {
                    "parts": [
                        {
                            "text": prompt
                        }
                    ]
                }
            ],
            "generationConfig": {
                "thinkingConfig": {
                    "thinkingBudget": -1
                }
            }
        }
    
    def __makeRequest(self, reqBody: dict) -> requests.Response:
        return requests.request(
            "POST",
            self.ENDPOINT.format(self.config.getModel()),
            headers = {
                "Content-Type": "application/json",
                "x-goog-api-key": self.config.getApiKey()
            },
            json = reqBody
        )
    
    def __getResponseText(self, response: requests.Response) -> str:
        return response.json().get("candidates")[0].get("content").get("parts")[0].get("text")
    
    def submitPromptForText(self, prompt: str) -> str:
        reqBody = self.__getCommonRequestBody(prompt)
        response = self.__makeRequest(reqBody)
        return self.__getResponseText(response)

    def submitPromptForJson(self, prompt: str, outputJsonSchema: dict) -> dict:
        reqBody = self.__getCommonRequestBody(prompt)
        reqBody["generationConfig"]["responseMimeType"] = "application/json"
        reqBody["generationConfig"]["responseSchema"] = outputJsonSchema

        response = self.__makeRequest(reqBody)

        return json.loads(self.__getResponseText(response))
