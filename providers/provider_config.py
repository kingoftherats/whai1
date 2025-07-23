class ProviderConfig:
    """
    This class is used for strongly typing the generative AI provider configuration
    """

    def __init__(self, name: str, model: str, api_key: str):
        """
        Initializes a new ProviderConfig instance.

        Args:
            name (str): The name of the provider.
            model (str): The target model that the provider offers.
            api_key (str): The API key for authenticating requests to the provider.
        """
        
        self.name = name
        self.model = model
        self.api_key = api_key

    def getName(self) -> str:
        """
        Returns the name of the provider.

        Returns:
            str: The name of the provider.
        """
        
        return self.name

    def getModel(self) -> str:
        """
        Returns the target model of the provider.

        Returns:
            str: The target model of the provider.
        """

        return self.model

    def getApiKey(self) -> str:
        """
        Returns the API key for authenticating requests to the provider.

        Returns:
            str: The API key for authenticating requests to the provider.
        """
        
        return self.api_key
