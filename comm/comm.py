#!/usr/bin/env python3
import pigpio
import time
import threading

# Global parameters for GPIO communication protocol
PULSE_WIDTH = 0.0005
PIN_DATA_OUT = 18
PIN_CLK_OUT = 23
PIN_DATA_IN = 17
PIN_CLK_IN = 22


def get_binary(_stream: str) -> str:
    """Converts an ascii string to its binary representation.

        Args:
            _stream (str): The string representation of the drill.

        Returns:
            The binary representation of the drill string.
    """
    # Get the binary value for the ascii value of each character
    # in the string, and join
    return ''.join([bin(ord(c))[2:] for c in _stream])


def setup() -> pigpio.pi:
    """Initializes the GPIO pins of the Raspberry Pi to act as data and clock.

        Returns:
            The pigpio.pi object controlling the GPIO pins of the Raspberry Pi.
    """
    # Instantiate pi object
    _pi = pigpio.pi()

    # Set data and clock pins for sending data
    # to act as output
    _pi.set_mode(PIN_DATA_OUT, pigpio.OUTPUT)
    _pi.set_mode(PIN_CLK_OUT, pigpio.OUTPUT)

    # Set data and clock pins for receiving data
    # to act as input
    _pi.set_mode(PIN_DATA_IN, pigpio.INPUT)
    _pi.set_mode(PIN_CLK_IN, pigpio.INPUT)

    return _pi


def send(_pi: pigpio.pi, _stream: str) -> None:
    """Sends binary string through GPIO pins.

            Args:
                _pi (pigpio.pi): The pigpio.pi object controlling the GPIO pins.
                _stream (str): The string representation of the drill.

            Returns:
                None
    """
    # Wait for 1s to allow
    # multithread to receive data
    time.sleep(1)

    # Iterate over bits to be sent
    for bit in _stream:
        # Set clock high
        _pi.write(PIN_CLK_OUT, True)

        # Set data high or low according
        # to the bit being sent
        if bit == '1':
            _pi.write(PIN_DATA_OUT, True)
        else:
            _pi.write(PIN_DATA_OUT, False)

        # Wait for one pulse
        time.sleep(PULSE_WIDTH)
        # Set clock low
        _pi.write(PIN_CLK_OUT, False)
        # Wait for another pulse
        time.sleep(PULSE_WIDTH)


def receive(_pi: pigpio.pi, _record: list) -> None:
    """Receives binary string through GPIO pins.

                Args:
                    _pi (pigpio.pi): The pigpio.pi object controlling the GPIO pins.
                    _record (list): The binary representation of the drill.

                Returns:
                    None
    """
    # Set 3s timeout to listen for transmission
    TIMEOUT = 3
    timeout_start = time.time()

    # Listen pins for 3s
    while time.time() < timeout_start + TIMEOUT:
        # If clock is high, read the data
        if _pi.read(PIN_CLK_IN):
            _record.append(str(_pi.read(PIN_DATA_IN)))
        # Wait for one pulse
        time.sleep(PULSE_WIDTH)


def run(stream: str) -> bool:
    """Drives the image GPIO communication script.

            Args:
                stream (str): The string representation of the drill.

            Returns:
                The boolean result for whether the data sent matches the received data.
    """
    # Convert string representation to binary
    stream = get_binary(stream)
    # List for storing received datastream
    record = []

    # Setup GPIO pins
    pi = setup()

    # Use multithreading to send and receive data simultaneously
    # Note: This functionality is for testing purposes, the final
    #       design will be strictly receiving data.
    t1 = threading.Thread(target=send, args=(pi, stream,))
    t2 = threading.Thread(target=receive, args=(pi, record,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    return stream == ''.join(record)


if __name__ == '__main__':
    run('046.7827,150.9699;089.9901,114.0839;0092.913,109.1905;000099.0,000099.0;00000000')
