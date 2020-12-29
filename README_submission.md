# Coffee Shop Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in `./src/database/models.py`. We recommend skimming this code first so you know how to interface with the Drink model.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Running the server

From within the `./src` directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

```bash
export FLASK_APP=api.py;
```

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

#### Endpoint description
GET '/drinks'
- Fetches a dictionary of drinks in which the keys are the id, the title and the recipe. The values are the corresponding string of the name, an array containing the different parts of the recipe; parts and color.
- Request Arguments: None
- Returns: An object with a three keys, id, title and recipe:
{
    "drinks": [
        {
            "id": 2,
            "recipe": [
                {
                    "color": "blue",
                    "parts": 2
                }
            ],
            "title": "Water5"
        },
        {
            "id": 5,
            "recipe": [
                {
                    "color": "blue",
                    "parts": 1
                }
            ],
            "title": "Water55"
        }
    ],
    "success": true
}

-------------------------------------------------------------------------------------------------

GET '/drinks-detail'
- Fetches a dictionary of drinks in which the keys are the id, the name and the recipe. The values are the corresponding string of the name, an array containing the different parts of the recipe; parts, color and name.
- Request Arguments: None
- Returns: An object with a three keys, id, name and recipe:
{
    "drinks": [
        {
            "id": 2,
            "recipe": [
                {
                    "color": "blue",
                    "name": "Water",
                    "parts": 2
                }
            ],
            "title": "Water5"
        },
        {
            "id": 5,
            "recipe": [
                {
                    "color": "blue",
                    "name": "Water",
                    "parts": 1
                }
            ],
            "title": "Water55"
        }
    ],
    "success": true
}

-------------------------------------------------------------------------------------------------

POST '/drinks'
- Adds a new entry to the drinks table in the databse and returns the same a GET /drinks-detail.
- Request Arguments: A json object with the keys: title and recipe as e.g.:
{
    "title": "Water20",
    "recipe": [{
        "name": "Water",
        "color": "blue",
        "parts": 1
    }]
}
- Returns: Same as in GET /drinks-detail.

-------------------------------------------------------------------------------------------------

DELETE '/drinks/<int:id>'
- Deletes an entry in the drinks table in the database with the id given in the query parameter
- Request Arguments: None
- Returns: Same as in GET /drinks-detail.

-------------------------------------------------------------------------------------------------

PATCH '/drinks/<int:id>'
- Updates an existing entry in the drinks table in the databse and returns the same a GET /drinks-detail.
- Request Arguments: A json object with the keys: title and recipe or only of them e.g.:
{
    "title": "Water20",
    "recipe": [{
        "name": "Water",
        "color": "blue",
        "parts": 1
    }]
}
or
{
    "title": "Water20"
}
or
{
    "recipe": [{
        "name": "Water",
        "color": "blue",
        "parts": 1
    }]
}
- Returns: Same as in GET /drinks-detail.
