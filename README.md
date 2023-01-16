# BilsynAPI-Python-Flask
The code behind docker image https://hub.docker.com/r/xkaas/bilapi, a web application using the bilsyn API to fetch information about danish license plates


Can be run with:
```version: '2' 
services: 
  bilsynapi: 
    image: ghcr.io/kevinvincentals/bilsynapi-python-flask:latest
    restart: unless-stopped
    environment:
       - token=<insert bearer token here>
    ports: 
       - '5000:5000'
