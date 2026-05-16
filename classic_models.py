import os
import tkinter as tk
from tkinter import messagebox, simpledialog

import mysql.connector
import matplotlib.pyplot as plt
import numpy as np
from dotenv import load_dotenv

load_dotenv()

def connect_to_database():
"""
Ansluter till MySQL-databasen med värden från .env-filen.
"""

try:
    connection = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE")
    )

    return connection

except mysql.connector.Error as error:
    messagebox.showerror(
        "Databasfel",
        f"Kunde inte ansluta till databasen:\n{error}"
    )
    return None
def fetch_data(connection, query):
"""
Kör en SQL-fråga och returnerar resultatet.
"""

try:
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result

except mysql.connector.Error as error:
    messagebox.showerror(
        "SQL-fel",
        f"Kunde inte hämta data:\n{error}"
    )
    return []
def show_sales_by_country():
"""
Visar försäljning per land i ett stapeldiagram.
"""

query = """
    SELECT customers.country, SUM(orderdetails.priceEach * orderdetails.quantityOrdered) AS total_sales
    FROM customers
    JOIN orders ON customers.customerNumber = orders.customerNumber
    JOIN orderdetails ON orders.orderNumber = orderdetails.orderNumber
    GROUP BY customers.country
    ORDER BY total_sales DESC;
"""

data = fetch_data(db_connection, query)

if not data:
    messagebox.showwarning("Ingen data", "Det finns ingen försäljningsdata att visa.")
    return

countries = [row[0] for row in data]
sales = [float(row[1]) for row in data]

plt.figure(figsize=(12, 6))
plt.bar(countries, sales)
plt.title("Försäljning per land")
plt.xlabel("Land")
plt.ylabel("Total försäljning")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
def show_orders_by_customer():
"""
Visar topp 10 kunder efter antal ordrar.
"""

query = """
    SELECT customers.customerName, COUNT(orders.orderNumber) AS total_orders
    FROM customers
    JOIN orders ON customers.customerNumber = orders.customerNumber
    GROUP BY customers.customerName
    ORDER BY total_orders DESC
    LIMIT 10;
"""

data = fetch_data(db_connection, query)

if not data:
    messagebox.showwarning("Ingen data", "Det finns ingen orderdata att visa.")
    return

customers = [row[0] for row in data]
orders = [row[1] for row in data]

plt.figure(figsize=(12, 6))
plt.bar(customers, orders)
plt.title("Topp 10 kunder efter antal ordrar")
plt.xlabel("Kund")
plt.ylabel("Antal ordrar")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
def show_sales_over_time():
"""
Visar försäljning över tid per år.
"""

query = """
    SELECT YEAR(orders.orderDate) AS year, SUM(orderdetails.priceEach * orderdetails.quantityOrdered) AS total_sales
    FROM orders
    JOIN orderdetails ON orders.orderNumber = orderdetails.orderNumber
    GROUP BY YEAR(orders.orderDate)
    ORDER BY year;
"""

data = fetch_data(db_connection, query)

if not data:
    messagebox.showwarning("Ingen data", "Det finns ingen tidsdata att visa.")
    return

years = [row[0] for row in data]
sales = [float(row[1]) for row in data]

plt.figure(figsize=(10, 5))
plt.plot(years, sales, marker="o")
plt.title("Försäljning över tid")
plt.xlabel("År")
plt.ylabel("Total försäljning")
plt.grid(True)
plt.tight_layout()
plt.show()
def show_sales_forecast():
"""
Skapar en enkel försäljningsprognos med linjär regression.
"""

years_forward = simpledialog.askinteger(
    "Prognos",
    "Hur många år framåt vill du prognostisera?",
    minvalue=1,
    maxvalue=20
)

if years_forward is None:
    return

query = """
    SELECT YEAR(orders.orderDate) AS year, SUM(orderdetails.priceEach * orderdetails.quantityOrdered) AS total_sales
    FROM orders
    JOIN orderdetails ON orders.orderNumber = orderdetails.orderNumber
    GROUP BY YEAR(orders.orderDate)
    ORDER BY year;
"""

data = fetch_data(db_connection, query)

if len(data) < 2:
    messagebox.showwarning(
        "För lite data",
        "Det behövs minst två års data för att skapa en prognos."
    )
    return

years = np.array([row[0] for row in data])
sales = np.array([float(row[1]) for row in data])

coefficients = np.polyfit(years, sales, 1)
model = np.poly1d(coefficients)

future_years = np.arange(years[-1] + 1, years[-1] + years_forward + 1)
forecast_sales = model(future_years)

plt.figure(figsize=(10, 5))
plt.plot(years, sales, marker="o", label="Historisk försäljning")
plt.plot(future_years, forecast_sales, marker="o", linestyle="--", label="Prognos")
plt.title("Försäljningsprognos")
plt.xlabel("År")
plt.ylabel("Total försäljning")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
def close_program():
"""
Stänger databaskopplingen och avslutar programmet.
"""

if db_connection and db_connection.is_connected():
    db_connection.close()

root.destroy()
def create_gui():
"""
Skapar programmets grafiska gränssnitt.
"""

root_window = tk.Tk()
root_window.title("Interaktiv försäljningsanalys")
root_window.geometry("420x350")
root_window.resizable(False, False)

title_label = tk.Label(
    root_window,
    text="ClassicModels försäljningsanalys",
    font=("Arial", 16, "bold")
)
title_label.pack(pady=20)

subtitle_label = tk.Label(
    root_window,
    text="Välj vilken analys du vill visa",
    font=("Arial", 11)
)
subtitle_label.pack(pady=5)

button_width = 30

tk.Button(
    root_window,
    text="Visa försäljning per land",
    width=button_width,
    command=show_sales_by_country
).pack(pady=6)

tk.Button(
    root_window,
    text="Visa ordrar per kund",
    width=button_width,
    command=show_orders_by_customer
).pack(pady=6)

tk.Button(
    root_window,
    text="Visa försäljning över tid",
    width=button_width,
    command=show_sales_over_time
).pack(pady=6)

tk.Button(
    root_window,
    text="Visa prognos",
    width=button_width,
    command=show_sales_forecast
).pack(pady=6)

tk.Button(
    root_window,
    text="Avsluta",
    width=button_width,
    command=close_program
).pack(pady=20)

return root_window
db_connection = connect_to_database()

if db_connection is not None:
root = create_gui()
root.protocol("WM_DELETE_WINDOW", close_program)
root.mainloop()
