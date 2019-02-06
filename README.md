This program repairs QFX files that suffer from the "FITID NONE" bug that was reported by user in [this thread][1] the Quicken Community Forurm

Usage:

* Install python (tested with python 3 but python 2 and python 3 should both work) from [here][2].
* Copy fixFitidNone.py to your desktop.
* To fix a corrupted QFX file, drop it on the script you just put on your desktop.
* The QFX file will be modified to have unique FITID values where before there were invalid "NONE" values.
* A backup of the original file with the extension ".original" will be created.

[1]: https://community.quicken.com/discussion/7838358/cannot-download-transactions-from-chase-bank/p1
[2]: https://www.python.org/
