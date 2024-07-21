# Project Endpoints
from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from fastapi import Depends

import app.db_models.crud as crud
from app.api_models.projects import ProjectCreate, ProjectResponse
from app.api.dependencies.sqldb import get_db


router = APIRouter()


