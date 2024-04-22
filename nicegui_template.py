# .\avms\Scripts\activate
# deactivate

from nicegui import ui
import numpy as np

# Define the actions for each button press
def button_action(button_text):
    input_field.set_text(button_text)
    # Send the command to scale
    # serial_write(button_text)

    # Call function to read from the scale
    if button_text == "S" or button_text == "SI" or button_text == "Z":
        read_once_from_scale(button_text)
    else:
        read_continuously_from_scale(button_text)

# Function to read from the scale
def read_once_from_scale(comamnd):
    # serial_read() -- once
    output_field.set_text("29.1 g")

def read_continuously_from_scale(command):
    # serial_read() -- continuously
    output_field.set_text("123.9 g")

# Define styles
label_style = 'font-size: 20px; font-weight: bold;'
button_style = 'font-size: 20px; padding-top:5px; padding-bottom:5px; padding-top:5px; padding-bottom:5px; font-weight:bold; background-color: red; color: red;'
row_style = 'padding-top:5px; padding-bottom:5px;'

# Title
title = ui.label('Scale GUI').style('font-size: 50px; text-align: center; width: 100%; font-weight:bold;')

# A row for the date and time display
with ui.row().style('padding-left:20px; padding-top:5px; padding-bottom:5px;'):
    ui.label('Time:').style('font-size: 20px; font-weight:bold;')
    time = ui.label('9:20').style('font-size: 20px;')
    ui.label('Date:').style('font-size: 20px; font-weight:bold;')
    date = ui.label('19. 4. 2024').style('font-size: 20px;')

# split screen in two columns (one for buttons and one for plot)
with ui.row():
    with ui.column().style('padding-left:20px'):
        # A row for sensor readings with icons placed next to the values
        with ui.row().style(row_style):
            
            # Temperature
            with ui.column():
                ui.label('Temperature:').style(label_style)
                with ui.row().classes('items-center').style(row_style):
                    ui.icon('device_thermostat', color='primary').classes('text-5xl mr-2')
                    temperature = ui.label('15.3 °C').style('font-size: 20px;')
                    
            # Humidity        
            with ui.column().style('padding-left:20px'):
                ui.label('Humidity:').style(label_style)
                with ui.row().classes('items-center').style(row_style):
                    ui.icon('water_drop', color='primary').classes('text-5xl mr-2')
                    humidity = ui.label('33.67 %').style('font-size: 20px;')

            # Pressure        
            with ui.column().style('padding-left:20px'):
                ui.label('Pressure:').style(label_style)
                with ui.row().classes('items-center').style(row_style):
                    ui.icon('speed', color='primary').classes('text-5xl mr-2')
                    pressure = ui.label('1019 hPa').style('font-size: 20px;')

        # A row for buttons in two columns
        with ui.row().style(row_style):
            with ui.column():
                ui.button('Get Stable Weight', on_click=lambda: button_action('S')).style(button_style) # RGB: (50, 205, 50)
                ui.button('Get Weight Now', on_click=lambda: button_action('SI')).style(button_style)   # RGB: (50, 205, 50)
                ui.button('Get Weight Live', on_click=lambda: button_action('SIR')).style(button_style) # RGB for Orange: (255, 165, 0) or RGB for Amber: (255, 191, 0)
       
                ui.label('Command Sent:').style('font-size: 20px; padding-top:5px; font-weight: bold;')
                input_field = ui.label('').style('font-size: 20px;')

            with ui.column().style('padding-left:20px'):
                ui.button('Zero Scale', on_click=lambda: button_action('Z')).style(button_style)               # RGB: (0, 123, 255)
                ui.button('Get Stable Weight Live', on_click=lambda: button_action('SR')).style(button_style)  # RGB for Orange: (255, 165, 0) or RGB for Amber: (255, 191, 0)
                ui.button('Get Weight on Key Press', on_click=lambda: button_action('ST')).style(button_style) # RGB for Purple: (128, 0, 128) or RGB for Light Blue: (173, 216, 230)

                ui.label('Measurement:').style('font-size: 25px; padding-top:5px; font-weight: bold;')
                output_field = ui.label('').style('font-size: 40px; font-weight: bold;')

        # A section for output
        # with ui.row().style(row_style):
        #     with ui.column():
        #         ui.label('Command Sent:').style('font-size: 20px;')
        #         input_field = ui.label('').style('font-size: 20px;')
        #     with ui.column().style('padding-left:70px'):
        #         ui.label('Measurement:').style('font-size: 20px;')
        #         output_field = ui.label('').style('font-size: 30px;')

    # Plot
    with ui.column():
        with ui.matplotlib(figsize=(9, 5)).figure as fig:
            x = np.linspace(0.0, 5.0)
            y = np.cos(2 * np.pi * x) * np.exp(-x)
            ax = fig.gca()
            ax.plot(x, y, '-')
            ax.set_title('Plot placeholder', fontsize=20)
            ax.set_xlabel('X axis label', fontsize=14)
            ax.set_ylabel('Y axis label', fontsize=14)

ui.run(port=8081)  # Specify the port for the NiceGUI server
