# BilsynAPI-Python-Flask
A web application using the bilsyn API to fetch information about danish license plates. Displayed on a bootstrap html page. 


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
