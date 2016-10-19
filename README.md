# dokku-flask-redirect
Redirects catch-all domains in [dokku](https://github.com/dokku/dokku) to a specific URL


Add remote and push:
- `git remote add dokku dokku@<YOUR_DOKKU_DOMAIN>:00-default`
- `git push dokku master`

Set the redirect url:
- `dokku config:set 00-default REDIRECT_URL='http://example.com'`
