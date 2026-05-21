import pandas as pd

# We pakken een paar kamers uit jouw game als test-data
data_kamers = {
    "Kamer": ["Hal","Opslag", "Toilet","Eetkamer", "Woonkamer", "Studeerkamer", "Keuken", "Speelkamer", "Slaapkamer", "Tuin", "Zwembad", "Wijnkelder"],
    "Type_Item": ["Geen", "Deken", "Ontstopper", "Taart", "Televisie", "Boek", "Mes", "Dartpijltje", "Bed", "Plant", "Opblaaskrokodil", "Geen"],
    "HP_Bonus": [0, 100, 0, 25, 0, 0, 0, 0, 5, 200, -100, 0],
    "AP_Bonus": [0, 0, 2, 0, 0, 3, 10, 6, 0, -6, 0, 0],
    "Heeft_Vijand": [False, True, False, False, False, False, False, False, False, True, False, True]
}

# Hier gebeurt de magie: we maken het Dataframe!
df = pd.DataFrame(data_kamers)

# Laat de tabel zien op het scherm
print("-" * 60)
print(df)
print("-" * 60)

# Hiermee berekenen we het gemiddelde van bijvoorbeeld de HP-bonus
print(df["HP_Bonus"].mean())

# Hiermee laten we alleen zien in welke kamers een vijand zit
print(df[df["Heeft_Vijand"] == True])
print("-" * 60)

# Dit commando geeft je meteen een complete samenvatting van alle cijfers
#print(df.describe())

# Door een lijst met kamers mee te geven, selecteren we specifieke kolommen
hp_tabel = df[['Kamer', 'HP_Bonus']]

print("1. Enkel de HP kolommen:")
print(hp_tabel)

# Filter: geef me alle tijden waar AP_Bonus groter is dan 0
kracht_kamers = df[df['AP_Bonus']>0]

print("2. Kamers waar je kracht (Ap) verdient:")
print(kracht_kamers)

# We sorteren op HP_Bonus. 'ascending=False' zorgt ervoor dat de hoogste bovenaan staat
gesorteerd_op_hp = df.sort_values(by='HP_Bonus', ascending=False)

print("3. Kamers gesorteerd van de hoogste HP-bonus naar de laagste:")
print(gesorteerd_op_hp[['Kamer', 'Type_Item', 'HP_Bonus']])

# We gaan nu rekenen met Data
print("\n" + "="* 20 + " DATA STATISTIEKEN " + "="*20)

# 1. Hoeveel HP zit er in totaal verstopt in het hele huis?
totale_hp = df['HP_Bonus'].sum()
print(f"Totale hoeveelheid HP in het huis: {totale_hp} HP")

# 2. Wat is de gemiddelde aanvalskracht (AP) van de items?
gem_ap = df["AP_Bonus"].mean()
print(f"De gemiddelde AP bonus per kamer: {gem_ap:.2f} AP")

# 3. Hoeveel gevaarlijke kamers (met vijanden) zijn er in totaal?
aantal_gevaarlijk = df["Heeft_Vijand"].sum()
print(f"Er zijn {aantal_gevaarlijk} kamers met een vijand!")

# Hieronder nog een statistische samenvatting
print("\n--- STATISTISCHE SAMENVATTING ---")
print(df.describe())

# Nu gaat we grafieken maken!
import matplotlib.pyplot as plt # We importeren de grafieken-module

# 1. We bepalen de grootte van ons grafiekscherm (breedte, hoogte in inches)
plt.figure(figsize=(12,6))

# 2. We maken een staafdiagram: Kamer op de X-as, HP_bonus op de Y-as
# We geven de balken een mooie blauwe kleur en een zwarte rand
plt.bar(df['Kamer'], df['HP_Bonus'], color='skyblue', edgecolor='black')

# 3. We voegen titels en labels toe zodat de grafiek leesbaar is
plt.title("HP Bonus per Kamer in Mansions Adventure", fontsize = 16, fontweight='bold')
plt.xlabel('Kamers', fontsize=12)
plt.ylabel('HP Bonus', fontsize=12)
# Vraag: Hoe weet ik welke input deze methods geven?

# 4. We draaien de namen van de kamers een kwartslag (45 graden) zodat ze niet door elkaar lopen
plt.xticks(rotation=45)

# 5. We voegen een handig hulprooster toe op de achtergrond (alleen horizonaal)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 6. Zorg ervoor dat alles netjes binnen het plaatje past zonder dat er tekst wegvalt
plt.tight_layout()

#7 DE GOUDEN KNOP: Laat de grafiek zien op je scherm!
plt.show()
