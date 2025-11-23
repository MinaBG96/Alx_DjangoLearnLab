# Deployment Configuration for HTTPS

To enable HTTPS in production, the server is configured with SSL/TLS certificates.

For Nginx:

- The server listens on port 443 with SSL enabled.
- Certbot (Let's Encrypt) is used to automatically issue and renew certificates.
- HTTP traffic on port 80 is redirected to HTTPS (port 443).
- X-Forwarded-Proto headers are passed to Django so that SECURE_SSL_REDIRECT works correctly.

Typical Nginx SSL configuration:

server {
listen 80;
server_name example.com;
return 301 https://$host$request_uri;
}

server {
listen 443 ssl;
server_name example.com;

    ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;

    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

}
