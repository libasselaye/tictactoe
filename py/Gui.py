import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

import Tictactoe

def joueurVersTexte(joueur):
    if joueur == Tictactoe.Joueur.VIDE:
        return "vide"
    elif joueur == Tictactoe.Joueur.ROUGE:
        return "rouge"
    elif joueur == Tictactoe.Joueur.VERT:
        return "vert"
    elif joueur == Tictactoe.Joueur.EGALITE:
        return "égalité"
    else:
        return "inconnu"

def joueurVersCouleur(joueur):
    if joueur == Tictactoe.Joueur.ROUGE:
        return (255, 0, 0)
    elif joueur == Tictactoe.Joueur.VERT:
        return (0, 255, 0)
    else:
        return (255, 255, 255)

class Gui(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, default_width=400, default_height=400, title="Tictactoe")

        self.jeu = Tictactoe.Jeu()

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        self.drawingarea = Gtk.DrawingArea()
        self.drawingarea.connect('draw', self.draw)
        self.drawingarea.set_events(Gdk.EventMask.BUTTON_PRESS_MASK)
        box.pack_start(self.drawingarea, True, True, 0)

        # ...

        bouton = Gtk.Button(label="Recommencer")
        bouton.connect("clicked", self.gererBouton)
        box.pack_start(bouton, False, True, 0)

        self.add(box)
        self.connect("destroy", Gtk.main_quit)
        self.show_all()

        self.razGui()

    def gererBouton(self, widget):
        self.razGui()

    def razGui(self):
        print("TODO")

    def run(self):
        Gtk.main()

    def draw(self, da, ctx):
        win = self.drawingarea.get_window()
        width = win.get_width()
        height = win.get_height()

        # ...
        ctx.set_source_rgb(0, 0, 0)
        ctx.set_line_width(4)
        ctx.move_to(0, 0)
        ctx.line_to(width, height)
        ctx.move_to(width, 0)
        ctx.line_to(0, height)
        ctx.stroke()

