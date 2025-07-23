from providers.provider_config import ProviderConfig

class GenericProvider:
    """
    This is an abstract class that defines the interface for all generative AI providers.
    """

    def __init__(self, config: ProviderConfig):
        """
        Initializes a new GenericProvider instance. This should only be called by subclasses.
        
        Args:
            config (ProviderConfig): The configuration for the generative AI provider.
        """

        self.config = config

    def submitPromptForText(self, prompt: str) -> str:
        """
        Submits a text prompt to the generative AI provider and returns a string response.

        Args:
            prompt (str): The text prompt to submit.

        Returns:
            str: The string response from the generative AI provider.
        """

        raise NotImplementedError("Subclasses should implement this!")
    
    def submitPromptForJson(self, prompt: str, outputJsonSchema: dict) -> dict:
        """
        Submits a text prompt to the generative AI provider and returns a JSON (dict) response.

        Args:
            prompt (str): The text prompt to submit.
            outputJsonSchema (dict): The JSON schema for the output.

        Returns:
            dict: The JSON (dict) response from the generative AI provider.
        """
        
        raise NotImplementedError("Subclasses should implement this!")
