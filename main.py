import random
import string
import secrets
import pyperclip
from colorama import Fore, Style

def afficher_banniere():
    banniere = f"""{Fore.RED}
█████████████████████████████████████
█ 93N3R473UR D3 M07 D3 P4553 8Y 2WX █
█████████████████████████████████████{Style.RESET_ALL}
    """
    print(banniere)

def generer_mot_de_passe(longueur, inclure_lettres=True, inclure_chiffres=True, inclure_speciaux=True,
                         longueur_min_lettres=1, longueur_min_chiffres=1, longueur_min_speciaux=1,
                         exclure_similaires=True):
    caracteres = ""
    
    if inclure_lettres:
        caracteres += string.ascii_letters
    if inclure_chiffres:
        caracteres += string.digits
    if inclure_speciaux:
        caracteres += string.punctuation
    
    if not caracteres:
        print(f"{Fore.RED}Veuillez sélectionner au moins une catégorie de caractères.{Style.RESET_ALL}")
        return None
    
    caracteres_similaires = 'l1Io0O'
    
    mot_de_passe = []
    if inclure_lettres:
        mot_de_passe += [secrets.choice(string.ascii_letters) for _ in range(longueur_min_lettres)]
    if inclure_chiffres:
        mot_de_passe += [secrets.choice(string.digits) for _ in range(longueur_min_chiffres)]
    if inclure_speciaux:
        mot_de_passe += [secrets.choice(string.punctuation) for _ in range(longueur_min_speciaux)]
    
    mot_de_passe += [secrets.choice(caracteres) for _ in range(longueur - len(mot_de_passe))]
    
    random.shuffle(mot_de_passe)
    
    mot_de_passe = ''.join(mot_de_passe)
    
    if exclure_similaires:
        for similaire in caracteres_similaires:
            mot_de_passe = mot_de_passe.replace(similaire, secrets.choice(caracteres))
    
    return mot_de_passe

def demander_longueur():
    while True:
        try:
            longueur = int(input("Entrez la longueur souhaitée pour le mot de passe (au moins 8 caractères) : "))
            if longueur < 8:
                print(f"{Fore.RED}La longueur minimale recommandée est de 8 caractères.{Style.RESET_ALL}")
            else:
                return longueur
        except ValueError:
            print(f"{Fore.RED}Veuillez entrer un nombre entier valide.{Style.RESET_ALL}")

def demander_criteres():
    inclure_lettres = input(f"{Fore.YELLOW}Voulez-vous inclure des lettres majuscules et minuscules ? (Oui/Non){Style.RESET_ALL} ").strip().lower() == "oui"
    inclure_chiffres = input(f"{Fore.YELLOW}Voulez-vous inclure des chiffres ? (Oui/Non) {Style.RESET_ALL}").strip().lower() == "oui"
    inclure_speciaux = input(f"{Fore.YELLOW}Voulez-vous inclure des caractères spéciaux ? (Oui/Non){Style.RESET_ALL} ").strip().lower() == "oui"
    
    longueur_min_lettres = 1 if inclure_lettres else 0
    longueur_min_chiffres = 1 if inclure_chiffres else 0
    longueur_min_speciaux = 1 if inclure_speciaux else 0
    
    exclure_similaires = input(f"{Fore.YELLOW}Voulez-vous exclure les caractères similaires (par exemple, 'l' et '1', 'O' et '0') ? (Oui/Non) {Style.RESET_ALL}").strip().lower() == "oui"
    
    return inclure_lettres, inclure_chiffres, inclure_speciaux, longueur_min_lettres, longueur_min_chiffres, longueur_min_speciaux, exclure_similaires

def copier_dans_presse_papiers(mot_de_passe):
    try:
        pyperclip.copy(mot_de_passe)
        print(f"{Fore.GREEN}Le mot de passe a été copié dans le presse-papiers.{Style.RESET_ALL}")
    except pyperclip.PyperclipException:
        print(f"{Fore.RED}Impossible de copier le mot de passe dans le presse-papiers. Vous pouvez le copier manuellement.{Style.RESET_ALL}")

if __name__ == "__main__":
    afficher_banniere()
    longueur = demander_longueur()
    (inclure_lettres, inclure_chiffres, inclure_speciaux,
     longueur_min_lettres, longueur_min_chiffres, longueur_min_speciaux, exclure_similaires) = demander_criteres()
    
    mot_de_passe = generer_mot_de_passe(
        longueur, inclure_lettres, inclure_chiffres, inclure_speciaux,
        longueur_min_lettres, longueur_min_chiffres, longueur_min_speciaux, exclure_similaires)
    
    if mot_de_passe:
        mot_de_passe += " by Zwx"  
        print(f"{Fore.GREEN}Mot de passe généré :{Style.RESET_ALL} {mot_de_passe}")
        copier_dans_presse_papiers(mot_de_passe)