#include "Tictactoe.hpp"

Jeu::Jeu() {
    raz();
}

void Jeu::raz() {
    /*_plateau = {
        {JOUEUR_VIDE,JOUEUR_VIDE,JOUEUR_VIDE},
        {JOUEUR_VIDE,JOUEUR_VIDE,JOUEUR_VIDE},
        {JOUEUR_VIDE,JOUEUR_VIDE,JOUEUR_VIDE}
    }
    }*/
    // TODO
}

std::ostream & operator<<(std::ostream & os, const Jeu & jeu) {
    // TODO
    return os;
}

Joueur Jeu::getVainqueur() const {
    // TODO
    return JOUEUR_VIDE;
}

Joueur Jeu::getJoueurCourant() const {
    // TODO
    return JOUEUR_VIDE;
}

bool Jeu::jouer(int i, int j) {
    // TODO     
    return false;
}

