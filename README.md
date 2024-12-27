# #Author  : Hackfut
#Contact : t.me/H4ckfutSec
#License : MIT
#[Warning] I am not responsible for the way you will use this program [Warning]

#██╗░░██╗░█████╗░░█████╗░██╗░░██╗███████╗██╗░░░██╗████████╗
#██║░░██║██╔══██╗██╔══██╗██║░██╔╝██╔════╝██║░░░██║╚══██╔══╝
#███████║███████║██║░░╚═╝█████═╝░█████╗░░██║░░░██║░░░██║░░░
#██╔══██║██╔══██║██║░░██╗██╔═██╗░██╔══╝░░██║░░░██║░░░██║░░░
#██║░░██║██║░░██║╚█████╔╝██║░╚██╗██║░░░░░╚██████╔╝░░░██║░░░
#╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░░░░░╚═════╝░░░░╚═╝░░░

# ProxGrab

ProxGrab est un outil permettant de récupérer des proxies publics de type HTTP, SOCKS4 et SOCKS5 à partir d'une API, de vérifier leur validité, et de les sauvegarder dans un fichier pour une utilisation ultérieure. Ce projet est conçu pour être utilisé principalement par les chercheurs en sécurité et les professionnels de l'anonymat en ligne.

## Fonctionnalités

- **Récupération de proxies** : Téléchargez des proxies publics de différents types (HTTP, SOCKS4, SOCKS5).
- **Vérification de la validité** : Vérifiez si les proxies sont accessibles avant de les enregistrer.
- **Informations sur les IP** : Obtenez des informations géographiques (pays, ville) associées à chaque proxy.
- **Enregistrement des proxies valides** : Sauvegardez les proxies valides dans un fichier texte avec un nom unique si nécessaire.
- **Interface utilisateur** : Interface en ligne de commande simple avec des options de sélection pour le type de proxy et le pays.

## Installation

### Prérequis

1. **Python 3.6+** : Le script est écrit en Python et nécessite Python version 3.6 ou supérieure.
2. **Bibliothèques Python** : Installez les bibliothèques nécessaires via pip :

```bash
pip install requests prettytable
```

### Cloner le dépôt

Clonez ce dépôt GitHub sur votre machine locale :

```bash
git clone https://github.com/HackfutSec/ProxGrab.git
cd ProxGrab
```

## Utilisation

1. **Exécution du script** : Une fois le dépôt cloné et les dépendances installées, vous pouvez exécuter le script en lançant la commande suivante :

```bash
python proxgrab.py
```

2. **Sélection du type de proxy** : L'outil vous demandera de choisir le type de proxy que vous souhaitez récupérer :
    - **1 - HTTP**
    - **2 - SOCKS4**
    - **3 - SOCKS5**

3. **Sélection du pays** : Ensuite, vous devrez choisir un code pays (par exemple, "1" pour les États-Unis, "2" pour le Canada, etc.).

4. **Sélection du nombre de proxies** : L'outil vous demandera combien de proxies vous souhaitez récupérer. Vous pouvez spécifier un nombre précis.

5. **Sauvegarde des proxies valides** : Une fois les proxies récupérés et validés, ils seront sauvegardés dans un fichier texte. Si le fichier existe déjà, un suffixe numérique sera ajouté pour créer un nom unique.

## Exemple d'exécution

Voici un exemple de sortie possible :

```
[!] Select the type of proxy you want:

1 - HTTP
2 - SOCKS4
3 - SOCKS5
4 - Quit

[!] Enter your choice (1-4): 1

[!] Select the country code for proxies:

1 - US
2 - CA
3 - GB
...

[!] Enter your country choice (1-32): 1

[!] How many proxies do you want to grab: 10

[!] Grabbers: 10 HTTP proxies from US...
Fetching proxies...
[!] Proxies Table:
+-------------+-------+---------+---------+--------------+---------------------+
| IP          | Port  | Country | City    | Status       | Fetch Time (s)      |
+-------------+-------+---------+---------+--------------+---------------------+
| 192.168.1.1 | 8080  | US      | New York| Reachable    | 1.23                |
| 192.168.2.1 | 1080  | US      | Los Angeles| Not Reachable| 1.23               |
+-------------+-------+---------+---------+--------------+---------------------+

[!] Hostnames Table:
+-------------+-------------+-------+--------------+
| IP          | Hostname    | Port  | Status       |
+-------------+-------------+-------+--------------+
| 192.168.1.1 | proxy1.com  | 8080  | Reachable    |
| 192.168.2.1 | Unknown     | 1080  | Not Reachable|
+-------------+-------------+-------+--------------+

[!] Valid proxies saved in HTTP_US_Proxy.txt
```

## Avertissement

**[Warning]** L'utilisation de cet outil pour des activités malveillantes ou illégales est strictement interdite. L'auteur de ce projet ne sera pas tenu responsable de l'utilisation abusive de cet outil.

## License

Ce projet est sous la licence **MIT**.
