import json
from enum import Enum
from typing import Annotated, List

from pydantic import BaseModel, Field, StrictInt
from pydantic.config import ConfigDict

import random
import dill
from io import BytesIO
import matplotlib.pyplot as plt
import pandas as pd


class Input(BaseModel):
    dataframe: dict

class Output(BaseModel):
    serialized_fig: bytes 

def random_color():
    a = random.randint(0, 200)
    b = random.randint(0, 200)
    c = random.randint(0, 200)
    color = (((a << 8) | b) << 8) | c
    return f'#{color:06x}'

def gen_year_plot(input: Input) -> Output:
    # create dataframe and get year
    df = pd.DataFrame(input.dataframe)
    year = df['Date time'][0].split('/')[2]
    city = df['Address'][2]
    # create figure and plot
    fig, ax = plt.subplots()
    df.plot(x='Date time', y='Temperature', figsize=(13, 8), \
            xlabel='Ziua', ylabel='Temperatura Medie', grid=True, \
            title=f"Temperatura in {year} in {city}", \
            kind='line', ax = ax, color=random_color())    
    # serialize to bytes and return
    byte_stream = BytesIO()
    dill.dump(fig, byte_stream)
    data = byte_stream.getvalue()
    return Output(serialized_fig=data)
