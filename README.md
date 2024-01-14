# Y2_2022_12618

Labyrintti projekti aalto yliopiston kurssille CS-A1121 varten

Riippuvuudet:
python-qt5 (graafinen toiminta ympäristö) 


## Checkpoint2

   Dijksras algoritmi toimii samoin DFS-labyrintin luonti algoritmi mutta text guin teksti versiossa näyttää olevan bugeja. 

   Lisäksi yksittäisi testejä on tehty koodille testaamaan toiminnallisuutta tietyissä luokka olioissa.

   1.4.22 import ja export file toimtvat helpoissa tapauksissa. Tarvitaan ainakin universaalimpaa koodia import metodille. Testejä on toteutettu import metodille  

   15.4.22 importissa on selvinnyt bugeja ja alkeelista guita luotu pelille. Nyt pelissä pelaaja liikuu (vihreät pallo) ja kun pääsee maaliin lopettaa liikkumisen (keltainen ruutu). Labyrintti ei piirry oikein ja esim pelaaja hyppää seinien yli. Importissa on vielä isompia ongelmia esimerkiksi pelaaja saattaa hypätä pois kartalta.

## Käyttöohje
    
    aja test_gui.py nähdäksesi graafisen käyttöliittymän toiminnallisuutta. 

## Aikataulu

    Käytetyt päivät 7-9 päivää eli noin 56-72 h
   
## Muuta
    Teksti pohjainen gui on vaikea toteuttaa pythonilla, koska meni aikaa tajuta että [luokka * 3] luo tasan saman luokan listan sisään eikä 3 eri luokan tapausta

    Muutoksia on tullut luokkan sisäisiin tietorakenteisiin verrattuna dokumentissa oleviin

    Gui tekeminen lähtenyt hyvin käytiin. Muutama bugia ja toiminnallisuutta lukuunottamatta. Esimerkiksi ongelma kohta on miten toteuttaa animaationa dijkstran toteuttama stack ratkaisusta.


    
