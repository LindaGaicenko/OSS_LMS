# LIBRARY MANAGEMENT SYSTEM

#### Technologies:

- Backend:
  - _Django 4_
    - _Djest_ for user management
    - _Django Rest Framework_ for RESTful API
    - _Django Filters_ for advanced data filtering
- Frontend
  - _Vuetify 3_
    - _Vue 3_ as base JS Framework
    - _Axios_ for communication with API
    - _Pinia_ for state management
    - And more smaller importance packages

#### Requirements:

- Python 3
- Yarn

## Initial setup CLI:

Both setups start at the root of the project

#### Backend:

```sh
python -m venv env
# Windows
env/Scripts/activate
# Linux/Mac
source env/bin/activate
pip install django django-filter django-rest-framework django-cors-headers djoser pillow
cd backend
python manage.py migrate
python manage.py createsuperuser
```

#### Frontend:

```sh
cd frontend
yarn install
```

### To start the project:

#### Backend:

```sh
# Windows
env/Scripts/activate
# Linux/Mac
source env/bin/activate
cd backend
python manage.py runserver
```

#### Frontend:

```sh
cd frontend
yarn dev
```

## Database Structure:

Database consists of predefined models made by _Django_ and _Djoser_

There are also custom models made:

- #### Category

  - name - string
  - description - string
  - slug - string

- #### Item

  - user_groups - string
  - type - string
  - isbn - 13 character string
  - title - string
  - author - string
  - publisher - string
  - publication_date - string
  - description - string
  - slug - string
  - image - foreign key ImageField
  - thumbnail - foreign key ImageField
  - is_external - boolean
  - file_url - string
  - file - foreign key FileField
  - date_added - datetime
  - available - boolean
  - category - foreign key to Category

- #### Reservation

  - created_at - datetime
  - status - string
  - user - foreign key to Reservation Item model

- #### Reservation Item
  - reservation - foreign key to Reservation model
  - item - foreign key to Item model

## API Endpoints:

API endpoints consists of predefined ones made by _Django_ and _Djoser_

All endpoints start with _/api/v1/_

There are also custom endpoints:

#### Item management

<details>
 <summary><code>GET</code> <code>latest-items/</code> <code>(retrieves a list of items ordered descending by _createdAt_)</code></summary>

##### Parameters

> | name | type     | data type | description |
> | ---- | -------- | --------- | ----------- |
> | None | required | N/A       | N/A         |

</details>

<details>
 <summary><code>GET</code> <code>items/</code> <code>(retrieves a list of items matching the parameters)</code></summary>

##### Parameters

> | name      | type     | data type | description                                    |
> | --------- | -------- | --------- | ---------------------------------------------- |
> | from_date | required | string    | Search publication_date greater/equal to value |
> | to_date   | required | string    | Search publication_date lower/equal to value   |
> | type      | required | string    | Search type exact                              |

</details>

<details>
 <summary><code>GET</code> <code>items/filter</code> <code>(retrieves an object of data for the items filter)</code></summary>

##### Parameters

> | name | type     | data type | description |
> | ---- | -------- | --------- | ----------- |
> | None | required | N/A       | N/A         |

</details>

<details>
 <summary><code>POST</code> <code>items/search/</code> <code>(retrieves a list of items matching the query)</code></summary>

##### Parameters

> | name  | type     | data type | description                      |
> | ----- | -------- | --------- | -------------------------------- |
> | query | required | string    | Search string to filter items by |

</details>

<details>
 <summary><code>GET</code> <code>items/{category_slug}</code> <code>(returns a list of items in a category)</code></summary>

##### Parameters

> | name | type     | data type | description |
> | ---- | -------- | --------- | ----------- |
> | None | required | N/A       | N/A         |

</details>

<details>
 <summary><code>GET</code> <code>items/{category_slug}/{item_slug}</code> <code>(returns a matching item)</code></summary>

##### Parameters

> | name | type     | data type | description |
> | ---- | -------- | --------- | ----------- |
> | None | required | N/A       | N/A         |

</details>

#### Reservation management

<details>
 <summary><code>POST</code> <code>checkout/</code> <code>(creates an reservation)</code></summary>

##### Parameters

> | name  | type     | data type   | description                              |
> | ----- | -------- | ----------- | ---------------------------------------- |
> | items | required | array<item> | Array of item items as reservation items |

</details>

<details>
 <summary><code>GET</code> <code>reservations</code> <code>(returns the list of reservations associated to the user)</code></summary>

##### Parameters

> | name | type     | data type | description |
> | ---- | -------- | --------- | ----------- |
> | None | required | N/A       | N/A         |

</details>
