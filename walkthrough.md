# Walkthrough - Serial Monitor & Data Validation Updates

## Baud Rate Synchronization (2026-03-25)

The serial monitor and data validation script were updated as part of a system-wide baud rate synchronization.

### Changes Made
1. **Serial Monitor**: Updated `BAUD_RATE` to **115200** in `serial_monitor.py` to match the SUT and Test Framework.
2. **Validation Reporting**: Updated `rt_data_validation.py` to extract `iteration` and `testsequence` from test logs.
3. **Error Labels**: Mismatches are now reported with descriptive labels (e.g., `Iter 1 [5min]`) instead of flat indices.

### Verification
Verified by running `rt_data_validation.py` against existing test logs. The validator now uses a tighter **250ms** tolerance. Serial monitor jitter was reduced by decreasing the polling sleep interval to 1ms.
