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
# Comment System for Blog

Features:
- Each post can have multiple comments.
- Anyone can read comments on a post.
- Only authenticated users can add comments.
- Only the author of a comment can edit or delete it.

URLs:
- Add comment: /post/<post_id>/comments/new/
- Edit comment: /comment/<comment_id>/update/
- Delete comment: /comment/<comment_id>/delete/

Comment Model:
- post: ForeignKey to Post
- author: ForeignKey to User
- content: TextField
- created_at: auto_add_now
- updated_at: auto_now

# Tagging and Search Features

Tagging:
- Each Post can have multiple Tags.
- Tags are entered as a comma-separated list in the post form (e.g. "django, backend, api").
- Tags are automatically created if they do not exist.
- On the post detail page, tags are shown and each tag links to a page showing all posts with that tag.

Search:
- A search bar is available on the posts list page.
- Search matches:
  - Post title
  - Post content
  - Tag names
- Search results are shown at `/search/?q=<keyword>`.

URLs:
- View posts by tag: `/tags/<tag_name>/`
- Search posts: `/search/?q=<keyword>`
