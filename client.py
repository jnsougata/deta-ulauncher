import json
import subprocess

from typing import List, Dict, Any

def get_canvas_apps() -> List[Dict[str, Any]]:
    out = subprocess.check_output(["space", "api", "-X", "GET", "/v0/canvas?limit=999&per_page=999"])
    return json.loads(out)["items"]

def get_actions() -> List[Dict[str, Any]]:
    out = subprocess.check_output(["space", "api", "-X", "GET", "/v0/actions?limit=999&per_page=999"])
    return json.loads(out)["actions"]