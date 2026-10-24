# notes-api

Tiny API for the 16-lecture DevOps course.

This is **not** a production server. Later lectures will package it with Docker, then run it on a small AWS instance.

You **call** it today. You do not write it.

## Run

```bash
cd lec-02/codebase/notes-api
python notes-api.py
```

Leave that window open. In a second terminal, follow `../api-lab-instructions.txt`.

## Endpoints

| Method | Path | Auth | Meaning |
|---|---|---|---|
| GET | `/health` | No | Is the process up? |
| GET | `/notes` | No | List notes |
| POST | `/notes` | No | Add a note. JSON: `{"text":"..."}` |
| GET | `/notes/secret` | Header `X-API-Key: lecture2-key` | Demo of 200 vs 401 |

## Files

| File | Commit it? |
|---|---|
| `notes-api.py` | Yes |
| `README.md` | Yes |
| `.env` with a real secret | **Never** |
