# Tictactoe

Implémentation C++/JavaScript du jeu de Tictactoe.

- [site en ligne](https://juliendehos.gitlab.io/L3_GL_tictactoe/)

- [page de cours](https://juliendehos.gitlab.io/posts/gl/post70-tp-workflow.html)


## Compilation du projet C++

Projet CMake classique, dans le dossier `cpp`.

## Compilation du projet Python

```
python3 -m virtualenv -p python3 myenv
source myenv/bin/activate
python3 setup.py install
python3 setup.py install

python3 setup.py build
python3 py/main.py
```

## Compilation du projet JavaScript

Rester dans le dossier principal (qui contient ce `README.md`), puis :

```
docker run --rm -v `pwd`:/tmp -p3000:3000 -e USER_ID=`id -u` juliendehos/emscripten make -C js
firefox js/index.html
```

