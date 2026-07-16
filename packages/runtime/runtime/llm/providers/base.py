from abc import ABC, abstractmethod

from runtime.llm.models import LLMResponse


class BaseProvider(ABC):
    """Base class for all LLM providers."""

    @abstractmethod
    def build(self):
        """Return the provider-specific chat model."""
        raise NotImplementedError

    @abstractmethod
    async def generate(
        self,
        prompt: str,
        system_prompt: str | None = None,
        temperature: float = 0.0,
        max_tokens: int | None = None,
    ) -> LLMResponse:
        """Generate a response."""
        raise NotImplementedError