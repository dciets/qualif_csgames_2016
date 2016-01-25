# Qualification CS Games 2016

## DCIETS

L’objectif de l’épreuve de qualification de la DCI pour les CS Games 2016 sera de concevoir et développer un programme communiquant avec un gestionnaire de mission et remplir les missions assignées par celui-ci. Ainsi, votre logiciel devra pouvoir résoudre une série de missions différente afin de maximiser votre score et faire partie de la prochaine délégation de l’ÉTS!

# Communication

Afin de recevoir et répondre aux missions, votre logiciel devra être en mesure d’implémenter un protocole très simple. La communication de votre programme avec le gestionnaire de mission se fera via les entrées et sorties standard (stdin et stdout).

Ainsi, les requêtes de mission sont reçues en lisant une ligne de l’entrée standard de votre programme (par exemple, en Java vous pourriez utiliser BufferedReader.readLine). Chaque requête est composée d’un identifiant représentant le type de mission et les paramètres de ladite mission. Les types de missions possibles sont présentés plus loin. Les paramètres de mission seront toujours encodés en ASCII et leur format est spécifique à chaque type de mission. Le type de mission et ses paramètres sont séparés par deux points (`:`).

Ainsi, une requête de mission de type Ping avec le paramètre "Pong" serait reçue sous la forme:

```
1:Pong
```

La réponse est simplement envoyée en écrivant une ligne dans la sortie standard de votre programme. Ainsi, la réponse à la requête précédente serait:

```
Pong
```

# Outil de test

Un logiciel est fourni afin d’exécuter votre application et d’évaluer ses performances en la testant à un petit ensemble de données. Pour tester votre application, éditer "run.sh" en ajoutant les lignes de commande nécessaires pour exécuter votre application. Par la suite, exécutez les tests avec `./runner ./run.sh`. Vous pouvez aussi utiliser le paramètre `-i 3` pour exécuter seulement la suite de tests de la mission 3.

Dans le cas où votre soumission ne supporte pas une mission, veuillez répondre à la mission avec une ligne vide.

Trois fichiers d’exemples sont fournis (`run.sh`, `solution.py` et `solution.java`). Ceux-ci offrent un exemple très simple pour répondre à une requête de type Ping en Python et Java. Libre à vous de vous en inspirer pour développer votre solution dans un autre langage!

### Note

* Les données textes sont encodées en ASCII.

* Vous pouvez écrire des messages dans "stderr" afin de les voir affichés dans la sortie de l’outil de test.

* **Il est possible que les sorties de votre programme soient mises en tampon. Assurez-vous d’appeler "flush" sur la sortie standard après l'envoi de chaque message. Vous pouvez aussi désactiver la mise en tampons de stdout (“setbuf(stdout, NULL);” en C/C++).**

# Missions

## Mission 1 - Ping (2 Pts)

La mission est simplement de renvoyer une réponse avec la chaîne de caractère donnée en paramètre.

### Exemple

<table>
  <tr>
    <td>**#**</td>
    <td>**Paramètre de Requête**</td>
    <td>**Réponse**</td>
  </tr>
  <tr>
    <td>1</td>
    <td>ping</td>
    <td>ping</td>
  </tr>
  <tr>
    <td>2</td>
    <td>foobar</td>
    <td>foobar</td>
  </tr>
</table>


## Mission 2 - Palindrome (3 Pts)

La mission est d’envoyer "true" si la chaîne donnée en paramètre est un palindrome ou “false” dans le cas contraire.

### Exemple

<table>
  <tr>
    <td>**#**</td>
    <td>**Paramètre de Requête**</td>
    <td>**Réponse**</td>
  </tr>
  <tr>
    <td>1</td>
    <td>foobar</td>
    <td>false</td>
  </tr>
  <tr>
    <td>2</td>
    <td>barrab</td>
    <td>true</td>
  </tr>
  <tr>
    <td>3</td>
    <td>xyzazyx</td>
    <td>true</td>
  </tr>
</table>


## Mission 3 - Trie (3 Pts)

La mission est de trier en ordre croissant la liste de nombres séparés par des virgules.

### Exemple

<table>
  <tr>
    <td>**#**</td>
    <td>**Paramètre de Requête**</td>
    <td>**Réponse**</td>
  </tr>
  <tr>
    <td>1</td>
    <td>6,5,4,3,2,1</td>
    <td>1,2,3,4,5,6</td>
  </tr>
  <tr>
    <td>2</td>
    <td>6345, 234, 945</td>
    <td>234,945,6345</td>
  </tr>
