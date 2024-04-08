# FastApi Boilerplate

## Description

A starting point for projects using FastApi. Project structure was made keeping in mind for bigger applications. simple authentication with jwt. can manage different versions of a project.

---

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)

---

## Installation

- For Docker: `docker-compose up`
- For Local: `pipenv install`

Run with `uvicorn app.main:app --reload`

---

## Usage

Modify openapi details about the app in main.py

- Add Your Models Under models folder.
- Add The Schemas Under schemas folder.
- Add Endpoints Under routers folder.
- Add Database Query Under operations folder.
- Add Your Env Variables Under config/settings.py

---
