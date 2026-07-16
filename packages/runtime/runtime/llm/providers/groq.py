from langchain_groq import ChatGroq

from runtime.llm.providers.base import BaseProvider


class GroqProvider(BaseProvider):
    """Groq LLM provider."""

    def __init__(
        self,
        api_key: str,
        model: str,
    ) -> None:
        self.api_key = api_key
        self.model = model

    def build(self) -> ChatGroq:
        """Create the Groq chat model."""
        return ChatGroq(
            groq_api_key=self.api_key,
            model_name=self.model,
            temperature=0,
        )

    async def generate(
        self,
        prompt: str,
        system_prompt: str | None = None,
        temperature: float = 0.0,
        max_tokens: int | None = None,
    ):
        raise NotImplementedError("Implement in next task.")