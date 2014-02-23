CPS-rename
==========

Présentation du contexte
------------------------

France 3 a eu la bonne idée de mettre à disposition une très grande quantité d'épisodes de [*C'est pas sorcier*](http://fr.wikipedia.org/wiki/C'est_pas_sorcier) sur YouTube : http://www.youtube.com/user/cestpassorcierftv. À l'heure où j'écris ces lignes, il y a environ 350 vidéos uploadées sur 560 épisodes au total (d'après Wikipédia).

J'ai voulu télécharger toutes les vidéos, en utilisant [youtube-dl](https://github.com/rg3/youtube-dl) qui permet de télécharger toutes les vidéos d'une chaîne. youtube-dl permet de formater le nom des fichiers en sortie, mais ayant oublié la commande exacte qui donne le résultat souhaité, je me suis décidé à télécharger normalement avec le script download.sh (qui évite de relancer manuellement la commande lors d'une erreur de connexion).

Les fichiers obtenus ont un nom de cette forme :

    C'est pas sorcier - LE TITRE de la Vidéo -I8e_8DT9.mp4

Le but est d'obtenir :

    le titre de la vidéo.mp4

Il peut ou non y avoir des espaces autour des tirets et la casse n'est pas garantie. L'extension peut varier. Dans certains cas, le bout de chaîne qui doit représenter un id contient un trait d'union et le nouveau fichier aura donc un mauvais nom. On signale donc à l'utilisateur qu'un nom de fichier contenant encore un trait d'union après le renommage est à vérifier, et éventuellement à corriger manuellement (ce qui devrait être rare).

Il était hors de question de le faire manuellement, d'où le script cps-rename.py.

Utilisation du script
---------------------

On peut accéder à l'aide en exécutant simplement le script sans paramètres :

    ./cps-rename.py
    Utilisation : cps-rename.py dossier fichier_exclus_1 fichier_exclus_2 ...

Le premier paramètre est le dossier où se trouvent les vidéos. Les suivant sont les fichiers s'y trouvant qu'on ne veut pas renommer.

Le script est conçu de telle sorte que le nom de fichier « utile » est compris entre le tout premier tiret et le tout dernier. Ça correspond à la très large majorité des vidéos, bien que quelques unes possèdent un trait d'union dans l'id aléatoire juste avant l'extension. Le script vous prévient donc des fichiers dont le nom contient encore un tiret. L'inconvénient, c'est que beaucoup de vidéos ont un nom avec un tiret, mais pas dans l'id. Il faudra donc vérifier et faire les modifications manuellement. Dans tous les cas, c'est bien plus rapide ainsi que de devoir tout renommer à la main !

Licence d'utilisation
---------------------

                   LICENCE PUBLIQUE RIEN À BRANLER
                         Version 1, Mars 2009
    
    Copyright (C) 2014 Thomas Duchesne
    
    La copie et la distribution de copies exactes de cette licence sont
    autorisées, et toute modification est permise à condition de changer
    le nom de la licence. 
    
            CONDITIONS DE COPIE, DISTRIBUTON ET MODIFICATION
                  DE LA LICENCE PUBLIQUE RIEN À BRANLER
    
     0. Faites ce que vous voulez, j’en ai RIEN À BRANLER.