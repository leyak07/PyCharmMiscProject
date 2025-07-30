import streamlit as st

# Titre de l'application
st.title("Calculateur d'IMC")
st.subheader("Indice de Masse Corporelle")

# Saisie des données personnelles
nom = st.text_input("Entrez votre nom")
prenom = st.text_input("Entrez votre prénom")
age = st.number_input("Entrez votre âge", min_value=0, max_value=120, step=1)
sexe = st.radio("Entrez votre sexe", ["H", "F"])

# Saisie des données physiques
poids = st.number_input("Entrez votre poids (kg)", min_value=0.0, format="%.2f")
taille = st.number_input("Entrez votre taille (m)", min_value=0.0, format="%.2f")

# Calcul de l'IMC et affichage des résultats
if st.button("Calculer l'IMC"):
    if taille > 0 and poids > 0:
        imc = poids / (taille ** 2)

        # Interprétation
        if imc < 16:
            interpretation = "Dénutrition sévère"
        elif 16 <= imc < 18.5:
            interpretation = "Maigreur"
        elif 18.5 <= imc < 25:
            interpretation = "Corpulence normale"
        elif 25 <= imc < 30:
            interpretation = "Surpoids"
        elif 30 <= imc < 35:
            interpretation = "Obésité modérée (classe 1)"
        elif 35 <= imc < 40:
            interpretation = "Obésité sévère (classe 2)"
        else:
            interpretation = "Obésité morbide (classe 3)"

        # Affichage
        st.markdown("### Résultat du diagnostic")
        st.write(f"**Nom :** {nom}")
        st.write(f"**Prénom :** {prenom}")
        st.write(f"**Âge :** {age} ans")
        st.write(f"**Sexe :** {sexe}")
        st.write(f"**Poids :** {poids} kg")
        st.write(f"**Taille :** {taille} m")
        st.write(f"**IMC :** {imc:.2f}")
        st.success(f"**Interprétation médicale :** {interpretation}")
    else:
        st.error("Veuillez entrer un poids et une taille valides (non nuls).")
