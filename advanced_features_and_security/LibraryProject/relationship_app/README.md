"""
Permissions / Groups Setup:
---------------------------

Custom permissions defined in Book model:
- can_view
- can_create
- can_edit
- can_delete

Groups recommended:
- Viewers: can_view
- Editors: can_edit, can_create
- Admins: all permissions

These permissions are enforced in views using @permission_required.
"""
