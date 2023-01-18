# BilsynAPI-Python-Flask
A web application using the bilsyn API to fetch information about danish license plates. Displayed on a bootstrap html page. Updated to newest version with watchtowerr


Can be run with:
```
version: '3'
services:
  bilsynapi:
    image: ghcr.io/kevinvincentals/bilsynapi-python-flask:latest
    restart: unless-stopped
    environment:
       - token=<insert bearer token here>
    ports:
       - '5000:5000'
    labels:
       - "com.centurylinklabs.watchtower.scope=bilsynapi"

  watchtower:
    image: containrrr/watchtower
    restart: always
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    command: --interval 30 --cleanup --scope bilsynapi
    labels:
      - "com.centurylinklabs.watchtower.scope=bilsynapi"

