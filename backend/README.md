# Backend API

This project is a FastAPI-based application designed to provide weather-related information. It uses OpenWeatherMap API to fetch the data and provides endpoints to retrieve the weather forecast for a specific location, and PixaBay API to fetch images related to the location.

## Prerequisites

- Python 3.12 or higher
- Poetry

## Installation

1. Clone the repository

2. Install the dependencies using Poetry:

```bash
poetry install
```

This command will create a virtual environment and install all the necessary dependencies.

## Running the application

To run the application, execute the following command:

```bash
poetry run start
```

This command will start the FastAPI application and make it available at `http://localhost:8080`.

## Project structure

The project is structured as follows:

```text
.
├── app                     # Main application package
│   ├── cache               # Caching mechanism
│   ├── main.py             # Entry point for the application
│   ├── models              # Data models
│   ├── repositories        # Data access layer
│   ├── routes              # API endpoint definitions
│   ├── schemas             # Pydantic schemas for data validation
│   └── services            # Business logic
├── docker-compose.yaml      # Docker Compose configuration file
├── Dockerfile               # Dockerfile for building the application container
├── .env                     # Environment variables
├── .gitignore               # Git ignore file
├── poetry.lock             # Poetry lock file for dependencies
├── pyproject.toml          # Poetry project configuration
├── README.md               # Project documentation
└── tests                   # Unit and integration tests
```

## Usage

TBD

## Development

To enable the virtual environment created by Poetry, use the following command:

```bash
poetry shell
```

To ensure a consistent development environment, the project uses Poetry for dependency management. To install a new package, use the following command:

```bash
poetry add <package-name>
```

The dependencies will be automatically added to the `pyproject.toml` file and installed in the virtual environment. Some of them can be included as dev or test dependencies by using the `-G` flag:

```bash
poetry add -G dev <package-name>
poetry add -G test <package-name>
```

To run the tests, execute the following command:

```bash
poetry run pytest
```

This command will run all the tests located in the `tests` directory.

For code quality, this project uses Black and Ruff. To format the code and check for linting issues, use the following commands:

```bash
poetry run black .
poetry run ruff check .
```

## Deployment

TBD

## Contact

For any inquiries or issue, pease open an issue in the repository or contact the maintainers.
