import json
from enum import Enum
from typing import Annotated, List
from pydantic import BaseModel, Field
from pydantic.config import ConfigDict

import pandas as pd
from io import StringIO

class Input(BaseModel):
    csv_chunk: str

class Output(BaseModel):
    dataframe: pd.core.frame.DataFrame

def filter_columns(data: Input) -> Output:
    COLUMNS = ['Date time', 'Temperature']
    
    csv_io = StringIO(data.csv_chunk)
    df = pd.read_csv(csv_io)
    df_filtered = df[COLUMNS]
    return Output(dataframe=df_filtered)
