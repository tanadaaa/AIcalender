from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import Field, BaseModel
from typing import Optional
from datetime import datetime

model_openai = ChatOpenAI(model="gpt-4o-mini")


def create_extract_prompt() -> ChatPromptTemplate:
    return ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "あなたは抽出アルゴリズムの専門家です。"
                "テキストから関連情報だけを抽出します。"
                "抽出を求められた属性の値がわからない場合、その属性の値に対してNoneを返します。",
            ),
            ("{text}"),
        ]
    )


class CalendarEventSchema(BaseModel):

    starttime: Optional[str] = Field(
        default=None,
        description=f"カレンダーに入れるイベントの開始時刻を表す文字列。現在時刻は{datetime.now().strftime('%Y-%m-%dT%H:%M:%S')}。出力の形式は'YYYY-MM-DDTHH:MM:SS'にしなさい。例: 2021-01-01T00:00:00",
    )

    endtime: Optional[str] = Field(
        default=None,
        description=f"カレンダーに入れるイベントの終了時刻を表す文字列。現在時刻は{datetime.now().strftime('%Y-%m-%dT%H:%M:%S')}。出力の形式は'YYYY-MM-DDTHH:MM:SS'にしなさい。例: 2021-01-01T01:09:00",
    )

    place: Optional[str] = Field(
        default=None,
        description="カレンダーに入れるイベントの場所を表す文字列。",
    )

    element: Optional[str] = Field(
        default=None,
        description="カレンダーに入れるイベントが何かを表す文字列。",
    )


def process_parse(natural_text):

    model = model_openai
    extract_prompt = create_extract_prompt()
    runnable = extract_prompt | model.with_structured_output(schema=CalendarEventSchema)
    result = runnable.invoke({"text": natural_text})

    return result
