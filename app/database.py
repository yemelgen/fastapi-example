#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=C,R

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from app.config import DATABASE_URI

engine =  create_engine( DATABASE_URI )
SessionLocal = sessionmaker( autocommit=False, autoflush=False, bind=engine )
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
