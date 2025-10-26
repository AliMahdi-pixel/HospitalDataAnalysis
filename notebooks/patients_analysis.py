# ANALYSE COMPLÈTE DES DONNÉES HOSPITALIÈRES - VERSION CORRIGÉE
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

print("🏥 ANALYSE DES DONNÉES PATIENTS")
print("=" * 50)

# 1. Chargement des données
df = pd.read_csv("data/patients.csv")
print("✅ Données chargées avec succès")

# 2. Exploration des données
print(f"\n📊 INFORMATIONS GÉNÉRALES")
print(f"Nombre total de patients : {len(df)}")
print(f"Nombre de variables : {len(df.columns)}")

print("\n🔍 APERÇU DES DONNÉES :")
print(df.head())

# 3. Statistiques descriptives
print("\n📈 STATISTIQUES DESCRIPTIVES")
print(df.describe())

print("\n👥 RÉPARTITION PAR SEXE")
sex_counts = df['Sex'].value_counts()
print(sex_counts)

print("\n🏥 DIAGNOSTICS DES PATIENTS")
diagnosis_counts = df['Diagnosis'].value_counts()
print(diagnosis_counts)

# 4. Visualisations
print("\n🎨 CRÉATION DES GRAPHIQUES...")

# Graphique 1 : Cholesterol vs Age
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
colors = {'M': 'blue', 'F': 'red'}
for sex in df['Sex'].unique():
    subset = df[df['Sex'] == sex]
    plt.scatter(subset['Age'], subset['Cholesterol'], 
               c=colors[sex], label=sex, alpha=0.7, s=80)

plt.xlabel('Âge (années)')
plt.ylabel('Cholestérol (mg/dL)')
plt.title('Cholestérol vs Âge')
plt.legend()
plt.grid(True, alpha=0.3)

# Graphique 2 : Diagramme des diagnostics
plt.subplot(1, 2, 2)
diagnosis_counts.plot(kind='bar', color='lightgreen')
plt.title('Répartition des Diagnostics')
plt.xlabel('Diagnostic')
plt.ylabel('Nombre de patients')
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)

plt.tight_layout()

# SAUVEGARDE CORRIGÉE
try:
    plt.savefig('analysis_results.png', dpi=150, bbox_inches='tight')
    print("✅ Graphique sauvegardé : analysis_results.png")
except Exception as e:
    print(f"❌ Erreur sauvegarde : {e}")
    # Essayer un autre emplacement
    plt.savefig('../notebooks/analysis_results.png', dpi=150, bbox_inches='tight')
    print("✅ Graphique sauvegardé dans le dossier parent")

plt.show()

# 5. Analyses avancées
print("\n🔬 ANALYSES COMPLÉMENTAIRES")

# Patients à risque (cholestérol > 220 ou pression > 140)
high_risk = df[(df['Cholesterol'] > 220) | (df['BloodPressure'] > 140)]
print(f"Nombre de patients à risque élevé : {len(high_risk)}")

# Moyennes par sexe
print("\n📊 MOYENNES PAR SEXE :")
means_by_sex = df.groupby('Sex')[['Age', 'BloodPressure', 'Cholesterol']].mean()
print(means_by_sex.round(2))

# 6. Sauvegarde des résultats
print("\n💾 SAUVEGARDE DES RÉSULTATS...")

# Créer un rapport texte
try:
    with open('analysis_report.txt', 'w', encoding='utf-8') as f:
        f.write("RAPPORT D'ANALYSE - DONNÉES HOSPITALIÈRES\n")
        f.write("=" * 50 + "\n")
        f.write(f"Date de l'analyse : {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M')}\n")
        f.write(f"Nombre de patients analysés : {len(df)}\n")
        f.write(f"Âge moyen : {df['Age'].mean():.1f} ans\n")
        f.write(f"Pression artérielle moyenne : {df['BloodPressure'].mean():.1f}\n")
        f.write(f"Cholestérol moyen : {df['Cholesterol'].mean():.1f}\n\n")
        
        f.write("RÉPARTITION PAR SEXE :\n")
        for sex, count in sex_counts.items():
            f.write(f"- {sex} : {count} patients\n")
        
        f.write("\nDIAGNOSTICS :\n")
        for diagnosis, count in diagnosis_counts.items():
            percentage = (count / len(df)) * 100
            f.write(f"- {diagnosis} : {count} patients ({percentage:.1f}%)\n")
    print("✅ Rapport sauvegardé : analysis_report.txt")
except Exception as e:
    print(f"❌ Erreur rapport : {e}")

# 7. Vérification des fichiers créés
print("\n🔍 VÉRIFICATION DES FICHIERS CRÉÉS :")
import glob
files = glob.glob('*.png') + glob.glob('*.txt')
if files:
    for file in files:
        print(f"📄 {file}")
else:
    print("❌ Aucun fichier créé")

# 8. Résumé final
print("\n" + "=" * 50)
print("🎉 ANALYSE TERMINÉE !")
print("=" * 50)
print(f"📋 Patients analysés : {len(df)}")
print(f"📈 Graphiques créés : 2 (dans analysis_results.png)")
print(f"💾 Fichiers générés : Voir liste ci-dessus")
print("=" * 50)