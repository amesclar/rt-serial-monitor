# References

- [References](#references)
  - [Serial Monitor](#serial-monitor)
    - [Run](#run)
  - [Python](#python)
    - [Install Dependencies](#install-dependencies)
    - [Capture Dependencies](#capture-dependencies)
    - [Activate Virtual Environment](#activate-virtual-environment)
    - [Deactivate Virtual Environment](#deactivate-virtual-environment)
    - [Create Virtual Environment](#create-virtual-environment)
    - [Install venv](#install-venv)
    - [Install pip](#install-pip)


## Serial Monitor

### Run

```bash
python3 serial-monitor.py --sut-port /dev/ttyACM0 --test-port /dev/ttyACM1
```


## Python

### Install Dependencies

```bash
pip install --no-cache-dir -r requirements.txt
```

### Capture Dependencies

```bash
pip freeze > requirements.txt
```

### Activate Virtual Environment

```bash
source venv/bin/activate
```

### Deactivate Virtual Environment

```bash
deactivate
```

### Create Virtual Environment

```bash
python3 -m venv venv
```

### Install venv

```bash
sudo apt update
sudo apt install python3-venv
```

### Install pip

```bash
sudo apt update
sudo apt install python3-pip
```
