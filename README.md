# Pantry

A feature store: define a feature once, serve it offline for training and online for low-latency inference.

> **Status: planned.** This repository is a skeleton. The plan is below; work starts at M1.

## What it will do

- Registers feature definitions with owners, types and freshness expectations.
- Materialises features to an offline store and produces point-in-time correct training sets.
- Syncs the latest values to an online store and serves them over an API.
- Detects training/serving skew between the offline and online values.

## Planned stack

Python · DuckDB · Parquet · Redis · FastAPI

## Milestones

- [x] **M0**: repository skeleton and CI
- [ ] **M1**: Feature registry and offline materialisation to Parquet
- [ ] **M2**: Point-in-time joins for leakage-free training sets
- [ ] **M3**: Online store and serving API
- [ ] **M4**: Freshness monitoring and skew checks

## Layout

```
src/pantry/   package source
tests/             unit tests
```

## Getting started

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e .
python -m unittest discover -s tests -v
```

---

Part of [Sagar Arora's data engineering projects](https://github.com/sagararora492).
