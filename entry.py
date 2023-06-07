import gi
import threading

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from client import run_action

class DialogWindow(Gtk.Window):
    def __init__(self, response):
        super().__init__(title=response['title'])
        self.set_size_request(400, 200)
        self.set_position(Gtk.WindowPosition.CENTER)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        label = Gtk.Label()
        label.set_text(response['message'])
        label.set_max_width_chars(50)
        label.set_justify(Gtk.Justification.LEFT)
        label.set_line_wrap(True)
        vbox.pack_start(label, False, False, 10)
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)
        button = Gtk.Button.new_with_label("Close")
        button.connect("clicked", self.on_close_clicked)
        button.set_size_request(50, 30)
        hbox.pack_end(button, False, False, 5)
        vbox.pack_end(hbox, False, False, 10)
        main_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=20)
        main_box.pack_start(vbox, True, True, 10)
        self.add(main_box)
        self.show_all()
    
    def on_close_clicked(self, button):
        self.destroy()
    



class EntryWindow(Gtk.Window):
    def __init__(self, data):
        super().__init__(title=f'{data["app_name"]} - {data["title"]}')
        self.set_size_request(400, 100)
        self.timeout_id = None
        self.data = data
        self.set_position(Gtk.WindowPosition.CENTER)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        for inp in data['input']:
            name = inp['name']
            inp_type = inp['type']
            name_as_attr = name.replace(' ', '_')
            setattr(self, name_as_attr, Gtk.Entry())
            getattr(self, name_as_attr).set_text(f"{name} <{inp_type}>")
            getattr(self, name_as_attr).set_size_request(200, 30)
            vbox.pack_start(getattr(self, name_as_attr), False, False, 10)
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)
        button = Gtk.Button.new_with_label("Submit")
        button.connect("clicked", self.on_submit_clicked)
        button.set_size_request(50, 30)
        hbox.pack_end(button, False, False, 5)
        vbox.pack_end(hbox, False, False, 10)
        main_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=20)
        main_box.pack_start(vbox, True, True, 10)
        self.add(main_box)
        self.show_all()


    def on_submit_clicked(self, button):
        body = {}
        for inp in self.data['input']:
            name = inp['name']
            name_as_attr = name.replace(' ', '_')
            body[name] = getattr(self, name_as_attr).get_text()
        self.destroy()
        resp = run_action(self.data, body)
        response = {
            'title': f'{self.data["app_name"]} - Response',
            'message': f'{resp}'
        }
        DialogWindow(response)
        threading.Thread(target=Gtk.main).start()