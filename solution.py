# Modifiez ce fichier si votre solution est en Python.
# Ce programme est un court exemple du protocol texte et d'une réponse au
# premier challenge "Ping".
# Modifiez "run.sh" pour exécuter ce programme python et
# exécutez la suite de test avec la commande "./runner ./run.sh"
#
# Pour l'exemple en java regardez "solution.java". Pour d'autre langage,
# faites un programme qui lit et écrit par les entrées et sorties standard
# et modifier "run.sh" pour compiler et exécuter votre programme.
#
# N'OUBLIER PAS DE "FLUSHER" VOS SORTIES!

import sys
print('T')
sys.stdout.flush()
mid, _, msg = sys.stdin.readline().split(':')
print(':'.join([mid, msg]))
sys.stdout.flush()

