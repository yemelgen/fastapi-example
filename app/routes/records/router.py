#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=C,R

from io import StringIO
from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from app.database import get_db
from . import models, schemas

api = APIRouter()

# Create a new record
@api.post( '/' )
async def create_record( data: schemas.RecordCreate, db: Session = Depends(get_db) ):
    record = models.Record( **data.dict() )
    db.add( record )
    db.commit()
    db.refresh( record )
    return {'detail': 'Record created successfully', 'record': record }

# Retrive a record by ID
@api.get('/{record_id}')
async def get_record( record_id: int, db: Session = Depends(get_db) ):
    record = db.query( models.Record ).filter( models.Record.id == record_id).first()
    if not record:
        raise HTTPException( status_code=404, detail='Record not found')
    return { 'record': record }

# Retrive all records
@api.get( '/', response_class=StreamingResponse )
async def get_all_records( db: Session = Depends(get_db) ):
    records = db.query( models.Record ).all()
    csv = StringIO()
    for record in records:
        csv.write( f'{record.date},{record.name},{record.value}\n' )
    csv.seek(0)
    headers = {
        'Content-Disposition': 'attachment; filename="records.csv"'
    }
    return StreamingResponse( iter([csv.getvalue()]), media_type='text/csv', headers=headers )

# Update a record
@api.put('/{record_id}')
async def update_record( record_id: int, data: schemas.RecordUpdate, db: Session=Depends(get_db) ):
    record = db.query( models.Record ).filter( models.Record.id == record_id).first()
    if not record:
        raise HTTPException( status_code=404, detail='Record not found')

    for key, value in data.dict( exclude_unset=True ).items():
        setattr( record, key, value )
    db.add( record )
    db.commit()
    db.refresh( record )
    return { 'detail': 'Record updated successfully', 'record': record }

# Delete a record
@api.delete('/{record_id}')
async def delete_record( record_id: int, db: Session=Depends(get_db)  ):
    record = db.query( models.Record ).filter( models.Record.id == record_id).first()
    if not record:
        raise HTTPException( status_code=404, detail='Record not found')
    db.delete( record )
    db.commit()
    return {'detail': 'Record deleted successfully' }

