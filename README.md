# PDI_pluginQGIS
Projet de Développement Informatique 11
## Preview
Le plugin QGIS RVA a pour objectif de placer des itinéraires routiers de manière semi-automatique à côté d'une route. L'utilisateur pourra alors réorganiser l'ordre de ceux-ci à l'aide d'un clic continu.
## Tutoriel d'installation
* Il faut télécharger le plugin dans QGIS. Pour ce faire, il faut extraire le dossier rva.zip (dans le dossier présentation) via Extensions > Installer depuis un ZIP.
## Tutoriel d'utilisation
* Pour le lancer, il faut cliquer sur la petite icône en forme de prise électrique ; le plugin s'affichera.
* Il faudra rentrer une couche de tronçons de route à l'emplacement Couche Route (couches > Troncons_route) et de même pour la couche des itinéraires (couches > itinéraires.shp).
! Contraintes techniques sur ces couches ! : il faut que ces couches soient vectorielles et possèdent une même géométrie. La couche de Tronçons de routes doit être découpée en tronçons.
* On appuie alors sur OK.
* Les itinéraires apparaissent alors sans symbologie. Pour la faire apparaître, il faut importer 3 scripts Python (Script_post_plugin > les 3 sont là) en ouvrant la console Python de QGIS et les exécuter dans l'ordre de votre choix.
Pour que l'affichage se fasse, il suffit de faire une action telle qu'un zoom ou un simple mouvement sur la carte. Les Itinéraires avec symbologie devront alors apparaître.
* Pour ce qui concerne le déplacement, il suffit alors de placer la petite croix (souris) sur le premier itinéraire, d'effectuer un clic gauche, DE LE MAINTENIR, jusqu'au second itinéraire et de le relâcher. Les itinéraires s'inverseront ! N'hésitez pas à zoomer afin de bien sélectionner les objets que l'on veut échanger.
** Remarque : Si l'on change d'outil avant de déplacer les itinéraires tels , il est possible de réactiver le plugin en cliquant sur l'icône invisible à droite du bouton plugin (logo avec la prise électrique), si l'on veut de nouveau déplacer les itinéraires.
