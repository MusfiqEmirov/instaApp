# Instagram Clone (Backend)

This is a backend API for an Instagram-like social media platform built using **Django** and **Django REST Framework (DRF)**. The API supports user authentication, posts, likes, comments, and a follower system.

---

## Features

### User Authentication & Profiles
- **User Registration**: Create a new user with a unique email and hashed password.
- **User Login**: Authenticate users using JWT (access and refresh tokens).
- **User Profile**: Get user details (username, bio, profile picture, followers count, following count).
- **Follow/Unfollow User**: Toggle follow/unfollow for other users.

### Posts & Media
- **Create a Post**: Upload an image with a caption.
- **List Posts**: Get the latest posts from followed users (with pagination).
- **Retrieve Post Details**: Get full post details including comments and likes.
- **Delete a Post**: Only the post owner can delete a post.

### Likes & Comments
- **Like a Post**: Toggle like/unlike for a post.
- **Comment on a Post**: Add a comment to a post.
- **List Comments**: Get all comments for a specific post.

### Stories (Optional)
- **Upload Story**: Upload an image or video that expires after 24 hours.
- **List Active Stories**: Get active stories from followed users.

---

## Technology Stack

- **Backend**: Django, Django REST Framework (DRF)
- **Database**: PostgreSQL (or SQLite for development)
- **Authentication**: JWT (using `djangorestframework-simplejwt`)
- **Storage**: Local storage for images (or cloud storage using `django-storages`)
- **Optional**: Redis (for caching), Celery (for background tasks)

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/MusfiqEmirov/instaApp.git
   cd instagram-clone-backend