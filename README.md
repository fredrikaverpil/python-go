# Extend Python with Go

## Prerequisites

- go 1.21.0
- python 3.11

## Setup

Set up Python virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Build:

```bash
# linux
go build -buildmode=c-shared -o fib.so

# macOS
go build -buildmode=c-shared -o fib.dylib

# windows
go build -buildmode=c-shared -o fib.dll
```

## Run

```bash
python main.py
```

## Docs

- https://docs.python.org/3/library/ctypes.html
- https://pkg.go.dev/cmd/cgo
