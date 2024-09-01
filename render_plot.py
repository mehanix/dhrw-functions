import json
from enum import Enum
from typing import Annotated, List

from pydantic import BaseModel, Field, StrictInt
from pydantic.config import ConfigDict

import dill
from io import BytesIO
import matplotlib.pyplot as plt
from base64 import b64encode

class Input(BaseModel):
    serialized_fig: bytes

class Output(BaseModel):
    base64_png: str

def render_plot(input: Input) -> Output:
    byte_stream = BytesIO(input.serialized_fig)
    fig = dill.load(byte_stream)
    plt.figure(fig)
    
    byte_stream.close()
    byte_stream = BytesIO()
    plt.savefig(byte_stream, dpi=100, format='png')
    img_bytes = byte_stream.getvalue()
    b64 = b64encode(img_bytes)
    return Output(base64_png: b64.decode())
