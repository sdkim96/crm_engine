from langchain_community.tools.tavily_search.tool import TavilySearchResults
from pydantic import BaseModel, Field

class add(BaseModel):
    """Add two integers together."""

    a: int = Field(..., description="First integer")
    b: int = Field(..., description="Second integer")

    def run(self):
        return self.a + self.b


class multiply(BaseModel):
    """Multiply two integers together."""

    a: int = Field(..., description="First integer")
    b: int = Field(..., description="Second integer")

    def run(self):
        return self.a * self.b

tavily = TavilySearchResults(max_results=2)