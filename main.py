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

from client import get_actions

logger = logging.getLogger(__name__)


class DetaLauncher(Extension):

    def __init__(self):
        super(DetaLauncher, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        actions = get_actions()
        results = []
        name_arg = event.get_argument()
        if not name_arg:
            logger.info('preferences %s' % json.dumps(extension.preferences))
            for action in actions:
                results.append(
                    ExtensionResultItem(
                        icon='images/action.png',
                        name=action['title'],
                        description=f'{action["app_name"]}',
                        on_enter=ExtensionCustomAction(action, keep_app_open=True)
                    )
                )
        else:
            for action in actions:
                if name_arg.lower() in action['app_name'].lower():
                    results.append(
                        ExtensionResultItem(
                            icon='images/action.png',
                            name=action['title'],
                            description=f'{action["app_name"]}',
                            on_enter=ExtensionCustomAction(action, keep_app_open=True)
                        )
                    )
        
        return RenderResultListAction(results)



class ItemEnterEventListener(EventListener):

    def on_event(self, event, extension):
        data = event.get_data()
        results = []
        for inp in data['input']:
            results.append(
                ExtensionResultItem(
                    icon='images/action.png',
                    name=inp['name'],
                    description=inp['type'],
                    on_enter=ExtensionCustomAction(inp, keep_app_open=True)
                )
            )
        return RenderResultListAction(results)


if __name__ == '__main__':
    DetaLauncher().run()
