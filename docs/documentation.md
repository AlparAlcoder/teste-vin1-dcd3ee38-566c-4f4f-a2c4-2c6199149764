# User Management API

This is a simple REST API created with FastAPI for managing users. It supports basic CRUD operations: Create, Read, Update, and Delete. 

## Model

### User

The User model is defined with the following attributes:

- `id` (int): The unique identifier of a user
- `name` (str): The name of the user
- `email` (str): The email of the user
- `password` (str): The password of the user

## Endpoints

### POST `/users/`

Create a new user

**Parameters:**

- `user` (User): The user object to create

**Response:**

- A User object

### GET `/users/{user_id}`

Get a user by id

**Parameters:**

- `user_id` (int): The unique identifier of a user

**Response:**

- A User object

### GET `/users/`

Get all users

**Response:**

- A list of User objects

### PUT `/users/{user_id}`

Update a user by id

**Parameters:**

- `user_id` (int): The unique identifier of a user
- `user` (User): The user object to update

**Response:**

- A User object

### DELETE `/users/{user_id}`

Delete a user by id

**Parameters:**

- `user_id` (int): The unique identifier of a user

**Response:**

- A User object

## Example Usage

### Create a User

```python
user = {
    "id": 1,
    "name": "John Doe",
    "email": "jdoe@example.com",
    "password": "secretpass"
}
response = requests.post("http://localhost:8000/users/", json=user)
```

## Important Notes

- User `id` must be unique. Creating a user with an existing `id` will result in an HTTP 400 error.
- When getting, updating, or deleting a user, if the `user_id` does not exist, it will result in an HTTP 404 error.

## Dependencies

This API requires the following Python libraries:

- FastAPI
- Pydantic
- typing
- HTTPException from fastapi