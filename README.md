# TIPE-feu-de-forets

Ce projet est surement celui le plus développé de mes projets du fait que j'ai eu 2 ans pour
le développer pendant la prépa.
J'ai d'abord développé différents modèles progressivement compliqués à chaque itération. J'ai
ensuite choisi un modèle probabiliste que j'ai amélioré à l'aide de la méthode de descente de
gradient. 
Du fait de l'utilisation d'un modèle probabiliste, il a fallut moyenner les résultats pour éviter
des écarts types trop important. Ceci a posé des problèmes d'efficacité en python. Je l'ai réglé
en programmant la descente de gradient en C++. J'ai pu à l'occasion apprendre ce langage.
De plus pour réduire la complexité il a fallut actualiser uniquement les cases "menacées" par
le feu.
