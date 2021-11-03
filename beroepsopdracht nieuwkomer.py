import os
#stuk 1
def begin():
    os.system("cls")
    print("Terwijl ik in mijn kamer zit hoor ik de schoten en explosies steeds dichterbij komen.\nIk moet nu echt weg hier ver van dit lawaai en geweld voor het te laat is.\nJe pakt je rugtas en loopt naar buiten.")
    groep()

#stuk 2
def groep():
    print("\nEenmaal buiten aangekomen zie je een groep mensen staan die net als jouw willen vluchten van de bezetting door de taliban.\nJe hoort dat ze naar Nederland willen vluchten omdat ze daar familie hebben.\nzal ik vragen of ik met ze mee kan of zal ik zelf proberen te vluchten.\n\na. vraag of je mee kan\nb. probeer zelf te vluchten.")
    answer1 = input()
    if answer1.lower() == "a":
        samen()
    else:
        liften()

#stuk 3
def samen():
    os.system("cls")
    print("\nJe kunt mee met de groep.\nJullie pakken wat extra eten en drinken en gaan onderweg naar Nederland.\nGaan jullie met de bus of lopend naar de grens.\n\na. ga lopend\nb. ga met de bus")
    answer2 = input()
    if answer2.lower() == "a":
        lang()
    else:
        stadje()

#stuk 4
def lang():
    os.system("cls")
    print("\nNa een uur te hebben gelopen merken jullie dat dit te lang gaat duren.\njullie bellen een taxi.")
    stadje()

#stuk 5
def stadje():
    print("\nEenmaal aangekomen in een stadje dat dicht bij de grens licht moeten jullie proberen om het land uit te komen.\nEen van de mensen uit de groep kent iemand die mensen de grens over laat smokkelen maar je weet niet zeker of dat nodig is.\n\na. bel de smokkelaar\nb. probeer door de grensbewaking te komen.")
    answer3 = input()
    if answer3.lower() == "a":
        smokkelaar()
    else:
        einde1()

#stuk 6
def smokkelaar():
    print("\nNa een tijdje te hebben gebeld met de smokkelaar komt hij jullie ophalen en over de grens brengen.\njullie worden in een vrachtwagen container gestopt en de grens over gereden.\nNu moeten jullie een manier zien te vinden om naar Nederland te komen.\n\na. probeer met mensen mee te liften naar Turkije\nb. loop naar het dichtsbijzijnde dorpje")
    answer4 = input()
    if answer4.lower() == "a":
        griekenland()
    else:
        aankomst_dorpje()

#stuk 7
def einde1():
    print("\nJe komt niet de grens over omdat de taliban niemand wil laten vluchten uit hun land.\n\nEINDE")

#stuk 8
def griekenland():
    print("\nNa 2 dagen met een vrachtwagen te hebben mee gelift kom je aan in Turkije waar vandaan je met een bootje naar Griekenland vaart.\nMaar onderweg gaat de motor van jullie boot stuk\n je probeert de motor te maken.")
    geluk()

#stuk 9 
def aankomst_dorpje():
    print("\nEenmaal aangekomen in het dropje komen er mensen naar jullie toe die vragen waar jullie heen gaan.\nNa het zeggen dat jullie naar Nederland willen zegt iemand dat hij jullie wel naar Turkije kan brengen omdat hij daar toch heen moet met zijn vrachtwagen.\ner worden jullie ook kamers aangeboden om te slapen en uitrusten.\n\na. ga mee met de vrachtwagen\nb. blijf een nacht in het dorpje")
    answer5 = input()
    if answer5.lower() == "a":
        griekenland()
    else:
        einde2()

#stuk 10
def geluk():
    print("\nHet had niet echt zin maar gelukkig ziet een boot in de vertel jullie rond drijven.\nDe boot brengt jullie naar Griekenland.\nAls jullie aankomen lopen er een paar soldaten die de grens bewaken jullie kant op.\njullie besluiten om gewoon door te lopen en te doen alsof er niks is.")
    soldaten()

