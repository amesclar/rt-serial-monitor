# Serial Monitor Specification 

## Summary

Python script that monitors two serial ports, one receiving logs from regattaTimer-Kicad Arduino application and the other receiving logs from rt-testFW Arduino test driver application.

Python script should accept command line arguments for the serial ports at 9600 baud rate with default values shown below.

Port output should be prefixed with SUT or TEST to identify the source of the log. Output should be saved to a file with a timestamp. File name should be in the format: [SUT|TEST]-YYYY-MM-DD_HH-MM-SS.log stored in a logs directory.

Default ports:

- ttyacm0 = regattaTimer-Kicad
- ttyacm1 = rt-testFW

Default baud rate:

- 9600

