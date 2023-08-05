import os
import shutil
import time
import stat
import gradio as gr
import modules.extras
import modules.ui
from modules.shared import opts, cmd_opts
from modules import shared, scripts
from modules.paths_internal import extensions_dir
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
import json
from modules import shared
from fastapi import APIRouter

pg_ip = "127.0.0.1"
#pg_ip = "127.0.0.1" if shared.cmd_opts.listen else 'localhost'
pg_port = 5173



def on_ui_settings():
    global pg_ip
   
    with open(os.path.join(extensions_dir, 'prompt_gallery_name.json')) as fd:
        name = json.load(fd)['name']
    # os.chmod('./extensions/'+name, stat.S_IRWXO)
    app = FastAPI()
    app.mount('/', StaticFiles(directory=extensions_dir+"/"+name,html=True))
    config = Config(app=app,  host=pg_ip,port=pg_port, log_level="info", loop="asyncio", limit_max_requests=1)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"], 
        allow_credentials=True, 
        allow_methods=["*"], 
        allow_headers=["*"]  
    )

    thread = threading.Thread(target= uvicorn.run, kwargs={'app':app, 'host': pg_ip, 'port':pg_port})
    thread.start()

    wait_time = 0
    if_connect =False

    while if_connect == False and wait_time<=6:
        try:
            tmp = requests.get("http://{}:{}".format(pg_ip, str(pg_port)))
            if_connect = True if int(tmp.status_code) /100 == 2. or int(tmp.status_code) /100 == 2 else False
        except:
            print(".")
            time.sleep(1)
            wait_time+=1


def on_ui_tabs():
    if  shared.cmd_opts.theme is None or shared.cmd_opts.theme != 'dark':
        extension_theme = 'white'
    else:
        extension_theme = 'black'
    remote_webui = '127.0.0.1'
    if  shared.cmd_opts.server_name:
        remote_webui = str(shared.cmd_opts.server_name)
    port = str(shared.cmd_opts.port) if shared.cmd_opts.port is not None else "7860"
    
    html = """<script>var ip = window.location.hostname; </script>
    <iframe id="tab_iframe" allow="clipboard-read; clipboard-write" style="width: 100%; min-height: 1080px; padding: 0;margin: 0;border: none;" src="http://{pg_ip:s}:{pg_port:s}/?theme={theme:s}&port={port:s}&ip={remote_webui:s}" frameborder="0" marginwidth="0" marginheight="0"></iframe>""".format(pg_ip=pg_ip, pg_port=str(pg_port), remote_webui=remote_webui, theme=extension_theme, port=port)
    with gr.Blocks(analytics_enabled=False, elem_id="prompt_gallery") as prompt_gallery:
        prompt_gallery = gr.HTML(html)
    
    return (prompt_gallery , "Prompt Gallery", "prompt_gallery"),

script_callbacks.on_ui_tabs(on_ui_tabs)

script_callbacks.on_ui_settings(on_ui_settings)