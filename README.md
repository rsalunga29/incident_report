# Incident Report

Incident Report is a FastAPI & VueJS Practice Project inspired by [Netflix's Dispatch](https://github.com/Netflix/dispatch/). Some line of code from their source code are copied and used here.

## Installation

Clone the project using the Git Clone command

```bash
$ git clone https://github.com/rsalunga29/incident_report
```
Create a Virtual Environment using `virtualenv` package from Pip

```bash
$ cd incident_report
$ pip install virtualenv
$ virtualenv env
```
Activate your Virtual Environment and install all required packages

```bash
$ source env/bin/activate
$ pip install -r requirements-base.txt
$ pip install -r requirements-dev.txt
```

Run Alembic to create your database structure

```bash
$ alembic upgrade head
```

Finally, run your local FastAPI server

```bash
$ uvicorn src.main:app --reload # hot reload enabled
```
