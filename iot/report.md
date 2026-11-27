# IOT

Groupe : Théo Constant; Etienne Kita;

## Partie 1 : Simulateur de traffic en ligne

### 1

Les couleurs des véhicules correspondent à leur vitesse. De rouge, le plus lent, à violet, le plus rapide (le code couleur suit le spectre visible).

Sur les routes, il y a des endroits où l'on peut mesurer les métriques de débit, vitesse et densité.

- Débit : Nombre de véhicule par here
- Vitesse : Vitesse moyenne de voitures en km/h
- Densité : Nombre de véhicule au kilomètre

### 2

Notre critère de congestion est la suivante, on considère qu'en dessous de 30km/h juste avant l'arrivée de la bretelle, il y a une congestion.

Avec 300 secondes de simulation, on trouve qu'en moyenne, les bouchons selon notre critère apparraissent vers 100 secondes, au niveau de la bretelle, et se propage en arrière, dans le sens inverse de la circulation.

### 3

|  | Entrée | Sortie |
|:-|:-|:-| 
| Vitesse (km/h) | 70-80 | 70-80 |
| Débit (veh/km) | 50-60 | 45-50 |

Ce n'est pas une solution d'enlever la bretelle, car elle n'existe plus. Les personnes ne peuvent plus aller sur l'autoroute.

Oui, une file peut être déplacée hors de la zone observé, par exemple, si on permet aux voitures de sortir avec une grande vitesse, il se peut que le bouchon arrive chez le voisin et qu'on reporte le problème sur quelqu'un d'autre.

### 4

critère : > 30km/h
temps d'observation
100 veh/h => pas de bouchon 
200 veh/h => pas de bouchon
300 veh/h => pas de bouchon
400 veh/h => pas de bouchon
500 veh/h => pas de bouchon
600 veh/h => pas de bouchon
700 veh/h => BOUCHONS (à partir de 200 secondes)
650 veh/h => pas de bouchon
680 veh/h => BOUCHONS (des fois)

On remarque qu'entre 650 et 700, il peut avoir des bouchons avec de la malchance, au dessus de 700, il y aura toujours des bouchons.

### 5

Modifier la vitesse maximale ne permet pas efficacement de débloquer un bouchon.

En augmentant l'accélération, il devient difficile de créer un bouchon, et s'il y a déjà un bouchon, avec 2m/s^2, on remarque que le traffic est fluide même s'il reste en dessous de 30km/h. Avec une meilleur accélération, il y a toujours des bouchons, mais il n'y a presque plus de file d'attente sur la bretelle.

Avec le time gap, quand on le met trop bas, les véhicules à l'entrée se rentre dedans et se stack entre eux. Ce n'est pas très réaliste, dans la vraie vie, ce serait plus un accident.
