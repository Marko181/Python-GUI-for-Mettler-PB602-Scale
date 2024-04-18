import tkinter as tk
import serial
import threading
import time

# Function to handle continuous reading from the serial port
def read_from_scale():
    while not stop_thread.is_set():
        try:
            if ser.in_waiting > 0:  # Check if data is available
                response = ser.readline().decode().strip()  # Read data
                update_response_label(response)  # Update the GUI with the response
        except Exception as e:
            update_response_label("Napaka pri branju: " + str(e))
        time.sleep(0.1)  # Short delay to prevent excessive CPU usage

# Update the GUI safely from another thread
def update_response_label(text):
    def task():
        response_label.config(text="Odgovor naprave: " + text)
    root.after(1, task)  # Schedule GUI update on main thread

# Function to send command to the scale
def send_command():
    command = command_entry.get()
    try:
        ser.write((command + '\r\n').encode())
    except Exception as e:
        update_response_label("Napaka pri pošiljanju ukaza: " + str(e))

# RS232 connection settings
ser = serial.Serial(
    port='COM1',
    baudrate=9600,
    timeout=1
)

# Check if the connection is established
if ser.is_open:
    print("Povezava vzpostavljena.")
else:
    print("Napaka pri vzpostavljanju povezave.")
    exit()

# Create the main window
root = tk.Tk()
root.title("Pošiljanje ukazov preko RS232")

# Create the entry for the command
command_entry = tk.Entry(root, width=50)
command_entry.pack(pady=10)

# Create the send button
send_button = tk.Button(root, text="Pošlji ukaz", command=send_command)
send_button.pack(pady=5)

# Create the label for the device response
response_label = tk.Label(root, text="")
response_label.pack(pady=10)

# Thread control variable
stop_thread = threading.Event()

# Start the reading thread
reading_thread = threading.Thread(target=read_from_scale)
reading_thread.start()

# Function to close RS232 connection and stop the thread
def on_closing():
    stop_thread.set()  # Signal the thread to stop
    reading_thread.join()  # Wait for the thread to finish
    ser.close()
    root.destroy()

# Set the on_closing function as the handler for the window close event
root.protocol("WM_DELETE_WINDOW", on_closing)

# Run the main loop
root.mainloop()
