{ pkgs ? import <nixpkgs> {} }:

with pkgs.python3Packages;

buildPythonPackage {
  name = "pytictactoe";
  src = ./.;
  propagatedBuildInputs = [
    ((pkgs.pybind11.override { python = pkgs.python3; }).overrideDerivation (attrs: { doCheck = false; }))
    pkgs.gnome3.gtk
    pkgs.gobjectIntrospection
    pygobject3
  ];
}

