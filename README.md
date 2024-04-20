# Oceanographic cruise scraper

## About

Extract oceanographic cruise information based on DOI and write it to a csv file.

## Requirements

- python3

## Setup

Create a python virtual environment and activate it.

```bash
python3 -m venv .venv

source .venv/bin/activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

## How to use

### Extract oceanographic cruise information

Retrieve cruise DOI (e.g. 18003056 for FE2M 2024) and enter the following command.

```bash
python3 main.py 18003056 output_file.csv
```

### Append an existing output file

Simply add `--append` to the previous command.

```bash
python3 main.py --append 18003056 output_file.csv
```
