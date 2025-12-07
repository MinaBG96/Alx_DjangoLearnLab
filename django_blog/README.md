# Blog Post Management

Features:
- List all posts at `/posts/`
- View post details at `/posts/<id>/`
- Create new post at `/posts/new/` (login required)
- Edit existing post at `/posts/<id>/edit/` (author only)
- Delete post at `/posts/<id>/delete/` (author only)

Permissions:
- Anonymous users can only view list and detail pages.
- Authenticated users can create new posts.
- Only the author of a post can edit or delete it.
