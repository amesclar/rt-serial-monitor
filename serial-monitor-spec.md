# Serial Monitor Specification 

## Summary

Python script that monitors two serial ports, one receiving logs from regattaTimer-Kicad Arduino application (SUT) and the other receiving logs from rt-testFW Arduino test driver application (TEST).

Python script should accept command line arguments for the serial ports at 9600 baud rate with default values shown below.

Port output should be prefixed with SUT or TEST to identify the source of the log. Output should be saved to a file with a timestamp. File name should be in the format: [SUT|TEST]-YYYY-MM-DD_HH-MM-SS.log stored in a logs directory.

Log messages should be timestamped using the following format: YYYY-MM-DD_HH-MM-SS.MS and the datetime function should be used to generate the timestamp; e.g. 

```f"{datetime.now().isoformat(sep=' ', timespec='milliseconds')}"```

Default ports:

- ttyacm0 = regattaTimer-Kicad
- ttyacm1 = rt-testFW

Default baud rate:

- 9600

