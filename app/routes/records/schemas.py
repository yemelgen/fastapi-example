#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=C,R

from pydantic import BaseModel
from datetime import datetime

class RecordBase(BaseModel):
    date: datetime
    name: str
    value: int

class RecordCreate(RecordBase):
    pass

class RecordUpdate(RecordBase):
    pass

class Record(RecordBase):
    id: int
    
    class Config:
        orm_mode = True

