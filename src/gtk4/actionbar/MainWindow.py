# -*- coding: utf-8 -*-
"""Python e GTK 4: Gtk.ActionBar()."""

import gi

gi.require_version(namespace='Gtk', version='4.0')

from gi.repository import Gio, Gtk


class MainWindow(Gtk.ApplicationWindow):
    # Lista com o nome dos ícones.
    icons = ['call-start-symbolic', 'call-stop-symbolic',
             'contact-new-symbolic', 'address-book-new-symbolic']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Python e GTK 4: Gtk.ActionBar()')
        # Tamanho inicial da janela.
        self.set_default_size(width=1366 / 2, height=768 / 2)
        # Tamanho minimo da janela.
        self.set_size_request(width=1366 / 2, height=768 / 2)

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        vbox.set_margin_bottom(12)
        vbox.set_margin_end(12)
        vbox.set_margin_start(12)
        vbox.set_margin_top(12)
        vbox.set_valign(Gtk.Align.END)
        self.set_child(child=vbox)

        actionbar = Gtk.ActionBar.new()
        vbox.append(child=actionbar)

        # Loop de repetição para ler a lista com o nome dos ícones.
        for icon in self.icons:
            # Criando um botão com ícone dentro.
            button = Gtk.Button.new_from_icon_name(icon_name=icon)
            button.set_margin_end(6)
            actionbar.pack_start(child=button)


class Application(Gtk.Application):

    def __init__(self):
        super().__init__(application_id='br.natorsc.Exemplo',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)

    def do_startup(self):
        Gtk.Application.do_startup(self)

    def do_activate(self):
        win = self.props.active_window
        if not win:
            win = MainWindow(application=self)
        win.present()

    def do_shutdown(self):
        Gtk.Application.do_shutdown(self)


if __name__ == '__main__':
    import sys

    app = Application()
    app.run(sys.argv)