#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=C,R

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
)
from app.database import Base

class Record( Base ):
    __tablename__ = 'records'
    id = Column( Integer, primary_key=True, index=True )
    date = Column( 'datetime', DateTime )
    name = Column( 'name', String )
    value = Column( 'value', Integer )

if __name__ == '__main__':
    from sqlalchemy import create_engine
    from config import DATABASE_URI

    reply = str( input('Proceed creating tables? (y/n): ') )
    if reply.strip().lower() in ['y', 'yes']:
        engine = create_engine( DATABASE_URI )
        reply = str( input('Clear Database? (y/n): ') )
        if reply.strip().lower() in ['y', 'yes']:
            Base.metadata.drop_all( engine )
        Base.metadata.create_all( engine )
