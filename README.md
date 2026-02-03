# sentiment-analysis-app

A minimal Streamlit app that performs sentiment analysis using VADER.

## Run locally

Install dependencies and run the app:

```bash
python -m pip install -r requirements.txt
streamlit run app.py
```

See `RUN.md` for a quick reminder.

## Docker

Build and run with Docker:

```bash
docker build -t sentiment-app .
docker run -p 8501:8501 sentiment-app
```

The app will be available at http://localhost:8501.

## Deployment

A simple `Procfile` is included for Heroku-like platforms:

```
web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
```

License: MIT
# sentiment-analysis-app