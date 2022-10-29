from typing import Union
from fastapi import FastAPI, Request, Response
from fastapi.responses import PlainTextResponse
import gradio as gr
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
import logging
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)  
limiter = Limiter(key_func=get_remote_address)
app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

from models import serverless_diffusion

@app.get("/expensive")
@limiter.limit("5/minute")
async def homepage(request: Request, response: Response):
    return {"key": "value"}


app.mount('/serverless_diffusion', serverless_diffusion.gradio_app())

@app.get("/")
def read_main():
    return {"message": "This is your main app"}



# GRADIO_ROOT = "/gradio"
# io = gr.Interface(lambda x: "Hello, " + x + "!", "textbox", "textbox")
# gradio_app = gr.routes.App.create_app(io)
# app.mount(GRADIO_ROOT, gradio_app)
