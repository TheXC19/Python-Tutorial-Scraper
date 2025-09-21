# Python Tutorial Scraper

## Description

Ce projet est un script Python éducatif qui permet de scraper automatiquement le contenu des tutoriels Python depuis le site [pythontutorial.net](https://www.pythontutorial.net/). Le script extrait les informations structurées de différentes catégories de tutoriels Python et génère un fichier JSON contenant tous les liens, titres et résumés des cours.

## Fonctionnalités

- **Scraping automatique** : Extraction des liens et contenus depuis pythontutorial.net
- **Structure organisée** : Organisation par catégories (Basics, OOP, Concurrency, etc.)
- **Résumés automatiques** : Génération de résumés pour chaque tutoriel
- **Export JSON** : Sauvegarde des données dans un fichier JSON structuré
- **Headers personnalisés** : Utilisation d'un User-Agent pour éviter les blocages

## Catégories couvertes

Le script extrait les tutoriels des catégories suivantes :
- Python Basics
- Python OOP (Programmation Orientée Objet)
- Python Concurrency (Programmation concurrente)
- Advanced Python
- Python Regex (Expressions régulières)
- Unit Testing (Tests unitaires)
- NumPy
- Tkinter (Interface graphique)
- PyQt (Interface graphique avancée)
- Django (Framework web)

## Installation

1. Clonez ce repository :
```bash
git clone https://github.com/TheXC19/Python-Tutorial-Scraper.git
cd python-tutorial-scraper
```

2. Installez les dépendances :
```bash
pip install -r requirements.txt
```

## Utilisation

Exécutez simplement le script principal :

```bash
python scraper.py
```

Le script va :
1. Se connecter à pythontutorial.net
2. Extraire les liens et contenus de chaque catégorie
3. Générer des résumés pour chaque tutoriel
4. Sauvegarder le tout dans `FinalScrapingPythonTuto.json`

## Structure du fichier de sortie

Le fichier JSON généré a la structure suivante :

```json
{
    "Python Basics": {
        "Section Name": [
            {
                "Name": "Titre du tutoriel",
                "resume": "Résumé du contenu...",
                "link": "https://www.pythontutorial.net/..."
            }
        ]
    }
}
```

## Fonctions principales

### `ResumeSujet(link)`
- Extrait le résumé d'un tutoriel spécifique
- Utilise BeautifulSoup pour parser le HTML
- Retourne un résumé formaté

### `addCategorie(link, Title)`
- Scrape une catégorie complète de tutoriels
- Organise les liens par sections
- Génère les résumés pour chaque tutoriel
- Ajoute les données au dictionnaire global

## Considérations éthiques

⚠️ **Important** : Ce projet est à des fins éducatives uniquement. Assurez-vous de :
- Respecter les conditions d'utilisation du site scraped
- Ne pas surcharger le serveur avec trop de requêtes
- Utiliser les données de manière éthique et légale

## Améliorations possibles

- Ajouter un système de cache pour éviter les requêtes répétitives
- Implémenter un délai entre les requêtes
- Ajouter la gestion d'erreurs pour les liens brisés
- Créer une interface graphique pour la consultation des données
- Ajouter un système de mise à jour automatique

## Technologies utilisées

- **Python 3.x**
- **Requests** : Pour les requêtes HTTP
- **BeautifulSoup4** : Pour le parsing HTML
- **JSON** : Pour la sérialisation des données

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
- Signaler des bugs
- Proposer des améliorations
- Ajouter de nouvelles fonctionnalités

## Licence

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

## Avertissement

Ce script est fourni à des fins éducatives. L'utilisateur est responsable de s'assurer que son utilisation respecte les conditions d'utilisation du site web cible.
