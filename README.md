# PDI_pluginQGIS
Projet de Développement Informatique 11

Dans un premier temps il faut télécharger le plugin dans QGIS, pour ce faire, il faut extraire le dossier rva.zip (dans le dossier présentation) via la  Extensions puis Installer depuis un ZIP. "\n"
Ensuite pour le lancer, il faut cliquer sur la petite icon en forme de prise éléctrique, la plugin s'affichera. 
Il faudra rentrer une couche de tronçons de route a l'emplacement Couche Route (couches > Troncons_route)
Et de même pour la couche itinéraires (couches > itinéraires.shp)
On appui alors sur OK.
Les itinéraires apparaissent alors sans symbologie. Pour la faire apparaitre il faut importer 3 scripts python (Script_post_plugin > les 3 sont là) en ouvrant la console Python de QGIS et les executer dans l'ordre de votre choix. 
Pour que l'affichage se fasse il suffit de faire une action telle qu'un zoom ou un simple mouvement sur la carte. Les Itinéraires avec symbologie devront alors apparaitre.
Pour ce qui est du déplacement, il suffit alors de placer la petite croix (souris) sur le premier itinéraires, d'effectuer un clic gauche, DE LE MAINTENIR, jusqu'au second itinéraires et de le relâcher. Les itinéraires s'inverseront! N'hésitez pas a zoomer afin de bien sélectionner l'objet.
Si l'on change d'outils, il est possible de re-activer le plugin en cliquant sur l'icône invisible à la droite du bouton plugin (logo avec la prise electrique), si l'on re-veut déplacer les itinéraires.
