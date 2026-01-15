# FastAPI Auth & Resource API 🚀

A high-performance, production-ready backend built with **FastAPI**. Features secure JWT authentication, password hashing, and paginated resource management. Designed as a foundational architecture for scalable web applications.

## 🛠️ Tech Stack
* **Framework:** FastAPI
* **Database:** SQLite with SQLAlchemy ORM
* **Security:** OAuth2 with Password (Bearer), Passlib (Bcrypt), Python-Jose (JWT)
* **Validation:** Pydantic
* **Server:** Uvicorn

## ✨ Features
* **Secure Authentication:** User signup and login with hashed passwords (Bcrypt).
* **JWT Authorization:** Stateless token-based protection for sensitive endpoints.
* **User Management:** Create, Read, Delete users with skill-based filtering and sorting.
* **Product Management:** Create and list products with authentication.
* **Pagination & Filtering:** Optimized `skip` and `limit` query parameters with skill-based filtering.
* **Sorting:** Sort users by age or creation date (ascending/descending).
* **Robust Error Handling:** Clear HTTP status codes (400, 401, 404).

## 🚀 How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/MohamedSharfan/user-registration-backend.git
cd user-registration-backend
```
### 2. Create a virtual environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
Create a `.env` file in the project root:
```bash
SECRET_KEY=your_super_secret_key_here
```

### 5. Run the server
```bash
uvicorn main:app --reload
```

### Visit http://127.0.0.1:8000/docs to explore the interactive API documentation.

## 🔌 API Endpoints

### Authentication
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/login` | Get access token (JWT) | ❌ |

### Users
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/users/` | Register a new user | ❌ |
| GET | `/users/` | Get all users (sortable by age/created_at) | ❌ |
| GET | `/users/me` | Get current user details | ✅ |
| GET | `/users/{stu_id}` | Get user by ID | ❌ |
| GET | `/users/users?skill=<skill>&skip=0&limit=10` | Filter users by skill (paginated) | ✅ |
| DELETE | `/users/{stu_id}` | Delete a user | ✅ |

### Products
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/products/` | Create a new product | ✅ |
| GET | `/products/items?skip=0&limit=10` | Get list of products (Paginated) | ❌ |



## 🛡️ License
This project is licensed under the MIT License.
