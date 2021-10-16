# ML pipeline to expose API on Heroku

## Developer environment

## Run tests

Test suite can be executed by `pytest`.

## Procedures

### Cleaning 

Please run `python main.py --step basic_cleaning`

### Train model 

Please run `python main.py --step train_model`

### Check model score 

Please run `python main.py --step check_score`

### Run entire pipeline

Please run `python main.py --step all`

### Serve the FastAPI on local host

Please run `uvicorn api_server:app --reload`

### Verify Heroku deployed API

Please run `python check_heroku_api.py`

## Rubric docs and screenshots

Requested files by rubric can be found in screenshots and docs folders.
