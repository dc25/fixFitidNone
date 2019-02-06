This program repairs QFX files that suffer from the "FITID NONE" bug that was reported by user in [this thread][1] the Quicken Community Forurm

Usage:

* Install python (tested with python 3 but python 2 and python 3 should both work) from [here][2].
* Copy fixFitidNone.py to your desktop.
* To fix a corrupted QFX file, drop it on the script you just put on your desktop.
* The QFX file will be modified to have unique FITID values where before there were invalid "NONE" values.
* A backup of the original file with the extension ".original" will be created.


Credits:

* This program is a modified version of [fixChaseFitidNone][3] by hleofxquotes@gmail.com

[1]: https://community.quicken.com/discussion/7838358/cannot-download-transactions-from-chase-bank/p1
[2]: https://www.python.org/
[3]: https://social.microsoft.com/Forums/mvpforum/en-US/f9a4fa77-fe71-4eed-a66e-c828572ab911/fixchasefitidnonepy-python-script-to-fix-up-chase-ltfitidgtnone?forum=money
