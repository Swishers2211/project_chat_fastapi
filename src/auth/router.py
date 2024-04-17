from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory='templates')

router = APIRouter(
    prefix='/user',
    tags=['auth']
)
