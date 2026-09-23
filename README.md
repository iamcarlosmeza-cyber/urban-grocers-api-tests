# Urban Grocers — API Test Automation

Automated API tests for Urban Grocers, a grocery delivery app. The suite validates the `name` field of the create-kit endpoint with 9 positive and negative tests.

## Stack
- Python 3 · pytest · Requests

## What's tested
Create-kit endpoint, `name` field:
- Valid names are accepted
- Empty name is rejected
- Maximum length is enforced

## Run it
```bash
pip install -r requirements.txt
```

The API ran on a temporary TripleTen test server. Set the server URL in `configuration.py`, then run:

```bash
pytest -v
```

## Project structure
- `test_create_kit_name.py` — test suite
- `sender_stand_request.py` — API request helpers
- `configuration.py` — server settings
- `data.py` — test data

Built as part of the TripleTen QA Engineering program.
