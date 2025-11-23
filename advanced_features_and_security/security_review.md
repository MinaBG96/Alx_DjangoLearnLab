# Security Review

This project implements the following security measures:

1. **HTTPS Enforcement**
   - All HTTP requests are redirected to HTTPS using `SECURE_SSL_REDIRECT = True`.
   - HSTS is enabled to force browsers to use HTTPS (`SECURE_HSTS_SECONDS = 31536000`).

2. **Secure Cookies**
   - `SESSION_COOKIE_SECURE` and `CSRF_COOKIE_SECURE` ensure cookies are sent only over HTTPS.

3. **Browser Security Headers**
   - `X_FRAME_OPTIONS = "DENY"` prevents clickjacking.
   - `SECURE_CONTENT_TYPE_NOSNIFF = True` blocks MIME type sniffing.
   - `SECURE_BROWSER_XSS_FILTER = True` activates browser XSS filters.

4. **CSRF Protection**
   - All templates include `{% csrf_token %}` to protect POST requests.

5. **Correct Deployment Practices**
   - Nginx configured with SSL certificates (Let's Encrypt).
   - Certbot automates certificate renewal.
   - X-Forwarded-Proto header ensures Django understands HTTPS behind reverse proxy.

These settings protect the application from XSS, CSRF, clickjacking, downgrade attacks, and cookie hijacking.
