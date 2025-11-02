import plotly.express as px
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

figure = px.pie(données, values='prix', names='produit', title='Chiffre d\'affaire par produit')

figure.write_html('prix-par-produit.html')

print('prix-par-produit.html généré avec succès !')
