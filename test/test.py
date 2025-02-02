
""" PYTHONPATH=. python -m test.test """
from langserve import RemoteRunnable

from app.engines.eval_smartwork.models import *

smartwork = RemoteRunnable("http://localhost:8000/smartwork/")

BASE_URL="http://localhost:8000/smartwork/stream"


mock = EvalSmartWorkState(
    profession=Profession.DESIGNER,
    bookmarks=[
        Bookmark(
            id=0,
            name="Python",
            type=BookmarkType.URL,
            url="https://www.python.org/"
        ),
        Bookmark(
            id=1,
            name="Django",
            type=BookmarkType.URL,
            url="https://www.djangoproject.com/"
        ),
        Bookmark(
            id=2,
            name="생성형 ai",
            type=BookmarkType.FOLDER,
            children=[
                Bookmark(
                    id=3,
                    name="GPT-3",
                    type=BookmarkType.URL,
                    url="https://www.openai.com/gpt-3/"
                ),
                Bookmark(
                    id=4,
                    name="GPT-4",
                    type=BookmarkType.URL,
                    url="https://www.openai.com/gpt-4/"
                ),
            ]
        )
    ],
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