</table>


## Mission 4 - Compter (3 Pts)

La mission est de compter le nombre d’éléments distincts passés en paramètre séparé par des espaces. La réponse doit être sous la forme <Élément>;<Nombre> avec chaque élément séparé par des espaces, en ordre alphabétique.

### Exemple

<table>
  <tr>
    <td>**#**</td>
    <td>**Paramètre de Requête**</td>
    <td>**Réponse**</td>
  </tr>
  <tr>
    <td>1</td>
    <td>c b a</td>
    <td>a;1 b;1 c;1</td>
  </tr>
  <tr>
    <td>2</td>
    <td>aa a aa aa bb</td>
    <td>a;1 aa;3 bb;1</td>
  </tr>
</table>


## Mission 5 - Recherche de texte (4 Pts)

La mission est d’envoyer le nombre d’instances d’une chaîne de caractères X dans le texte Y. Les deux paramètres sont séparés par un point virgule (;): <X>;<Y>

### Exemple

<table>
  <tr>
    <td>**#**</td>
    <td>**Paramètre de Requête**</td>
    <td>**Réponse**</td>
  </tr>
  <tr>
    <td>1</td>
    <td>a;aabbccdda</td>
    <td>3</td>
  </tr>
  <tr>
    <td>2</td>
    <td>aba;foobababa</td>
    <td>2</td>
  </tr>
  <tr>
    <td>3</td>
    <td>foo;aabbcc</td>
    <td>0</td>
  </tr>
</table>


## Mission 6 - Mathématique (4 Pts)

La mission contient une expression mathématique et vous devez renvoyer la réponse sous forme d’un nombre décimal avec une précision arrondie de deux chiffres après la virgule.

Opérations supportées: (),-,+,\*,/,^,sin,cos,tan,e

### Exemple

<table>
  <tr>
    <td>**#**</td>
    <td>**Paramètre de Requête**</td>
    <td>**Réponse**</td>
  </tr>
  <tr>
    <td>1</td>
    <td>1+4*(3-5)/7</td>
    <td>-0.14</td>
  </tr>
  <tr>
    <td>2</td>
    <td>2^4</td>
    <td>16</td>
  </tr>
  <tr>
    <td>3</td>
    <td>cos(1)+e</td>
    <td>3.26</td>
  </tr>
</table>


## Mission 7 - Mathématique II (10 Pts)

Tout comme la mission 6, cette mission consiste à résoudre une expression mathématique. Par contre, cette mission inverse l’ordre de priorité des opérations. Ainsi, les additions et soustractions doivent être effectuées avant les multiplications et divisions.

Opérations supportées: -,+,\* et /.

### Exemple

<table>
  <tr>
    <td>**#**</td>
    <td>**Paramètre de Requête**</td>
    <td>**Réponse**</td>
  </tr>
  <tr>
    <td>1</td>
    <td>3+4*2</td>
    <td>14</td>
  </tr>
  <tr>
    <td>2</td>
    <td>12/4-2</td>
    <td>6</td>
  </tr>
</table>


## Mission 8 - Parsing (8 Pts)

La mission est de retrouver une valeur précise dans un arbre de propriété N-aire sous un format maison. Le premier paramètre est le chemin à parcourir de la feuille à trouver. Le chemin est représenté sous forme de clés séparé par des points ("."). Un point virgule (“;”) sépare le chemin des données de l’arbre. Les données de l’arbre sont représentées sous forme de liste de valeurs entre parenthèses séparées par des virgules. Le premier élément de la liste est la clé du noeud et le reste est ses enfants. Si un noeud a un seul enfant, celui-ci est considéré comme une feuille de l’arbre. Par exemple, l’élément “(a, 1)” représente le noeud “a” avec la valeur “1”. Dans le cas où le chemin ne se rend pas à une feuille de l’arbre, la réponse doit être “-1”.

Le format de l’arbre est défini par la grammaire suivante:

```
Arbre := ( Noeud )
Noeud := ( Elements )
Elements: Clé, Liste | Clé, Feuille
Liste := Noeud | Noeud, Liste
Clé := [a-zA-Z0-9]
Feuille := [a-zA-Z0-9]
```

### Exemple

<table>
  <tr>
    <td>**#**</td>
    <td>**Paramètre de Requête**</td>
    <td>**Réponse**</td>
  </tr>
  <tr>
    <td>1</td>
    <td>a.b;(a, (a, 1), (b, 42), (c, 13))
