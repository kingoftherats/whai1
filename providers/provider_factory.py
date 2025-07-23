from providers.gemini_provider import GeminiProvider
from providers.generic_provider import GenericProvider
from providers.provider_config import ProviderConfig

class ProviderFactory:
    """
    This class is a factory for creating instances of generative AI providers based on the provided configuration.
    """
    
    @staticmethod
    def create_provider(config: ProviderConfig) -> GenericProvider:
        """
        Creates a new instance of a generative AI provider based on the provided configuration.
        """

        match config.getName():
            case "gemini":
                return GeminiProvider(config)
            case _:
                raise ValueError(f"Unknown provider: {config.getName()}")