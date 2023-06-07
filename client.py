import json
import subprocess

from typing import List, Dict, Any

def call_cli(method: str, path: str) -> List[Dict[str, Any]]:
    out = subprocess.check_output(["space", "api", "-X", method, path])
    return json.loads(out)

def get_canvas_apps() -> List[Dict[str, Any]]:
    return call_cli("GET", "/v0/canvas?limit=999&per_page=999")["items"]
    return json.loads(out)

def get_actions() -> List[Dict[str, Any]]:
    return call_cli("GET", "/v0/actions?limit=999&per_page=999")["actions"]

def post_action(action: Dict[str, Any], data) -> None:
    instance_alias = action["instance_alias"]
    name = action["name"]
    #call_cli("POST", f"/v0/actions/{instance_id}/{name}", json.dumps(data))
    body = "'{}'".format(json.dumps(data))
    command = "echo {} | space trigger {} {}".format(body, instance_alias, name)
    out = subprocess.check_output(["bash","-c", command])
    return out.decode("utf-8")