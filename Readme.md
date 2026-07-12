# CountDown.py

A simple, interactive command-line countdown timer written in Python. This application allows users to input a specific duration in hours, minutes, or seconds, and displays a dynamic, real-time countdown clock directly in the terminal.

## Features

- **Multiple Time Units:** Choose to input time in Hours, Minutes, or Seconds.
- **Real-Time Update:** Displays the remaining time using an in-place updating format (`HH : MM : SS`).
- **Error Handling:** Robust validation to handle invalid inputs or general exceptions gracefully.
- **Looping Menu:** Stay in the application to run multiple countdowns, or exit when finished.

## Code Overview

The project is structured around a central `TimeClass` that handles all time conversions and countdown logic:

- `PedirNumero()`: Asks the user for a numeric input and handles text entry errors (`ValueError`).
- `Horas(horas)` / `Minutos(Minutos)`: Converts the given time units into seconds.
- `cronometro_atras(segundos)`: The core loop that calculates hours, minutes, and seconds remaining using `divmod()`, formatting it dynamically.
- `Usuario()`: The interactive submenu for selecting time units.

## Requirements

- Python 3.x

## How to Run

1. Clone or download `CountDawn.py` to your local machine.
2. Open your terminal or command prompt.
3. Navigate to the directory containing the file and execute:

```bash
python CountDawn.py
```

## Usage Example

Upon running the script, you will be greeted with the main menu:

```text
============================================================
1.Iniciar
2.Salir
Elige: 1


============================================================
desea ingrsar la cantidad en
1.horas
2.Minutos
3.segundos
Elige: 3
Ingrese la cantidad de tiempo: 10
Tiempo restante: 00 : 00 : 10
```

When the timer reaches zero, it will print `!!Fin del Tiempo!!` and return to the main menu.