Représente l’arbre:
```
   |
   a
  /|\
 a b c
 | |  \
 1 42 13
```
</td>
    <td>42</td>
  </tr>
  <tr>
    <td>2</td>
    <td>a.b.c;(a, (b,1), (c,2))</td>
    <td>-1</td>
  </tr>
  <tr>
    <td>2</td>
    <td>a.b;(a, (b, (c,2)))</td>
    <td>-1</td>
  </tr>
  <tr>
    <td>3</td>
    <td>foo.bar;(foo, (bar, 7),(biz, (a, 1), (b, 2)))
Représente l’arbre:
```
    / \
 foo   biz
  |     | \
 bar    a b
  |     | |
  7     1 2
```
</td>
    <td>7</td>
  </tr>
</table>


## Mission 9 - ASCII Art (10 Pts)

Cette mission consiste à traduire sous forme texte un nombre représenté sous forme de dessin ASCII. Les glyphes utilisés sont prédéfinis et alignés verticalement. Par contre, il est possible que des espaces soient insérés entre les lettres. Les sauts de ligne du dessin ASCII sont remplacés par des points-virgules (`;`). Les glyphes utilisés sont les suivants:

<table>
  <tr>
    <td>**1**</td>
    <td>**2**</td>
    <td>**3**</td>
    <td>**4**</td>
    <td>**5**</td>
  </tr>
  <tr>
    <td>
```
##
 #
 #
###
```
</td>
    <td>
```
 ##
#  #
  #
####
```
</td>
    <td>
```
###
  ##
####
###
```
</td>
    <td>
```
# #
# #
###
  #
```
</td>
    <td>
```
###
##
  #
###
```
</td>
  </tr>
  <tr>
    <td>**6**</td>
    <td>**7**</td>
    <td>**8**</td>
    <td>**9**</td>
    <td>**0**</td>
  </tr>
  <tr>
    <td>
```
 ##
#
###
###
```
</td>
    <td>
```
###
 #
#
#
```
</td>
    <td>
```
###
# #
###
###
```
</td>
    <td>
```
###
###
  #
##
```
</td>
    <td>
```
###
# #
# #
###
```
</td>
  </tr>
</table>


### Exemple

<table>
  <tr>
    <td>**#**</td>
    <td>**Paramètre de Requête**</td>
    <td>**Réponse**</td>
  </tr>
  <tr>
    <td>1</td>
    <td>
```
##   ##  ### ;
 #  #  #   ##;
 #    #  ####;
### #### ### ;
```
(Les sauts de ligne sont ajoutés pour la présentation seulement)</td>
    <td>123</td>
  </tr>
  <tr>
    <td>2</td>
    <td>
```
# #     ###;
# #      # ;
###     #  ;
  #     #  ;
```
(Les sauts de ligne sont ajoutés pour la présentation seulement)</td>
    <td>47</td>
  </tr>
</table>


## Mission 10 - Mathematique III (10 Pts)

Cette mission est similaire à Mathematique I, par contre cette fois il vous est demandé de trouver la valeur de "x" dans une expression d’égalité algébrique. La réponse doit être sous forme d’un nombre décimal avec une précision arrondie de deux chiffres après la virgule.

Opérations supportées: -,+,\*,/,^

### Exemple

<table>
  <tr>
    <td>**#**</td>
    <td>**Paramètre de Requête**</td>
    <td>**Réponse**</td>
  </tr>
  <tr>
    <td>1</td>
    <td>x=10+1</td>
    <td>11</td>
  </tr>
  <tr>
    <td>2</td>
    <td>1 + x * 1000 = 126 - 2</td>
    <td>0.12</td>
  </tr>
  <tr>
    <td>3</td>
    <td>2 ^ x = 8</td>
    <td>3</td>
  </tr>
</table>


## Mission 11 - Labyrinthe (10 Pts)

La mission est de trouver un chemin pour compléter le labyrinthe reçu en paramètre. Des points additionnels sont donnés si la solution donnée est le chemin le plus rapide. Le labyrinthe est représenté sous la forme:

```
###e#;
#...#;
#s###
```

où ‘e’ est le départ, ‘s’ la sortie, ‘#’ un mur, ‘ ‘ un passage libre et ‘;’ le délimiteur de ligne. Les sauts de ligne sont ajoutés pour la présentation seulement.

