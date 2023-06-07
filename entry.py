import gi
import threading

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk



class DialogWindow(Gtk.Window):
    def __init__(self, response):
        super().__init__(title=f'Response')
        self.set_size_request(400, 100)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        label = Gtk.Label()
        label.set_text(response)
        label.set_size_request(200, 30)
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
        dialog = DialogWindow("Response")
        dialog.show_all()
        self.destroy()


       
