import json
import logging
from time import sleep
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction

from client import get_canvas_apps

logger = logging.getLogger(__name__)


class DetaLauncher(Extension):

    def __init__(self):
        super(DetaLauncher, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        items = []
        logger.info('preferences %s' % json.dumps(extension.preferences))
        apps = get_canvas_apps()
        for app in apps:
            items.append(
                ExtensionResultItem(
                    icon='images/icon.png',
                    name=app['id'],
                    description="Open app in browser",
                    on_enter=ExtensionCustomAction(app, keep_app_open=True)
                )
            )
        return RenderResultListAction(items)


class ItemEnterEventListener(EventListener):

    def on_event(self, event, extension):
        data = event.get_data()
        return RenderResultListAction(
            [
                ExtensionResultItem(
                    icon='images/icon.png',
                    name=f"{data}",
                    on_enter=HideWindowAction()
                )
            ]
        )


if __name__ == '__main__':
    DetaLauncher().run()
