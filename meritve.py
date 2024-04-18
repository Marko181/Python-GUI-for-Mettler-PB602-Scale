import tkinter as tk
import serial
import time

# Funkcija za pošiljanje ukaza
def send_command():
    command = command_entry.get()  # Pridobi ukaz iz vnosnega polja
    try:
        ser.write((command + '\r\n').encode())  # Pošlji ukaz napravi
        time.sleep(1)  # Počakaj, da se naprava odzove
        response = ser.readline().decode().strip()  # Preberi odgovor naprave
        response_label.config(text="Odgovor naprave: " + response)  # Prikaži odgovor
    except Exception as e:
        response_label.config(text="Napaka pri pošiljanju ukaza: " + str(e))

# Nastavitve RS232 povezave
ser = serial.Serial(
    port='COM1',  # Prilagodi glede na port, ki ga uporabljaš
    baudrate=9600,  # Hitrost prenosa, prilagodi glede na zahteve naprave
    timeout=1  # Časovna omejitev za branje iz serijske povezave
)

ukazi = ["S", "SI", "SIR"]

# Preveri, ali je povezava vzpostavljena
if ser.is_open:
    print("Povezava vzpostavljena.")
else:
    print("Napaka pri vzpostavljanju povezave.")
    exit()

# Ustvari glavno okno
root = tk.Tk()
root.title("Pošiljanje ukazov preko RS232")

# Ustvari vnosno polje za ukaz
command_entry = tk.Entry(root, width=50)
command_entry.pack(pady=10)

# Ustvari gumb za pošiljanje ukaza
send_button = tk.Button(root, text="Pošlji ukaz", command=send_command)
send_button.pack(pady=5)

# Ustvari oznako za prikaz odgovora naprave
response_label = tk.Label(root, text="")
response_label.pack(pady=10)

# Funkcija za zapiranje RS232 povezave ob zaprtju programa
def on_closing():
    ser.close()
    root.destroy()

# Nastavi funkcijo on_closing kot handler za dogodek zapiranja okna
root.protocol("WM_DELETE_WINDOW", on_closing)

# Zagnaj glavno zanko
root.mainloop()