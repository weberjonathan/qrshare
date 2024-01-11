# QR Share

<img src="embed.jpg" alt="logo" width="100ppx" />

Command line tool to quickly create and show a QR code for a given text input. Included is the launch script `qrshare.bat` (Windows) which can be placed on `PATH` to launch from anywhere.

```
usage: qrshare [-h] [-e [PATH]] [--debug] [-v] data

Receives text and displays it as a QR code.

positional arguments:
  data                  the text encoded in the QR code, e. g. 'https://www.qrcode.com'.

options:
  -h, --help            show this help message and exit
  -e [PATH], --embed [PATH]
                        embed a custom image in the centre of the QR code by specifying a path or use a default image by omitting the positional argument
  --debug               enables debug messages
  -v, --version         show program's version number and exit
```

## Setup

### Python

- `pip install qrcode`.

### Launch script

The directory structure for the launch script must be created manually. The expected structure is:

```
| bin/
   | qrshare.bat
| qrshare/
   | embed.jpg
   | qrshare.py
```