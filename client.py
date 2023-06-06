import json
import subprocess

def get_canvas_apps():
    out = subprocess.check_output(["space", "api", "-X", "GET", "/v0/canvas?limit=999&per_page=999"])
    return json.loads(out)
