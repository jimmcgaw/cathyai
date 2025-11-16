from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from pydantic import BaseModel

from starlette.responses import FileResponse 

from pipelines import prompt_guard, chatty_cathy


class ChatRequest(BaseModel):
    prompt: str


class ChatResponse(BaseModel):
    prompt: str
    response: str

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def index():
    return FileResponse("static/index.html", media_type="text/html", status_code=200, headers={"Cache-Control": "no-cache"}, content_disposition_type="inline")


@app.post("/chat")
async def chat(request: ChatRequest) -> ChatResponse:
    prompt = request.prompt
    prompt_guard_result = prompt_guard(prompt)
    # a really weak, initial guard against injection attacks
    # TODO: use score value to determine if prompt is safe,
    # transform prompt into a system prompt and user prompt,
    # and include a model to backtranslate the input.
    if prompt_guard_result[0]["label"] == "JAILBREAK":
        return {
            "prompt": prompt,
            "prompt_guard_score": prompt_guard_result[0]["score"],
            "result": "I'm sorry, I can't do that.",
        }

    # TODO: do some validation of the response
    response = chatty_cathy(prompt)
    return ChatResponse(prompt=prompt, response=response)