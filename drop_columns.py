import json
from enum import Enum
from typing import Annotated, List

from pydantic import BaseModel, Field, StrictInt
from pydantic.config import ConfigDict


class Input(BaseModel):
    array: List[int]

class Output(BaseModel):
    ans: StrictInt

def process(input: Input) -> Output:
    return Output(ans=sum(input.array))