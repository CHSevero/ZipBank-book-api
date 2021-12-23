# BookAPI
BookAPI is a basic crud operation API for authors and books. This is a dockerized FastAPI and Postgresql project. The API has endpoints to create, get, update and delete authors and books. This project was made for a hiring challenge. You can use this project as a learning example and as a start point to build your own API.

## How to setup
- ### Requirements
    You need to have docker and docker-compose installed and working.
- ### Run the project
  * Go to the project directory root.
  * Make a file called .env
  * Open the .env file and create the following environment variables: 
    * DB_USER=your_db_user
    * DB_PASSWORD=your_db_password
    * DB_NAME=your_db_name
    * DATABASE_URL=postgresql+psycopg2://your_db_user:your_db_password@db:5432/your_db_name
  * Save .env file
  * .env example:
    ```
    DB_USER=postgres
    DB_PASSWORD=password
    DB_NAME=book_api
    DATABASE_URL=postgresql+psycopg2://postgres:password@db:5432/book_api
    ```
  * Open the terminal
  * Type: 
    ``docker-compose up``
  * Press Enter
  * Wait for the project to be built and run
  * When the project is up and running you should see on your terminal:
    ```
    book_api | INFO:     Will watch for changes in these directories: ['/api']
    book_api | INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
    book_api | INFO:     Started reloader process [1] using statreload
    book_api | INFO:     Started server process [10]
    book_api | INFO:     Waiting for application startup.
    book_api | INFO:     Application startup complete.
    ```
  * Go to http://0.0.0.0:8000/docs#/
  * This is the API documentation
  * To use the API you have to create a user with the end “add_user” and log in by clicking on the “Authorize” button and passing the username and password that you created.

## Project Organization
```
├── README.md  <- The top-level README for developers using this project.
├── api
│      ├── app  <- application 
│      │      ├── alembic   <- database migrations
│      │      ├── models    <- database models
│      │      ├── routers   <- api endpoints
│      │      ├── schemas   <- pydantic models
│      │      ├── services  <- services
│      │      ├── test      <- api tests
│      │      └── utils     <- api utils
│      │
│      ├── Dockerfile         <- The final, canonical data sets for modeling
│      └── requirements.txt   <- The original, immutable data dump
│
├── .env  <- Environment variables file
│
├── .gitignore
│
├── docker-compose.yml
│
└── LICENSE  <- Project license
```

## Technologies
The following tools were used on the project construction.
- [Python3.9](https://www.python.org/)
- [Pip](https://pypi.org/project/pip/)
- [Docker](https://www.docker.com/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)  
- [Postgresql](https://www.postgresql.org/)
- [FastAPI-SQLAlchemy](https://pypi.org/project/FastAPI-SQLAlchemy/)
- [Alembic](https://pypi.org/project/alembic/)
- [Psycopg2](https://pypi.org/project/psycopg2/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)
- [Python-jose](https://cryptography.io/en/latest/)
- [Passlib](https://passlib.readthedocs.io/en/stable/)