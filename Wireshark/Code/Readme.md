# Code

## Capturing

### Requirements

* Kali Live on bootable usb stick

    * Kali Live (https://www.kali.org/downloads/)

    * Tool to easily create bootable usb stick (https://etcher.io/)

* Storage partition on bootable usb stick

    * After creating the Kali Live bootable usb stick make sure you create a data partition to store your captures on (you cannot store on the system partition of Kali Live), this can be done in windows. Make sure you create a FAT32 partition.

* Git repo code copied onto the storage partition.

### Running

* Make sure any existing wifi management daemon is not running by executing:

          	airmon-ng check kill

* Put your wifi adapter into monitoring mode

          	airmon-ng start wlan0

* cd into the Git repo code folder/Code folder

* Start the channel hopper

          	sh ./bash/chanhop.sh -i wlan0mon -b IEEE80211BINTL

* Open Wireshark and start capturing on wlan0mon interface \* Note: don't turn on monitoring from within Wireshark this will interfere with airmon.

* When finished store the capture as a .pcapng file onto the Storage partition

## Parsing

### Requirements

* python 3 (https://www.python.org/downloads/)
* pyshark (pip install pyshark)

### Running

* Put the .pcapng file into the captures directory

* Adjust 2 parser parameters if needed at the top of the parser file (process_captures.py), default settings should work fine.

* run the parser

          	python process_captures.py
