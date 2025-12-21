import serial
import threading
import sys
import time 
import argparse
import os

from datetime import datetime

# Configuration
BAUD_RATE = 9600

def get_log_filename(prefix, log_dir):
    """Generates the log file path with the format: [SUT|TEST]-YYYY-MM-DD_HH-MM-SS.log"""
    timestamp = f"[{datetime.now().isoformat(sep=' ', timespec='seconds')}]"
    filename = f"{prefix}-{timestamp}.log"
    return os.path.join(log_dir, filename)

def read_from_port(port_name, prefix, log_dir):
    """
    Continuously parses lines from a serial port, prints them with a prefix,
    and logs output to a unique timestamped file.
    """
    # Generate the unique, timestamped log file path
    log_file_path = get_log_filename(prefix, log_dir)

    try:
        # Open the serial port
        ser = serial.Serial(port_name, BAUD_RATE, timeout=1)
        print(f"Connected to {port_name} as {prefix}. Logging to {log_file_path}")

        # Open the log file in write mode ('w') since we want a fresh log per run
        with open(log_file_path, 'w') as log_file:
            while True:
                try:
                    if ser.in_waiting > 0:
                        # Read and decode the line
                        line = ser.readline().decode('utf-8', errors='replace').rstrip()
                        
                        if line:
                            # Timestamp for the log line itself
                            line_timestamp = f"[{datetime.now().isoformat(sep=' ', timespec='milliseconds')}]"
                            
                            console_output = f"[{prefix}] {line}"
                            log_output = f"{line_timestamp} {line}"

                            # 1. Print to console
                            print(console_output)
                            sys.stdout.flush() 

                            # 2. Write to log file
                            log_file.write(log_output + '\n')
                            log_file.flush() # Ensure data is written to disk immediately
                    else:
                         time.sleep(0.01) # Prevent CPU hogging
                except OSError as e:
                    print(f"Error reading {port_name}: {e}")
                    break
                except serial.SerialException as e:
                    print(f"Lost connection to {port_name}: {e}")
                    break

    except serial.SerialException as e:
        print(f"Could not open {port_name}: {e}")
    except IOError as e:
        print(f"Error opening log file {log_file_path}: {e}")


if __name__ == "__main__":
    # Define and parse command line arguments
    parser = argparse.ArgumentParser(description="Multi-port Serial Monitor.")
    parser.add_argument('--test-port', 
                        default='/dev/ttyACM0', 
                        help='Serial port for the Test Harness. Default: /dev/ttyACM0')
    parser.add_argument('--sut-port', 
                        default='/dev/ttyACM1', 
                        help='Serial port for the System Under Test (SUT). Default: /dev/ttyACM1')
    parser.add_argument('--log-dir',
                        default='logs',
                        help='Directory to store log files. Default: logs')
    args = parser.parse_args()

    # --- Setup Logging Directory ---
    LOG_DIR = args.log_dir
    try:
        os.makedirs(LOG_DIR, exist_ok=True)
        print(f"Log directory created/verified: {LOG_DIR}")
    except OSError as e:
        print(f"Error creating log directory {LOG_DIR}: {e}")
        sys.exit(1)
    
    # --- Port Configuration ---
    SUT_PORT = args.sut_port
    TEST_PORT = args.test_port

    print("Starting Serial Monitor...")
    print(f"SUT Port:  {SUT_PORT}")
    print(f"Test Port: {TEST_PORT}")
    print(f"Baud Rate: {BAUD_RATE}")

    # Create threads for each port, passing the log_dir
    # Note: Filenames are generated inside the thread function to ensure unique timestamps 
    # if the threads start slightly apart, although they are designed to start near-simultaneously.
    t1 = threading.Thread(target=read_from_port, args=(SUT_PORT, "SUT", LOG_DIR), daemon=True)
    t2 = threading.Thread(target=read_from_port, args=(TEST_PORT, "TEST", LOG_DIR), daemon=True)

    t1.start()
    t2.start()

    # Keep main thread alive
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping monitor...")