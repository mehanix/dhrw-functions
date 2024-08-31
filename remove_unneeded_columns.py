import json
from enum import Enum
from typing import Annotated, List

from pydantic import BaseModel, Field, StrictInt
from pydantic.config import ConfigDict


class Input(BaseModel):
    csv_chunk: str

class Output(BaseModel):
    csv_filtered_columns: List[List[int]] 

def csv_to_int_arr(input: Input) -> Output:
    res = []
    print(input.array)
    lines = input.csv_chunk.split(f'{chr(10)}')
    data = lines[1:]
    to_keep_indexes_columns = [0,1,2,3,6]
    for line in data:
        processed = []
        chunks = [x.strip() for x in lines[0].split(',')]
        for idx, chunk in chunks:
            if idx in to_keep_indexes_columns:
                processed.append(chunk)
        res.append(processed)
    return Output(data=res)
