
#  Movie Review API

This is a Django REST Framework (DRF) backend project that allows users to register, log in, and manage movie reviews. Each review includes a movie title, content, rating (1–5), and is linked to the user who created it. The API supports authentication, filtering, pagination, and includes unique features like likes and user profiles.

---

## Tech Stack

- Python 3
- Django
- Django REST Framework
- MySQL (or SQLite for local testing)
- JWT Authentication (`djangorestframework-simplejwt`)

---

##  Setup Instructions

1. **Clone the repo**
   ```bash
   git clone https://github.com/Nolii29/movie_review_api.git
   cd movie_review_api
   ```

2. **Create and activate virtual environment**
   ```bash
   pip install virtualenv
   virtualenv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure database in `settings.py`**
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'movie_reviews',
           'USER': 'your_mysql_user',
           'PASSWORD': 'your_mysql_password',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

5. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Start server**
   ```bash
   python manage.py runserver
   ```

---

##  ERD Diagram

```
User
 └── id
 └── username
 └── email
 └── password

Review
 └── id
 └── movie_title
 └── content
 └── rating (1–5)
 └── user (FK to User)
 └── created_at
 └── likes (M2M to User)
```

---

##  Authentication

- JWT-based login
- Only authenticated users can create, update, or delete reviews
- Users can only modify their own reviews

---

##  API Endpoints

###  Auth & Users
| Method | Endpoint                  | Description                  |
|--------|---------------------------|------------------------------|
| POST   | `/api/register/`          | Register new user            |
| POST   | `/api/token/`             | Get JWT token                |
| POST   | `/api/token/refresh/`     | Refresh JWT token            |
| GET    | `/api/profile/`           | View logged-in user's reviews |

### 🔹 Reviews
| Method | Endpoint                          | Description                          |
|--------|-----------------------------------|--------------------------------------|
| GET    | `/api/reviews/`                   | List all reviews                     |
| POST   | `/api/reviews/`                   | Create a review (auth required)      |
| PUT    | `/api/reviews/<id>/`              | Update own review                    |
| DELETE | `/api/reviews/<id>/`              | Delete own review                    |
| POST   | `/api/reviews/<id>/like/`         | Like a review                        |
| POST   | `/api/reviews/<id>/unlike/`       | Unlike a review                      |
| GET    | `/api/reviews/top_reviews/?movie_title=Inception` | Top liked reviews for a movie |
| GET    | `/api/reviews/?movie_title=Inception` | Filter by movie title           |
| GET    | `/api/reviews/?rating=5`          | Filter by rating                     |

---

## Sample curl Commands

### Register
```bash
curl -X POST http://localhost:8000/api/register/ \
-H "Content-Type: application/json" \
-d '{"username":"palesa","email":"palesa@example.com","password":"pass123"}'
```

### Get Token
```bash
curl -X POST http://localhost:8000/api/token/ \
-H "Content-Type: application/json" \
-d '{"username":"palesa","password":"pass123"}'
```

### Create Review
```bash
curl -X POST http://localhost:8000/api/reviews/ \
-H "Authorization: Bearer <your_token>" \
-H "Content-Type: application/json" \
-d '{"movie_title":"Inception","content":"Loved it!","rating":5}'
```

### Like a Review
```bash
curl -X POST http://localhost:8000/api/reviews/1/like/ \
-H "Authorization: Bearer <your_token>"
```

---

##  Unique Features

-  Users can like/unlike reviews
-  Users can view their own submitted reviews
-  Endpoint to show top liked reviews for a movie

---


