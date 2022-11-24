import os
import shutil
import time
import stat
import gradio as gr
import modules.extras
import modules.ui
from modules.shared import opts, cmd_opts
from modules import shared, scripts
from modules import script_callbacks
from pathlib import Path
from typing import List, Tuple
import uvicorn
from uvicorn import Config
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import contextlib
import threading
import requests
from fastapi.middleware.cors import CORSMiddleware
  

def on_ui_settings():
    app = FastAPI()
    app.mount('/', StaticFiles(directory='./extensions/prompt-gallery',html=True))
    config = Config(app=app,  host='localhost',port=5173, log_level="info", loop="asyncio", limit_max_requests=1)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"], 
        allow_credentials=True, 
        allow_methods=["*"], 
        allow_headers=["*"]  
    )
    
    thread = threading.Thread(target= uvicorn.run, kwargs={'app':app, 'host': 'localhost', 'port':5173})
    thread.start()
    tmp = requests.get("http://localhost:5173")
    while tmp.status_code != 204 and tmp.status_code != 200:
        time.sleep(0.01)
        tmp = requests.get("http://localhost:5173")
    pass
    # thread.join()



def on_ui_tabs():
    html = """<iframe id="tab_iframe" style="width: 100%; min-height: 864px; padding: 0;margin: 0;border: none;" src="http://localhost:5173/" frameborder="0" marginwidth="0" marginheight="0"></iframe>"""
    with gr.Blocks(analytics_enabled=False, elem_id="prompt_gallery") as prompt_gallery:
        prompt_gallery = gr.HTML(html)
    
    return (prompt_gallery , "Prompt Gallery", "prompt_gallery"),

script_callbacks.on_ui_tabs(on_ui_tabs)

script_callbacks.on_ui_settings(on_ui_settings)