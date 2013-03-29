PSSOptimisation
===============

This application is aimed at students of Cologne University of Applied Sciences in Germany. It tries to deliver features to PSSO users which the original PSSO doesn't offer.
Currently a big part of the code and all interface text is only available in german.

Features:
- either insert your PSSO access data or download the page with your grades and feed it to the program
- current sum of credit points (PSSO often lags behind here)
- current grade point average (PSSO also often lags here)
- number of grades

Potential features:
- Notifications on new grades
- Visualisations of grades and your study progress
- <insert your suggestions here>


How to run
==========
If you're a linux- or windows user, you can run the standalone programs from the dist directory. There is no mac executable yet. Let me know if you're feeling like meeting and letting me use your mac for a few minutes ;-)


Dependencies
============
The executables from the dist directory are all self-contained. You'll need nothing else for running them.
Still, if you want to modify and run the program afterwards, you'll need the following software including the respective dependencies:
- Python 2
- Beautiful Soup 4
- PyQt4
- Pyinstaller (only if you want to create a standalone executable)
