# pipeline-challenge

Final challenge of the Syntax DevOps course, Day 5: debug a broken CI/CD pipeline.

The app is a tiny calculator library (`summe`, `durchschnitt`, `prozent`) with pytest tests.
The workflow in `.github/workflows/pipeline.yml` is the broken version from the task, unchanged.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest -v
```

This repo is temporary and will be deleted after the course.
