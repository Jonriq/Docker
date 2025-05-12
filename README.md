# BIPM Flask & Docker Demo

A lightweight Flask web app demonstrating:
- A **Home** page with visit counter, footer, external link & image  
- A **Titanic** page showing the first 5 rows of the Titanic dataset and a survivors-by-sex bar chart  
- Static assets (images, CSS) served via Flask  
- Dockerized for easy build & deploy  
- (Optional) Multi-service setup with Redis via Docker Compose

## Prerequisites

- Docker & Docker Compose installed on your machine  
- (Optional, for local dev) Python 3.10+ and `pip-tools`

## Quick Start with Docker

1. **Build the image**  
   ```bash
   cd Docker
   docker build -t bipm_hello .


2. **Run the container**  
   ```bash
   docker run -d -p 8000:80 --name bipm_demo bipm_hello


3. **Browser** 
   Home: eg->  http://localhost:8000/
   Titanic: eg-> http://localhost:8000/titanic

4. **Stop & remove**  
   ```bash
   docker stop bipm_demo
   docker rm bipm_demo


Docker/
├── app/
│   ├── app.py
│   ├── titanic.csv
│   ├── templates/
│   │   ├── hello.html
│   │   └── titanic.html
│   └── static/
│       └── images/
│           ├── myphoto.jpg
│           └── titanic_survival.png
├── Dockerfile
└── README.md           ← this file
