from typing import Dict

from fastapi import APIRouter

from pydantic import BaseModel
from app.task.chatbot import ComfortBot
from app.models import skillTemplate

router = APIRouter(
    prefix="/chatbot",
    tags=["chatbot"],
    responses={404: {"description": "Not found"}},
)


class ComfortBotTestRequest(BaseModel):
    query: str


class ComfortbotRequest(BaseModel):
    userRequest: Dict


@router.post("/respond")
async def comfort(request: ComfortBotTestRequest):
    answer = ComfortBot().reply(request.query)
    return {"answer": answer}


@router.post("/kakao/respond")
async def kakao(request: ComfortbotRequest):
    # print(json.dumps(request.__dict__, ensure_ascii=False, indent=2))
    query = request.userRequest["utterance"]
    result = ComfortBot().reply(query)
    return skillTemplate.send_response(result)
