# Testing

---

This directory contains the testing resources and scripts.

### drills.txt

The `drills.txt` file contains 100 drill representation strings. These drills were randomly generated, then filtered by
their properties (e.g. trajectory angles, pocket alignment, ball distances etc.).

These strings are used to test the actual functional scripts.

### test.py

The `test.py` Python script automatically tests the functional scripts on "user-input" number of drills.

Current tests include:

- `comm_accuracy()`: Tests the accuracy of GPIO communication carried out in the `comm.py` script using simulated input.
- `DIS_runtime()`: Measures runtime of the execution of the `DIS.py` image generation script.