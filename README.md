# pipeline-challenge

Final challenge of the Syntax DevOps course, Day 5: debug a broken CI/CD pipeline.

The app is a tiny calculator library (`summe`, `durchschnitt`, `prozent`) with pytest tests.
The workflow in `.github/workflows/pipeline.yml` started as the broken version from the task.
It is now repaired: all jobs are green, and it meets the ten minimum requirements of the task.

## Pipeline

One workflow, four jobs:

```
test ──> build ──> deploy ──> release
            └──────────────────┘ (artifact app-paket)
```

| Job       | What it does                                                                  |
| --------- | ----------------------------------------------------------------------------- |
| `test`    | Sets up Python 3.12, restores the pip cache, installs `requirements.txt`, runs pytest. |
| `build`   | Zips `src/` into `build/app.zip` and uploads it as the artifact `app-paket`.  |
| `deploy`  | Checks that the secret `DEPLOY_TOKEN` is set, without printing it.            |
| `release` | Downloads `app-paket` and creates a GitHub release `v1.0.<run number>` with `app.zip`. |

Each job waits for the job before it (`needs:`). If the tests fail, nothing is built or released.

## Triggers

- `push` on every branch and `pull_request`: `test` and `build` run.
- `deploy` and `release` run only on `main` (`if: github.ref == 'refs/heads/main'`).
  On pull requests and other branches they are skipped.

## Secrets

| Secret         | Where                           | Used by                                    |
| -------------- | ------------------------------- | ------------------------------------------ |
| `DEPLOY_TOKEN` | Environment secret, `production` | `deploy`. Passed through `env:`, never printed. The job fails if it is empty. |
| `GITHUB_TOKEN` | Created by GitHub for each run  | `release`, for `gh release create`. The job gets `contents: write`; all other jobs only `contents: read`. |

## Deployment

`deploy` and `release` use the environment `production`. It has two protection rules:

- **Required reviewer:** the run stops until a reviewer approves it on the run page.
- **Branch rule:** only `main` may deploy to `production`.

After approval, `release` publishes the package as a GitHub release. The release tag is
`v1.0.<run number>`, so every run on `main` makes a new version.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest -v
```

This repo is temporary and will be deleted after the course.
