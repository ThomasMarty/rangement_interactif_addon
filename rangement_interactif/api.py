from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse
import sqlite3
import os
from typing import List
from pydantic import BaseModel


DB_PATH = '/data/rangement.db' if os.path.isdir('/data') else 'rangement.db'
app = FastAPI()


def get_db():
conn = sqlite3.connect(DB_PATH)
conn.row_factory = sqlite3.Row
return conn


@app.get('/')
def root():
return HTMLResponse(open('ui/index.html','r', encoding='utf-8').read())


@app.get('/ui/{path}')
def ui_static(path: str):
p = os.path.join('ui', path)
if not os.path.exists(p):
raise HTTPException(status_code=404, detail='Not found')
if p.endswith('.js'):
return FileResponse(p, media_type='application/javascript')
if p.endswith('.css'):
return FileResponse(p, media_type='text/css')
return FileResponse(p)


@app.get('/api/blocs')
def api_blcs():
conn = get_db()
cur = conn.cursor()
cur.execute('SELECT * FROM blocs')
rows = [dict(r) for r in cur.fetchall()]
conn.close()
return JSONResponse(rows)


@app.get('/api/positions')
def api_positions():
conn = get_db()
cur = conn.cursor()
cur.execute('SELECT * FROM positions')
rows = [dict(r) for r in cur.fetchall()]
conn.close()
return JSONResponse(rows)


return JSONResponse({'ok':True, 'tiroir_id': payload.tiroir_id, 'color': payload.color, 'duration': payload.duration})
