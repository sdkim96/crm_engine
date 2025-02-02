#!/usr/bin/env python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.engines import chatbot, eval_smartwork
from app.engines import BasicChatbotState, EvalSmartWorkState

from langserve import add_routes

app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple api server using Langchain's Runnable interfaces",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

add_routes(
    app,
    chatbot,
    path="/openai",
    input_type=BasicChatbotState,
    output_type=BasicChatbotState,
)

add_routes(
    app,
    eval_smartwork,
    path="/smartwork",
    input_type=EvalSmartWorkState,
    output_type=EvalSmartWorkState,
)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)