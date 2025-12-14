## Posts Endpoints
GET /api/posts/
POST /api/posts/
PUT /api/posts/{id}/
DELETE /api/posts/{id}/

## Comments Endpoints
GET /api/comments/
POST /api/comments/
PUT /api/comments/{id}/
DELETE /api/comments/{id}/

Authentication: Token
Authorization Header:
Authorization: Token <token>

## Follow System
POST /api/accounts/follow/{user_id}/
POST /api/accounts/unfollow/{user_id}/

## Feed
GET /api/feed/

Authentication:
Authorization: Token <token>

