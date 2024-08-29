from typing import Annotated, List

from pydantic import BaseModel, Field
from pydantic.config import ConfigDict


class Input(BaseModel):
    val: int

class Output(BaseModel):
    res: int

def cleanup(input: Input) -> Output:
    return Output(res=input.val ** 3)
