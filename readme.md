# Properties API

The following project extracts information from `BigQuery` tables and returns it as JSON through an API developed in `FastAPI`, which can be accessed graphically via Swagger or via REST using Postman. It also uses `Uvicorn` to deploy the local server.


## Project Structure

```bash
/scrapper/
│
├── main.py                 # Main script to execute the API.
├── api/                    # Folder with the modules of the API.
│   ├── __init__.py         # Empty file to python package recognition.
│   ├── security.py         # Script with basic auth configuration.
│   └── endpoint.py         # Script with endpoint configuration.
└── requirements.txt        # Required PIP libraries.
```