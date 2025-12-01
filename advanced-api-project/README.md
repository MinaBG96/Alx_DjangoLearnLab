## Filtering, Searching, and Ordering for Book API

### Base endpoint
`GET /api/books/`

### Filtering

You can filter by:
- `title`
- `author`
- `publication_year`

Examples:
- `/api/books/?title=1984`
- `/api/books/?author=1`
- `/api/books/?publication_year=1997`

### Searching

Search is enabled on:
- `title`
- `author__name`

Examples:
- `/api/books/?search=Harry`
- `/api/books/?search=Rowling`

### Ordering

You can order by:
- `title`
- `publication_year`

Examples:
- `/api/books/?ordering=title`
- `/api/books/?ordering=-title`
- `/api/books/?ordering=publication_year`
- `/api/books/?ordering=-publication_year`
