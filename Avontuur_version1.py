# Ideeën: Grotere wereld en dat je moet vechten met beesten met levens

# De dictionary met twee locaties: hal en keuken
# Beiden hebben een beschrijving en locatie ten opzichte van elkaar

import time
import copy

wereldkaart = {
    "hal" : {
        "omschrijving" : "De hal: Je komt hier het huis binnen, doe je schoenen uit", 
        "noord" : "woonkamer",
        "oost" : "toilet",
        "west" : "opslag"
    },
    "keuken" : {
        "omschrijving" : "De keuken: Als je binnenkomt, ruik je het heerlijke eten al",
        "zuid" : "eetkamer",
        "noord" : "tuin",
        "oost" : "speelkamer",
        "item" : {"naam" : "mes", "Hp" : 0, "Ap" : 10} 
    },
    "opslag" : {
        "omschrijving" : "De opslag: neuzel maar eens goed rond, misschien vind je iets nuttigs!",
        "oost" : "hal",
        "item" : {"naam": "deken", "Hp" : 100, "Ap" : 0},
        "vijand" : {"naam" : "Plork", "Hp" : 45, "Ap" : 20}
    },
    "slaapkamer" : {
        "omschrijving" : "De slaapkamer: wil je een dutje doen?",
        "noord" : "wijnkelder",
        "west" : "speelkamer",
        "item" : {"naam" : "bed", "Hp" : 5, "Ap" : 0}
    },
    "eetkamer" : {
        "omschrijving" : "De eetkamer: eet je buikje maar goed vol!",
        "noord" : "keuken",
        "oost" : "woonkamer",
        "item" : {"naam" : "taart", "Hp" : 25, "Ap" : 0}
    },
    "speelkamer" : {
        "omschrijving" : "De speelkamer: speel een potje snooker of gooi een dartpijltje",
        "oost" : "slaapkamer",
        "zuid" : "woonkamer",
        "west" : "keuken",
        "item" : {"naam" : "dartpijltje", "Hp" : 0, "Ap" : 6}
    },
    "woonkamer" : {
        "omschrijving" : "De woonkamer: warm jezelf maar bij het vuur",
        "noord" : "speelkamer",
        "oost" : "studeerkamer",
        "zuid" : "hal",
        "west" : "eetkamer",
        "item" : {"naam" : "televisie", "Hp" : 0, "Ap" : 0} #Ik wil bij dit item gewoon dat je 10 seconden moet wachten
    },
    "toilet" : {
        "omschrijving" : "Het toilet: wat je hier uitspookt blijft tussen 4 muren",
        "west" : "hal",
        "item" : {"naam" : "ontstopper", "Hp" : 0, "Ap" : 2}
    },
    "studeerkamer" : {
        "omschrijving" : "De studeerkamer: o wee als je een onvoldoende haalt!",
        "west" : "woonkamer",
        "item" : {"naam" : "boek", "Hp" : 0, "Ap" : 3}
    },
    "tuin" : {
        "omschrijving" : "De tuin: lekker chillen in de zon met een boekje",
        "zuid" : "keuken",
        "oost" : "zwembad",
        "item" : {"naam" : "plant", "Hp" : 200, "Ap" : -6},
        "vijand" : {"naam" : "nijntje", "Hp" : 110, "Ap" : 30}
    },
    "zwembad" : {
        "omschrijving" : "Het zwembad: heerlijk dobberen in het zonnetje",
        "west" : "tuin",
        "item" : {"naam" : "opblaaskrokodil", "Hp" : -100, "Ap" : 0}
    },
    "wijnkelder" : {
        "omschrijving" : "De wijnkelder: doe me nog een glaasje",
        "zuid" : "slaapkamer",
        "vijand" : {"naam" : "Eindbaas Vinor", "Hp" : 700, "Ap": 6}
    }
}

# Hier een kopie van de wereldkaart
wereldkaart_backup = copy.deepcopy(wereldkaart)

# Hier wordt de huidige kamer gedefinieerd
huidige_kamer = "hal"

# We beginnen met een lege rugzak
rugzak = []

# We starten met volle Hp
levens = 100

# Onze basiskracht is 10
kracht = 10

print("Hallo, welkom bij Mansions Adventure! Het is je doel om je weg te vinden en de eindbaas te verslaan!")
naam = input("Wat is jouw naam, dappere avonturier? ")

print(f"Hallo {naam}! Je begint dit spel met een lege rugzak, {levens} levens en {kracht} kracht!")
time.sleep(1)

