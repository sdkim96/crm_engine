
""" PYTHONPATH=. python -m test.test """
from langserve import RemoteRunnable

from app.engines.eval_smartwork.models import *

smartwork = RemoteRunnable("http://localhost:8000/smartwork/")

BASE_URL="http://localhost:8000/smartwork/stream"

bookmarks = """
Bookmarks

북마크바

BP1
마이페이지
Twitch Insights - Follow List
[OOP] 객체지향 5원칙(SOLID) - 개방-폐쇄 원칙 (Open-Closed Principle) - 𝝅번째 알파카의 개발 낙서장
Nas - Synology DiskStation
rickiepark/aiml4coders: <개발자를 위한 머신러닝&딥러닝> 도서의 코드 저장소
aiml4coders/03-beyond-the-basics.ipynb at main · rickiepark/aiml4coders
Best Acoustic Japanese Song 🎸 Relaxing Japanese Acoustic Music - YouTube
롤 전적 검색 OP.GG - 전적 검색, 관전, 리플레이, 챔피언 공략, 카운터, 랭킹
"""

mock = EvalSmartWorkState(
    profession=Profession.DESIGNER,
    input_bookmarks=bookmarks,
    mbti=MBTI.ISTP,
)

json_mock = mock.model_dump(mode="json")
payload={
    "input": json_mock
}
import requests

with requests.post(BASE_URL, json=payload ,stream=True) as response:
    for line in response.iter_lines():
        if line:  # 빈 줄 제외
            print(line.decode("utf-8"))








# for msg in smartwork.stream(input=mock):
#     print(msg, flush=True)
#     print("=====================================")