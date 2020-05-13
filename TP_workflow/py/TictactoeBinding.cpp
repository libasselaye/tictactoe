#include "../cpp/Tictactoe.hpp"

#include <pybind11/pybind11.h>

PYBIND11_PLUGIN(Tictactoe) {
    pybind11::module m("Tictactoe");

    pybind11::enum_<Joueur>(m, "Joueur")
        .value("VIDE", JOUEUR_VIDE)
        .value("ROUGE", JOUEUR_ROUGE)
        .value("VERT", JOUEUR_VERT)
        .value("EGALITE", JOUEUR_EGALITE)
        ;

    pybind11::class_<Jeu>(m, "Jeu")
        .def(pybind11::init<>())
        .def("raz", &Jeu::raz)
        // ...
        ;

    return m.ptr();
}


