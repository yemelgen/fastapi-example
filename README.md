# Installation
```console
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
# Testing
```console
uvicorn app.main:app --reload --workers 1 --host 0.0.0.0 --port 8000
```
You also can check out http://127.0.0.1:8000/docs for built-in API documentation.
