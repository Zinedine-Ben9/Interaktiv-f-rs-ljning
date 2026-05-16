START

Försök koppla till MySQL-databasen "classicmodels"

OM anslutning misslyckas:
    Visa felmeddelande
    AVSLUTA programmet

SKAPA GUI med Tkinter:
    Knappar:
        - Visa försäljning per land
        - Visa ordrar per kund
        - Visa försäljning över tid
        - Visa prognos
        - Avsluta

LOOPA medan programmet körs:

    Vänta på användarens val

    OM användaren väljer "Visa försäljning per land":
        Kör SQL-fråga:
            SELECT country, SUM(priceEach * quantityOrdered)
            FROM customers
            JOIN orders USING(customerNumber)
            JOIN orderdetails USING(orderNumber)
            GROUP BY country

        OM resultat är tomt:
            Visa felmeddelande
        ANNARS:
            Visa resultat i stapeldiagram med Matplotlib

    OM användaren väljer "Visa ordrar per kund":
        Kör SQL-fråga:
            SELECT customerName, COUNT(orderNumber)
            FROM customers
            JOIN orders USING(customerNumber)
            GROUP BY customerName

        OM resultat är tomt:
            Visa felmeddelande
        ANNARS:
            Visa resultat i diagram

    OM användaren väljer "Visa försäljning över tid":
        Kör SQL-fråga:
            SELECT YEAR(orderDate), SUM(priceEach * quantityOrdered)
            FROM orders
            JOIN orderdetails USING(orderNumber)
            GROUP BY YEAR(orderDate)

        OM data saknas eller är ofullständig:
            Visa felmeddelande
        ANNARS:
            Visa linjediagram med år och försäljning

    OM användaren väljer "Visa prognos":
        Be användaren ange antal år framåt

        Kör SQL-fråga:
            SELECT YEAR(orderDate), SUM(priceEach * quantityOrdered)
            FROM orders
            JOIN orderdetails USING(orderNumber)
            GROUP BY YEAR(orderDate)

        OM datamängden är för liten:
            Visa felmeddelande
        ANNARS:
            Skapa listor:
                x = år
                y = försäljning

            Använd NumPy för att beräkna linjär regression

            Skapa framtida år
            Beräkna prognosvärden

            Visa historisk data och prognos i linjediagram

    OM användaren väljer "Avsluta":
        STÄNG databaskoppling
        AVSLUTA programmet

SLUT
