# GPIO Communication Protocol Script

---

### Table of Contents

- Description
- Methodology
- Functions
    - `get_binary()`
    - `setup()`
    - `send()`
    - `receive()`
- Dependencies

### Description

`comm.py` is a Python script handling the communications through GPIO ports of a Raspberry Pi. The purpose of this
script is to carry out communications between the microcontroller and Raspberry Pi without using UART serial
communications, due to the unavailability of pins.

Note: The current version also handles simulated input.

### Methodology

The script follows the same setup procedure for both sending and receiving operations. This setup starts by taking a
string representation of a drill, and converting it to a bitstream, still in string format. This conversion is then
followed by the configuration of GPIO pins. Both sending and receiving functionalities use 2 GPIO pins, one to serve as
data transmission, the other as clock.

Once the GPIO pins are set up, the script creates two threads, one for each functionality (i.e. send and receive). This
multithreading is for the purposes of testing the receiving functionality, where sending data only acts as simulated
input for demonstration and testing. The final script will only listen and receive data from GPIO pins.

Data transmission is a simple protocol, where at each clock pulse, one bit of information is sent to the receiver. The
receiver reads the data pin state at each clock pulse, recording the result to obtain the full transmission. The
communication takes 3 seconds per string.

### Functions

#### get_binary( )

The `get_binary()` function takes the string representation of a drill, and converts it to a binary bitstream.

For example, the following string:

```python
'072.4188,166.2855;031.2016,035.1107;027.4153,030.8499;000.0,000.0;00120025'
```

is converted to the stream below.

```python
'110000110100110110101110110111111000110010110111101100110001110101110000101110111001110110111001111001111011110000111000111001101110111001111001110000110001101100110001110001110100101110110000111000110011111001111011110000110000111001110010101110111001110001110011101100110001110000111001101110110001111001110000110101111011110000110000110000110000111001111001101110110000101100110000110000110000110000111001111001101110110000111011110000110000110000110000110000110000110000110000'
```

#### setup( )

The `setup()` function simply configures the selected GPIO pins to act as either input or output pins.

#### send( )

The `send()` function sends a bitstream using the determined output pins. As described in the protocol, the clock signal
is set high and then low every clock pulse. The data signal is set to the bit being sent at every clock high.

#### receive( )

The `receive()` function is the correspondant of the `send()` function, receiving a bitstream using the determined input
pins. This function reads and stores the state of the data pin at every clock high.

### Dependencies

This script is written in `Python3`, and uses the `pigpio`, `time` and `threading` package contents, imported as
follows:

```python
import pigpio
import time
import threading
```

The `pigpio` package requires the following command to be executed on the Raspberry Pi to run the daemon which allows
the package to function properly:

```bash
sudo pigpiod
```

This requirement will be satisfied by the launch script of the Raspberry Pi which executes upon powering.