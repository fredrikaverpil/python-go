# python go extension

- Extending Python with C or C++: https://docs.python.org/3/extending/extending.html
- Python C API: https://docs.python.org/3/c-api
- Based on https://github.com/anthonywritescode/explains/tree/master/sample_code/ep338

## Prerequisites

- go 1.17
- gcc
- python3-dev, libpython3-dev (not sure about these actually...)

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Build and install

```bash
pip install .
```

# Run

```bash
pytest tests.py
```
