# AMAZING LIBRARY

#### Technologies:

- Backend:
  - _Django 4_
    - _Djest_ for user management
    - _Django Rest Framework_ for restful API
- Frontend
  - _Vuetify 3_
    - _Vue 3_ as base JS Framework
    - _Axios_ for communication with API
    - _Pinia_ for state management

#### Requirements:

- Python
- yarn

## Initial setup CLI:

Both setups start at the root of the project

#### Backend:

```sh
python3 -m venv env
source env/bin/activate
pip install django
pip install django-rest-framework
pip install django-cors-headers
pip install djoser
pip install pillow
cd backend
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
CREATE SUPERUSER
```

#### Frontend:

```sh
cd frontend
yarn install
```

### To start the project:

#### Backend:

```sh
source env/bin/activate
cd backend
python3 manage.py runserver
```

#### Frontend:

```sh
yarn dev
```

## Database Structure:

Database consists of predefined models made by _Django_ and _Djoser_

There are also custom models made:

- #### Category

  - id - automatic itirator
  - name - string
  - slug - string

- #### Book

  - id - automatic itirator
  - isbn - 13 character string
  - title - string
  - author - string
  - description - string
  - slug - string
  - image - image
  - thumbnail - image
  - date_added - datetime
  - available - boolean
  - category - foreign key to Category model

- #### Order

  - id - automatic itirator
  - created_at - datetime
  - status - string
  - user - foreign key to Order Item model

- #### Order Item
  - id - automatic itirator
  - order - foreign key to Order model
  - book - foreign key to Book model

## API Endpoints:

API endpoints consists of predefined ones made by _Django_ and _Djoser_

All endpoints start with _/api/v1/_

There are also custom endpoints:

#### Book management

<details>
 <summary><code>GET</code> <code>latest-books/</code> <code>(retrieves a list of books ordered descending by _createdAt_)</code></summary>

##### Parameters

> | name | type     | data type | description |
> | ---- | -------- | --------- | ----------- |
> | None | required | N/A       | N/A         |

</details>

<details>
 <summary><code>POST</code> <code>books/search/</code> <code>(retrieves a list of items matching the query)</code></summary>

##### Parameters

> | name  | type     | data type | description                      |
> | ----- | -------- | --------- | -------------------------------- |
> | query | required | string    | Search string to filter books by |

</details>

<details>
 <summary><code>GET</code> <code>books/{category_slug}</code> <code>(returns a list of books in a category)</code></summary>

##### Parameters

> | name | type     | data type | description |
> | ---- | -------- | --------- | ----------- |
> | None | required | N/A       | N/A         |

</details>

<details>
 <summary><code>GET</code> <code>books/{category_slug}/{book_slug}</code> <code>(returns a matching book)</code></summary>

##### Parameters

> | name | type     | data type | description |
> | ---- | -------- | --------- | ----------- |
> | None | required | N/A       | N/A         |

</details>

#### Order management

<details>
 <summary><code>POST</code> <code>checkout/</code> <code>(creates an order)</code></summary>

##### Parameters

> | name  | type     | data type   | description                        |
> | ----- | -------- | ----------- | ---------------------------------- |
> | items | required | array<Book> | Array of book items as order items |

</details>

<details>
 <summary><code>GET</code> <code>orders</code> <code>(returns the list of orders associated to the user)</code></summary>

##### Parameters

> | name | type     | data type | description |
> | ---- | -------- | --------- | ----------- |
> | None | required | N/A       | N/A         |

</details>
