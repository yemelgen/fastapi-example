#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=C,R

from fastapi import FastAPI

from app.database import engine
from app.routes.records import router
from app.routes.records import models

models.Base.metadata.create_all( engine )

app = FastAPI()

app.include_router( router.api, tags=['Records'], prefix='/v1.0/records')
