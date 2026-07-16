from pydantic import BaseModel


class LLMResponse(BaseModel):
    """Standard response returned by all LLM providers."""

    content: str
    model: str
    provider: str
    prompt_tokens: int = 0
    completion_tokens: int = 0
    total_tokens: int = 0