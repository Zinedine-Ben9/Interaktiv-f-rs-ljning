Interaktiv försäljningsanalys

Detta är ett Python-projekt som analyserar försäljningsdata från databasen classicmodels. Programmet använder ett grafiskt gränssnitt med Tkinter där användaren kan välja olika analyser och visualiseringar.

Projektet är gjort som ett skolprojekt och visar hur Python kan användas tillsammans med SQL, databaser, diagram och enkel prognosberäkning.

Funktioner

Programmet kan:

Ansluta till en MySQL-databas
Visa försäljning per land
Visa antal ordrar per kund
Visa försäljning över tid
Skapa en enkel försäljningsprognos med linjär regression
Visa resultat med diagram i Matplotlib
Tekniker som används

Python
Tkinter
MySQL
Matplotlib
NumPy
SQL
Säkerhet

Databaslösenord och privata uppgifter ska inte sparas direkt i koden.

Använd istället miljövariabler eller en lokal .env-fil som inte laddas upp till GitHub.

Exempel:

import os

password = os.getenv("MYSQL_PASSWORD")
