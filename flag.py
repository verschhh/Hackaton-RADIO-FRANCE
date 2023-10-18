import nltk

mots_cles_discriminatoires = ["discrimination", "racisme", "sexisme", "homophobie", "xénophobie", "Israel", "Palestine", "USA", "Russie", "Ukraine", "Viol", "Agression Sexuel", "Patriarca", "Immigré"]

texte_emission = open("transcript.txt", "r").read()

def check_discriminatory_keywords(texte):
    for mot_cle in mots_cles_discriminatoires:
        if mot_cle in texte.lower():
            return f"Mot-clé discriminatoire trouvé : {mot_cle}"
    return "Aucun mot-clé discriminatoire trouvé."

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        file_contents = file.read()
        result = check_discriminatory_keywords(file_contents)
        return result

file_path = 'transcript.txt'
result = process_file(file_path)
print(result)