#stuk 11
def einde2():
    print("\nJe schrikt wakker door het geluid van schoten.\nJullie zijn verlinkt door mensen uit het dorpje aan de taliban die jullie nu zien als landverraders\n\nEINDE")

#stuk 12
def soldaten():
    print("\nDe soldaten lopen langs jullie maar doen niks.\nNu jullie in Griekenland zijn kunnen jullie makkelijk naar Nederland gaan met de trein.")
    nederland()

#stuk 13
def liften():
    print("\nje staat langs de weg te vragen of mensen je mee kunne nemen naar de grens of het vliegveld van Kabul.\nNa een tijdje vragen zeg iemand dat je wel mee kan naar het vliegveld.")
    klapband()

#stuk 14
def klapband():
    print("\nOnderweg naar het vliegveld klapt de band van de auto uit het niets.\njullie moeten nu eerst de band maken voordat je naar het vliegveld kunt.\n\na. probeer zelf de band te vervangen\nb. wacht tot er iemand langs rijd en vraag om hulp")
    answer6 = input()
    if answer6.lower() == "a":
        vliegveld()
    else:
        einde3()

#stuk 15
def vliegveld():
    print("\nNa een uur hard werken is het gelukt om de band er op te krijgen en zijn jullie nu aangekomen op het vliegveld.\nhet lijkt wel alsof er een miljoen mensen om het vliegveld heen staan zoveel mensen willen naar binnen komen.\nJe moet proberen om op een van die vliegtuigen te komen want je weet niet of er nog nieuwe komen.\n\na. probeer door de menigte te komen\nb.rij met de auto door het hek van het vliegveld heen")
    answer7 = input()
    if answer7.lower() == "a":
        vliegen()
    else:
        vliegen()
#stuk 16
def einde3():
    print("\nterwijl je wacht tot er iemand langs rijd zie je in de verte een auto aankomen\ner zaten mensen van de taliban in die jullie achtervolgde.\n\nEINDE")

#stuk 17
def vliegen():
    print("\nhet is gelukt om op het vliegveld te komen.\nnu moet je snel een vliegtuig in komen om te vluchten.\n\na.pak het vleigtuig naar nederland\nb. pak het vliegtuig naar duitsland")
    answer8 = input()
    if answer8.lower() == "a":
        nederland()
    else:
        einde4()

#stuk 18
def einde4():
    print("\nDe taliban heeft gehoord dat er een belangrijk persoon in een Duits vliegtuig zit en wil vluchten.\nze schieten het landingstoestel stuk van het vliegtuig waardoor je niet kan vluchten.\n\nEINDE")

#stuk 19
def nederland():
    print("\nEenmaal aangekomen in Nederland word je opgenomen door de politie en ingeschreven in Nederland.\nJe vraagt een asiel aan en die word binnen een week geaccepteerd en je krijgt tijdelijk een plek om te slapen.\nje moet nu een inburgering examen maken als je in Nederland wilt wonen\n\na. leer goed voor het examen\nb. leer niet voor het examen")
    answer9 = input()
    if answer9.lower() == "a":
        inburgering()
    else:
        herkansing()
    
#stuk 20
def inburgering():
    print("\nje hebt het inburgering examen gehaald en je woont nu in Nederland waar je veilig bent voor de taliban\n\nEINDE")

#stuk 21
def herkansing():
    print("\nJe hebt het examen gezakt maar je kan een herkansing doen\n\na. leer nu wel voor het examen\nb. soms gaat het leven zo")
    answer10 = input()
    if answer10.lower() == "a":
        inburgering()
    else:
        einde5()

#stuk 22
def einde5():
    print("\nje mag niet in Nederland blijven en moet terug naar Afghanistan\n\nEINDE")

begin()

#repeat program
while True:
    print("\n\nherhaal programma?  y/n")
    loop = input()
    if loop.lower() == "y":
        begin()
    else:
        break
