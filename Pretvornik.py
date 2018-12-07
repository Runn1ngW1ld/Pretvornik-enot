print "Pozdravljeni, jaz sem tvoj osebni pretvornik kilometrov."


kilometri = 0
milje = 0.62137119

while True:

    vprasanje = raw_input("Ali zelite nadaljevati: ")
    if vprasanje == "da":
        print "Super, bomo nadaljevali"
        kilometri = raw_input("Vpisi kilometre: ")
        kilometri = int(kilometri)
        print milje + kilometri * milje

    if vprasanje == "ne":
        print "se vidiva naslednjic: "
        break






