from pydantic import BaseModel
from typing import Annotated

from langgraph.graph.message import add_messages

def get_right(left, right):
    return right

class State(BaseModel):

    messages: Annotated[list, add_messages]