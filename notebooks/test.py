# ANALYSE SIMPLE DES PATIENTS - VERSION TEST
print("=== ANALYSE SIMPLE DES PATIENTS ===")

try:
    import pandas as pd
    print("✅ Pandas installé")
    
    import matplotlib.pyplot as plt
    print("✅ Matplotlib installé")
    
    # Charger les données
    df = pd.read_csv("data/patients.csv")
    print(f"✅ Fichier CSV lu : {len(df)} patients")
    
    # Afficher les premières données
    print("\n📊 APERÇU DES DONNÉES :")
    print(df.head())
    
    # Statistiques simples
    print(f"\n📈 STATISTIQUES :")
    print(f"Âge moyen : {df['Age'].mean():.1f} ans")
    print(f"Cholestérol moyen : {df['Cholesterol'].mean():.1f}")
    
    # Graphique SIMPLE 1 - Diagramme en barres
    print("\n🎨 CRÉATION GRAPHIQUE 1...")
    plt.figure(figsize=(8, 4))
    
    # Compter hommes/femmes
    sexes = df['Sex'].value_counts()
    plt.bar(sexes.index, sexes.values, color=['blue', 'pink'])
    plt.title("Nombre de patients par sexe")
    plt.xlabel("Sexe")
    plt.ylabel("Nombre")
    
    # Sauvegarder le graphique
    plt.savefig('graphique_sexes.png')
    print("✅ Graphique 1 sauvegardé : graphique_sexes.png")
    plt.show()
    
    # Graphique SIMPLE 2 - Points basique
    print("🎨 CRÉATION GRAPHIQUE 2...")
    plt.figure(figsize=(8, 4))
    
    # Points simples
    plt.scatter(df['Age'], df['Cholesterol'], color='green', s=50)
    plt.xlabel("Âge")
    plt.ylabel("Cholestérol")
    plt.title("Âge vs Cholestérol")
    plt.grid(True)
    
    # Sauvegarder
    plt.savefig('graphique_age_cholesterol.png')
    print("✅ Graphique 2 sauvegardé : graphique_age_cholesterol.png")
    plt.show()
    
    # Résumé final
    print(f"\n🎉 ANALYSE TERMINÉE !")
    print(f"📋 {len(df)} patients analysés")
    print(f"📈 2 graphiques créés")
    print(f"💾 Fichiers : graphique_sexes.png et graphique_age_cholesterol.png")
    
except Exception as e:
    print(f"❌ Erreur : {e}")
    print("💡 Vérifiez que le fichier data/patients.csv existe")