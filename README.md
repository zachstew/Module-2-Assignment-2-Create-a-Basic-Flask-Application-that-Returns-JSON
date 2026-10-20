# Flask API Assignment

A small Flask REST API demonstrating functions & control flow, JSON data
handling, and error handling.

## Endpoints

| Method | Route   | Description                                              |
|--------|---------|----------------------------------------------------------|
| GET    | /hello  | Optional `name` query param; returns a JSON greeting     |
| POST   | /sum    | Body `{"numbers": [1,2,3]}`; returns `{"sum": 6}`        |

Bad input to `/sum` returns **400** with `{"error": "..."}`.

## Setup (macOS)

```bash
git clone https://github.com/ZachStew/flask_api_assignment.git
cd flask_api_assignment
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

**Outcome:** your terminal shows `(venv)` and Flask and pytest are installed.

> Note: macOS may use port 5000 for AirPlay Receiver. If you get an error saying: "Address already in use" turn it off in System Settings → General → AirDrop & Handoff.

## Run the Server

```bash
python app.py
```

**Outcome:** the server starts at http://127.0.0.1:5000

Try it:

```bash
curl "http://127.0.0.1:5000/hello?name=Sam"
# {"message":"Hello, Sam!"}

curl -X POST http://127.0.0.1:5000/sum -H "Content-Type: application/json" -d '{"numbers":[1,2,3]}'
# {"sum":6}

curl -X POST http://127.0.0.1:5000/sum -H "Content-Type: application/json" -d '{"oops":1}'
# {"error":"Missing required field: 'numbers'."}   (HTTP 400)
```

## Run the Tests
```bash
pytest test_app.py
```
**Outcome:** `9 passed`