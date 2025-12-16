- [rt-serial-monitor](#rt-serial-monitor)
  - [Usage](#usage)
  - [Notes](#notes)


# rt-serial-monitor

serial monitor to capture regatta timer and test framework logs

## Usage

```bash
./serial-monitor.py --sut-port /dev/ttyACM0 --test-port /dev/ttyACM1
```

## Notes  

1. Docker is not used because serial ports are not accessible from within the container

