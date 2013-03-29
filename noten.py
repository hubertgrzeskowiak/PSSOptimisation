# encoding: utf-8
import sys
from bs4 import BeautifulSoup
import urlparse

class ParsingError(Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg)

def main():
    if len(sys.argv) != 2:
        print "Dieses Programm benötigt eine html Datei als Parameter!"
        print "Speichere deine PSSO Seite, auf der die Noten zu sehen sind"
        print "und gib den Namen auf der Kommandozeile als Parameter an."
        print "Zum Beispiel: python noten.py rds.html"
        sys.exit(1)
    infos = getInfosFromHTMLFile(sys.argv[1])
    print "Anzahl der Noten: "+str(infos[0])
    print "Anzahl der Credits: "+str(infos[1])
    print "Notenschnitt: "+str(infos[2])

def getInfosFromHTMLFile(html_file_path):
    return getInfos(open(html_file_path).read())

def getInfos(html):
    """
    Der Rückgabewert ist ein 3-Elemente Tupel aus:
    - Anzahl der Noten
    - Anzahl der Credits
    - Notenschnitt
    """
    soup = BeautifulSoup(html)

    # Finde die richtige Tabelle. sie hat kein summary Attribut.
    noten_table = None
    noten_table = soup('table')[1]
    noten_table = noten_table.tbody or noten_table
    
    rows = noten_table.find_all("tr", recursive=False)

    # Erste Zeile enthält nur <th>. Wenn wir die Reihe rausschmeißen, haben wir
    # nachher leichtere Arbeit.
    del rows[0]

    # Hier speichern wir Tupel mit Note und Credits Anzahl
    noten_und_credits = []

    for tr in rows:
        # Alle Zellen mit Noten enthalten diese Klasse.
        # Überspringe deswegen die Reihen, deren erste Zelle sie nicht hat
        if tr.td["class"] != ["tabelle1_alignleft"]:
            continue
        # Alle übrigen Zellen enthalten entweder Noten und Credits oder ihnen
        # fehlt eines der Felder. Nichtbestandene Prüfungen geben 0 Credits.
        # Wir beachten also nur Zellen die Credits != 0,0 enthalten
        zellen = tr.find_all("td")
        credits = zellen[7].text.strip().replace(',', '.')
        if credits != "0.0":
            note = tr.find_all("td")[5].text.strip().replace(',', '.')
            noten_und_credits.append((float(note), float(credits)))

    note_gesamt = 0.0
    credits_gesamt = 0.0
    notenschnitt = 0.0
    for n, c in noten_und_credits:
        credits_gesamt += c
        note_gesamt += n
        notenschnitt += c*n
    notenschnitt /= credits_gesamt

    return (len(noten_und_credits),
            credits_gesamt,
            round(notenschnitt, 2))

def getLinkByName(html, name):
    soup = BeautifulSoup(html)
    return soup.find("a", text=name)["href"]

def getLinkByGraphic(html, img_src):
    soup = BeautifulSoup(html)
    for link in soup("a"):
        img = link.find("img", src=img_src)
        if img:
            return link["href"]

def getStudentName(html):
    soup = BeautifulSoup(html)
    return soup.find("table", summary=True).find("td").string

def checkLogin(html):
    soup = BeautifulSoup(html)
    return not bool(soup.find("font", text="Anmeldung fehlgeschlagen"))

    

if __name__ == "__main__":
    main()