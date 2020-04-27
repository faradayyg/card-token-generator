# card-token-generator
This generates a token and stores it against a card, which will be used later in transactions

## Setup

Steps in setting up this application.
There are two ways:

- Docker
- local python setup

### Docker setup
Setting up using docker

#### Prerequisites
- docker
- docker-compose
- A database

#### Steps
- clone this repository
- copy `.env.example` to `.env` 
- fill in .env with the correct settings
- run `docker-compose up -d`
- visit http://your-ip:8009

You can setup reverse proxy to serve on a domain


### Local setup
Setting up using your local python build 

#### Prerequisites
- python3
- python3 venv
- pip

#### Steps
- clone this repository
- copy `.env.example` to `.env` 
- fill in .env with the correct settings
- install requirements: run `pip install -r requirements.txt`
- to serve the app: run `flask run`
- Visit http://your-ip:5000

## Questions
Contact:

- Friday Godswill faradayyg@gmail.com

Api documentation: https://documenter.getpostman.com/view/3444520/SzfCV69W?version=latest
