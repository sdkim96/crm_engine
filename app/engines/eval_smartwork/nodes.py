from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser

from app.engines.base import openai
from app.engines.eval_smartwork.models import EvalSmartWorkState, Bookmarks

def analyze_bookmarks(state: EvalSmartWorkState):

    raw = """
    당신은 북마크 분석가입니다.\
    다음 유저의 메세지를 보고 북마크 정보를 분석해주세요.

    format_instructions: {format_instructions}
    북마크 정보: {bookmarks}
    """
    parser = PydanticOutputParser(pydantic_object=Bookmarks)
    prompt = PromptTemplate.from_template(raw)
    chain = prompt | openai | parser

    response = chain.invoke({
        "bookmarks": state.input_bookmarks,
        "format_instructions": parser.get_format_instructions()
    })

    state.bookmarks = response
    
    print("parser analysis 끝")
    return state

    return state

def analyze_human(state: EvalSmartWorkState):

    raw = """
    당신은 훌륭한 사람성격 분석가입니다.\
    다음 직업과 MBTI 를 가진 사람을 분석해보세요.

    장점만 적지말고, 단점도 적어주세요.

    직업: {profession}
    MBTI: {mbti}

    """
    prompt = PromptTemplate.from_template(raw)
    chain = prompt | openai | StrOutputParser()

    response = chain.invoke({
        "profession": state.profession.value,
        "mbti": state.mbti.value
    })

    state.human_analysis = response
    
    print("human analysis 끝")
    return state


def calculate_smartwork_score(state: EvalSmartWorkState):
    raw = """
    당신은 훌륭한 스마트워크 분석가입니다.\
    이 사람의 스마트워크 점수를 계산하여 리포트를 제출하세요.

    <분석> 는 그 사람의 성격에 대한 전반적인 분석입니다.
    <북마크 정보> 는 그 사람의 북마크 정보입니다.

    스마트워크 점수의 평가에 있어서 중요한 요소는 다음과 같습니다.
    - <북마크 정보>의 개수와 정보에 따라 스마트워크 점수가 달라집니다.
    - <북마크 정보>가 얼마나 해당 <분석> 와 연관되는지.
    - 그 사람의 성격의 장점이 <북마크 정보>에 얼마나 잘 반영되었는지도 고려해야합니다.
    
    하지만 북마크 정보가 많다고 해서 무조건 스마트워크 점수가 높은 것은 아닙니다.
    직업이 디자이너인데, 개발자 관련 북마크 정보가 많다면 스마트워크 점수가 낮을 수 있습니다.

    <분석>: {human_analysis}
    <북마크>: {bookmarks}

    """
    prompt = PromptTemplate.from_template(raw)

    chain = prompt | openai | StrOutputParser()

    response = chain.invoke({
        "bookmarks": str(state.bookmarks),
        "human_analysis": state.human_analysis
    })

    state.response = response

    print("스마트워크점수 분석 끝")
    return state
    