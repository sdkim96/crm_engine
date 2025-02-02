import enum
from typing import Optional, List
from pydantic import BaseModel, HttpUrl

class Profession(enum.Enum):
    DEVELOPER = "developer"
    DESIGNER = "designer"
    MARKETER = "marketer"
    MANAGER = "manager"

class BookmarkType(enum.Enum):
    URL = "url"
    FOLDER = "folder"

class BookmarkBase(BaseModel):
    id: int
    name: str
    type: BookmarkType

class Bookmark(BookmarkBase):
    url: Optional[str] = None
    children: Optional[List["Bookmark"]] = None 
    

class MBTI(enum.Enum):
    INTJ = "INTJ"
    INTP = "INTP"
    ENTJ = "ENTJ"
    ENTP = "ENTP"
    INFJ = "INFJ"
    INFP = "INFP"
    ENFJ = "ENFJ"
    ENFP = "ENFP"
    ISTJ = "ISTJ"
    ISFJ = "ISFJ"
    ESTJ = "ESTJ"
    ESFJ = "ESFJ"
    ISTP = "ISTP"
    ISFP = "ISFP"
    ESTP = "ESTP"
    ESFP = "ESFP"

class EvalSmartWorkState(BaseModel):
    
    profession: Profession
    bookmarks: List[Bookmark]
    mbti: MBTI

    human_analysis: Optional[str] = None


    response: Optional[str] = None



#################################
class PlanTools(enum.Enum):
    LLM = "LLM"
    

class Plan(BaseModel):
    plan: str
    tool: PlanTools
    tool_input: str