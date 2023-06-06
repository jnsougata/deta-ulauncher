from typing import List, Dict, Any

def filter_apps(apps) -> List[Dict[str, Any]]:
    return [app for app in apps if app["item_type"] == "instance"]