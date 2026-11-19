"""Server-side OpenAI configuration and private integration storage."""

import json
import os
from pathlib import Path

import httpx
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent
LOCAL = ROOT / ".local"
RESOURCE = "https://api.openai.com/v1"
load_dotenv(ROOT / ".env")


def load(name):
    p = LOCAL / (name + ".json")
    return json.loads(p.read_text()) if p.exists() else {}


def store(name, data):
    LOCAL.mkdir(mode=0o700, exist_ok=True)
    path = LOCAL / (name + ".json")
    tmp = path.with_suffix(".tmp")
    fd = os.open(str(tmp), os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, "w") as f:
        json.dump(data, f)
    os.replace(tmp, path)


def settings():
    return {
        "provider": "api",
        "model": os.getenv("OPENAI_MODEL", "").strip(),
        "base_url": RESOURCE,
        "api_key": os.getenv("OPENAI_API_KEY", "").strip(),
    }


def public_settings():
    result = settings()
    result["has_key"] = bool(result.pop("api_key"))
    return result


def models():
    key = settings()["api_key"]
    if not key:
        raise ValueError("Set OPENAI_API_KEY in the server .env file and restart.")
    try:
        response = httpx.get(
            RESOURCE + "/models",
            headers={"Authorization": "Bearer " + key},
            timeout=10,
        )
        response.raise_for_status()
        entries = response.json()["data"]
        if not isinstance(entries, list):
            raise ValueError("Invalid model catalog.")
        return [{"id": item["id"], "name": item["id"]} for item in entries]
    except (httpx.HTTPError, ValueError, TypeError, KeyError):
        raise ValueError("OpenAI model access could not be verified. Check your API key and project permissions.") from None


def connection_status():
    configured = bool(settings()["api_key"])
    try:
        models()
    except ValueError as exc:
        return {"api": {"configured": configured, "valid": False, "message": str(exc)}, "ready": False}
    return {"api": {"configured": True, "valid": True, "message": "OpenAI API access verified."}, "ready": True}
