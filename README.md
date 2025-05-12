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



