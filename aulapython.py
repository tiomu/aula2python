#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Desenvolvido por Tio Mu
# Email: contatotiomuca@gmail.com
# Site: https://linktr.ee/tiomu
#
# Copyright (C) 2021 Tio Mu
#
# License:
#
#    This package is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; version 2 dated June, 1991.
#
#    This package is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this package; if not, write to the Free Software
#    Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA
#    02111-1307, USA.
#
# On Debian GNU/Linux systems, the complete text of the GNU General
# Public License can be found in `/usr/share/common-licenses/GPL'.

import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk, Gdk

GLADE_FILE = "aulapython.glade"
CSS_FILE = "aulapython.css"

CAIXADEMENSAGEM_FILE = "caixademensagem.glade"

class aulapython:
    def __init__(self):
        screen = Gdk.Screen.get_default()
        provider = Gtk.CssProvider()
        provider.load_from_path(CSS_FILE)
        Gtk.StyleContext.add_provider_for_screen(screen, provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
        
        self.builder = Gtk.Builder()
        self.builder.add_from_file(GLADE_FILE)
        self.builder.connect_signals(self)
        
        self.window = self.builder.get_object("FMain")
        self.window_label = self.builder.get_object("window_label")
        
        self.window.show_all()
        
    def on_window_destroy(self, window):
        Gtk.main_quit()
        
    def LoadMessageDialog(self):
        self.Mensagem1 = Gtk.Builder()
        self.Mensagem1.add_from_file(CAIXADEMENSAGEM_FILE)
        self.Mensagem1.connect_signals(self)
        
    def Botao1_clicked(self, button):
        self.LoadMessageDialog()
        
        self.Info1 = self.Mensagem1.get_object("FMensagem")
        self.Info1.set_property("text", "Está é uma mensagem de teste!")
        self.Info1.show()
        
    def btnFecharMensagem_clicked(self, button):
        self.Info1.destroy()

def main():
    app = aulapython()
    Gtk.main()
    
if __name__ == "__main__":
    main()
