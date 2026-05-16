START
  |
  v
Läs databasinställningar från miljövariabler
  |
  v
Försök ansluta till MySQL-databasen
  |
  v
Lyckades anslutningen?
  |
  |-- Nej --> Visa felmeddelande --> AVSLUTA
  |
  |-- Ja --> Öppna GUI med Tkinter
                |
                v
        Vänta på användarens val
                |
                v
        Användaren väljer funktion
                |
                |-- Visa försäljning per land
                |       |
                |       v
                |   Kör SQL-fråga
                |       |
                |       v
                |   Visa stapeldiagram
                |
                |-- Visa ordrar per kund
                |       |
                |       v
                |   Kör SQL-fråga
                |       |
                |       v
                |   Visa diagram
                |
                |-- Visa försäljning över tid
                |       |
                |       v
                |   Kör SQL-fråga
                |       |
                |       v
                |   Visa linjediagram
                |
                |-- Visa prognos
                |       |
                |       v
                |   Hämta historisk försäljningsdata
                |       |
                |       v
                |   Beräkna linjär regression med NumPy
                |       |
                |       v
                |   Visa historisk data och prognos
                |
                |-- Avsluta
                        |
                        v
                Stäng databaskoppling
                        |
                        v
                    AVSLUTA
