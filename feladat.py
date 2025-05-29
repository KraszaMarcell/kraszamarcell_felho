
def keszit_diagram_sort(nap_szama, homerseklet):
    csillagok_szama = int(homerseklet)
    csillagok = '*' * csillagok_szama
    sor = f"Nap {nap_szama:2}: {csillagok} ({homerseklet}°C)"
    return sor

# A teljes diagram kirajzolása
def rajzolj_diagram(homersekletek):
    print("Napi átlaghőmérséklet diagram (°C)") # Címsor
    print("-" * 40)	  # Elválasztó vonal

    for i in range(len(homersekletek)):  # Végigmegyünk a hőmérsékletek listáján
        nap = i + 1  # Napok számozása 1-től indul  # Nap számozása 1-től
        sor = keszit_diagram_sort(nap, homersekletek[i])  # Sor elkészítése
        print(sor)	    # Sor kiírása

# Hőmérsékleti adatok egy hétre
napi_atlaghomersekletek = [12, 15, 14, 16, 13, 17, 18]
# A diagram kirajzolása a megadott adatok alapján
rajzolj_diagram(napi_atlaghomersekletek)


