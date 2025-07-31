# Warning:
This script has not been tested on linux, so you may have to change the "libcmdctrl" to be able to run the cmd cursor modefier on linux
Also not sure if psutil works on linux

### For further modifications you can do the following:
- `psutil.net_io_connections().items()` also has `errin` and `errout` to check number of errors while sending or recieving data `follow psutil site for more` [documnetaion](https://psutil.readthedocs.io/en/latest/)
- The previous connection module also have the `dropin` and `dropout` functions to check the total number of dropped packets
- The Programm has not been converted to an exutable which can be done using built-in library `pyinstaller` or by installing `auto-py-to-exe`
- `Pandas` Also can be used to neatly format the output
- Also the same script can be used with `PyQt5`, `PyQt6`, `Tkinter` or any `gui` framework
- Any more modification can be done after reading the code `it's simple`

## For Windows:
This script is ready to be run on windows, more modification can be added to suit the user

## For Linux:
The script has not been tested on linux

## For Mac:
Same as linux

This script is not genuin, there can be another tools like this online, but integrity counts

<ins>More documentaion, or code modification can be added in the future</ins>