La réponse est envoyée sous le format de caractère séparé par des espaces indiquant les directions à prendre à partir du début avec ‘U’, pour haut, ‘R’ pour droite, ‘D’ pour bas et ‘L’ pour gauche.

### Exemple

<table>
  <tr>
    <td>**#**</td>
    <td>**Paramètre de Requête**</td>
    <td>**Réponse**</td>
  </tr>
  <tr>
    <td>1</td>
    <td>
```
###e#;
# # #;
#   #;
#s###
```
(Les sauts de ligne sont ajoutés pour la présentation seulement)</td>
    <td>D D L L D</td>
  </tr>
</table>


## Mission 12 - Labyrinthe II (13 Pts)

Cette mission est similaire à la **mission 11 - Labyrinthe**. Par contre, le format du labyrinthe envoyé en paramètre est isométrique. Les directions possibles sont ‘UR’ pour la diagonale haut-droite, ‘DR’ pour la diagonale bas-droite, ‘DL‘ pour la diagonale bas-gauche et ‘UL’ pour la diagonale haut-droite.

### Exemple

<table>
  <tr>
    <td>**#**</td>
    <td>**Paramètre de Requête**</td>
    <td>**Réponse**</td>
  </tr>
  <tr>
    <td>1</td>
    <td>
```
/\           ;
\e\  /\      ;
 \ \ \s\     ;
  \ \ \ \/\  ;
  / / / /\ \ ;
  \ \/  \/ / ;
   \  /\  /  ;
    \/  \/   ;
```
(Les sauts de ligne sont ajoutés pour la présentation seulement)
Ce labyrinthe peut être visualisé de la façon suivante:
```
 ###
 #e#
 # #
## ###
#  #s#
# ## #
#    ##
### # #
  #   #
  #####
```
</td>
    <td>DR DR DR DL DR DR UR UR UR UL UL</td>
  </tr>
</table>


# Remise

Votre soumission doit être envoyée via une archive compressée avec votre nom comme nom de fichier à [dci+qualif16@aeets.com](mailto:dci+qualif16@aeets.com).

L’archive doit contenir:

* Les sources de votre programme.

* Votre programme compilé s’il y a lieu.

* Le fichier run.sh qui exécute votre programme.

La correction sera effectuée en exécutant la commande `./runner ./run.sh -t correction.json`.

# Pointage

<table>
  <tr>
    <td>Tâche</td>
    <td>Critère</td>
    <td>Point</td>
  </tr>
  <tr>
    <td>Mission 1 - Ping</td>
    <td>Exactitude des réponses</td>
    <td>2</td>
  </tr>
  <tr>
    <td>Mission 2 - Palindrôme</td>
    <td>Exactitude des réponses</td>
    <td>3</td>
  </tr>
  <tr>
    <td>Mission 3 - Trie</td>
    <td>Exactitude des réponses</td>
    <td>3</td>
  </tr>
  <tr>
    <td>Mission 4 - Compter</td>
    <td>Exactitude des réponses</td>
    <td>3</td>
  </tr>
  <tr>
    <td>Mission 5 - Recherche de texte</td>
    <td>Exactitude des réponses</td>
    <td>4</td>
  </tr>
  <tr>
    <td>Mission 6 - Mathématique</td>
    <td>Exactitude des réponses</td>
    <td>4</td>
  </tr>
  <tr>
    <td>Mission 7 - Mathématique II</td>
    <td>Exactitude des réponses</td>
    <td>10</td>
  </tr>
  <tr>
    <td>Mission 8 - Parsing</td>
    <td>Exactitude des réponses</td>
    <td>8</td>
  </tr>
  <tr>
    <td>Mission 9 - ASCII Art</td>
    <td>Exactitude des réponses</td>
    <td>10</td>
  </tr>
  <tr>
    <td>Mission 10 - Mathématique III</td>
    <td>Exactitude des réponses</td>
    <td>10</td>
  </tr>
  <tr>
    <td>Mission 11 - Labyrinthe</td>
    <td>Exactitude des réponses</td>
    <td>6</td>
  </tr>
  <tr>
    <td></td>
    <td>Chemins optimaux</td>
    <td>4</td>
  </tr>
  <tr>
    <td>Mission 12 - Labyrinthe II</td>
    <td>Exactitude des réponses</td>
    <td>10</td>
  </tr>
  <tr>
    <td></td>
    <td>Chemins optimaux</td>
    <td>3</td>
  </tr>
  <tr>
    <td>Total</td>
    <td></td>
    <td>80</td>
  </tr>
</table>


