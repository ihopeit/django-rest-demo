

## json service
http://127.0.0.1:8000/ to browse json apis
http://127.0.0.1:8000/users/
http://127.0.0.1:8000/questions/
http://127.0.0.1:8000/questions/?format=json
http://127.0.0.1:8000/admin for the admin site.

token based authentication:
generate token: 
    http http://127.0.0.1:8000/api-token-auth/ username=admin password=admin
access api via token: 
    http http://127.0.0.1:8000/users/  "Authorization:Token 8b1a7e57673fec4109324237dacfa13a2c4b5272"