while True:
    #Print de omschrijving van de huidige kamer
    kamer_pakketje = wereldkaart.get(huidige_kamer)
    print(kamer_pakketje["omschrijving"])

    # Is er een monster in de kamer
    if "vijand" in kamer_pakketje:
        levens_vijand = wereldkaart[huidige_kamer]["vijand"]["Hp"]
        kracht_vijand = wereldkaart[huidige_kamer]["vijand"]["Ap"]

        # We leven hier nog
        speler_is_dood = False

        print(f"Je bent gestuit op {wereldkaart[huidige_kamer]['vijand']['naam']}!")
        print(f"{wereldkaart[huidige_kamer]['vijand']['naam']} heeft {levens_vijand} levens en {kracht_vijand} kracht!")
        vlecht = input("Ga je vechten of vluchten? Typ 'vecht' of 'vlucht'")
        if vlecht == 'vlucht':
            print("Durf je het nog niet aan? Ga dan terug naar de hal.")
            huidige_kamer="hal"
            continue
        elif vlecht == "vecht":
            print("Het gevecht begint!")

            while levens_vijand > 0:
                #Wacht tot de speler op Enter drukt voor de volgende beurt
                input("\nDruk op [Enter] om de volgende beurt te starten...")
                print("-" * 50)

                # De vijand valt ons aan
                levens -= kracht_vijand
                if levens <=0:
                    print("Je bent dood! Je wordt wakker in de hal...")
                    time.sleep(3)
                    huidige_kamer = 'hal'
                    levens = 100
                    kracht = 10
                    rugzak = []
                    wereldkaart = copy.deepcopy(wereldkaart_backup)
                    speler_is_dood = True
                    break

                # We vallen de vijand aan
                levens_vijand -= kracht
                if levens_vijand <=0:
                    #Hier nog specifiek op als we vinor verslaan dat we dan het spel winnen
                    print(f"Je hebt {wereldkaart[huidige_kamer]['vijand']['naam']} verslagen! Ga zo door!")
                    if wereldkaart[huidige_kamer]["vijand"]["naam"] == 'Plork':
                        print("Je ziet plotseling een luik in de kamer")
                        print("Je opent het luik...")
                        time.sleep(1)
                        rugzak.append("sleutel")
                        print("Je vond een sleutel, hopelijk komt die nog van pas!")
                    
                    del wereldkaart[huidige_kamer]["vijand"]
                    break

                print(f"Je hebt nog {levens} levens en je vijand nog {levens_vijand}! Ga zo door!")
                time.sleep(0.5)
        else:
            print("Ongeldige keuze! Kies 'vecht' of 'vlucht'.")
            continue

        # Hier controleren we of de speler dood is
        if speler_is_dood == True:
            continue
    
    # Is er een item in de kamer
    if "item" in kamer_pakketje:
        print(f"Je hebt een {wereldkaart[huidige_kamer]["item"]["naam"]} gevonden!")
        gepakt = input('Wil je dit item gebruiken? Antwoord "ja" of "nee" ').lower()
        if gepakt=="ja":
            # We stoppen eerst het item in onze rugzak

            if wereldkaart[huidige_kamer]["item"]['naam'] == 'televisie':
                print("Je gaat lekker voor de televisie zitten")
                time.sleep(5)
            elif wereldkaart[huidige_kamer]['item']['naam'] == 'bed':
                print("Je gaat eens lekker liggen voor een kort dutje")
                time.sleep(5)
            else:
                rugzak.append(wereldkaart[huidige_kamer]["item"])
                print(f"Je stopt {wereldkaart[huidige_kamer]["item"]["naam"]} in je rugzak")

            # Hier nog toevoegen dat het optioneel is?
            # We krijgen de Hp van het item als het niet 0 is
            if wereldkaart[huidige_kamer]["item"]["Hp"] != 0:
                if wereldkaart[huidige_kamer]["item"]['naam'] == 'bed':
                    levens += wereldkaart[huidige_kamer]['item']['Hp']
                    print(f"Na deze powernap krijg je {wereldkaart[huidige_kamer]['item']['Hp']} levens.")
                else:
                    levens += wereldkaart[huidige_kamer]["item"]["Hp"]
                    print(f"Je gebruikt de/het {wereldkaart[huidige_kamer]["item"]["naam"]}! Je krijgt {wereldkaart[huidige_kamer]["item"]["Hp"]} HP. Je levens zijn nu {levens}")

            # We krijgen de kracht van het item als het niet 0 is
            if wereldkaart[huidige_kamer]['item']['Ap'] != 0:
                kracht += wereldkaart[huidige_kamer]["item"]["Ap"]
                print(f"Je gebruikt de/het {wereldkaart[huidige_kamer]["item"]["naam"]}! Je krijgt {wereldkaart[huidige_kamer]["item"]["Ap"]} kracht. Je kracht is nu {kracht}")
            
            #Speciaal voor de televisie
            #if wereldkaart[huidige_kamer]["item"]["Hp"] == 0 and wereldkaart[huidige_kamer]["item"]["Ap"] == 0:
            #    print("Je ziet slechts ruis en hoort een pieptoon, wat een tijdverspilling!")
            if wereldkaart[huidige_kamer]["item"]['naam'] == 'televisie':
                print("Je ziet slechts ruis en hoort een pieptoon, wat een tijdverspilling!")

            # Verwijder het item uit de kamer
            del wereldkaart[huidige_kamer]["item"]
        if gepakt!="ja":
            print(f"Je laat {wereldkaart[huidige_kamer]['item']['naam']} in {huidige_kamer} liggen!")
    else:
        if huidige_kamer == 'wijnkelder':
            print("Gefeliciteerd! Je hebt de eindbaas verslagen!")
            break
        else:
            #print("Er valt hier niets op te pakken!")
            #continue
            pass

    # Vraag de speler om een richting
    richting = input("Welke kant wil je nu op? (of typ 'stop' om te stoppen met het spel)").lower()

    # Als de speler stopt, ga uit de loop
    if richting == 'stop':
        print("Bedankt voor het spelen!")
        break

    # Controleer of de richting in de dictionary bestaat met in
    # Hier eventueel nog een sleutel toevoegen voor de woonkamer
    if richting in wereldkaart[huidige_kamer].keys():
        if huidige_kamer == 'hal':
            if richting == 'noord':
                if 'sleutel' in rugzak:
                    print("Je draait de sleutel om in het slot, en...")
                    time.sleep(2)
                    huidige_kamer = wereldkaart[huidige_kamer][richting]
                else:
                    print("Je hebt een sleutel nodig om deze kamer te openen!")
            else:
                huidige_kamer=wereldkaart[huidige_kamer][richting]
        else:
            huidige_kamer = wereldkaart[huidige_kamer][richting]
    else:
        print("Hier is geen deur!")

