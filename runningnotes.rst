===================================
Running notes for Neil's Greenhouse
===================================

2025-12-23
==========

Just discovered github CLI. Apparently this is what I should use. read up on it and use.

Need to rename. Do it safe by repeating the process.

----------


Starting to use uv for development. 

Steps

1. Install uv (if you haven't already)::

    curl -LsSf https://astral.sh/uv/install.sh | sh

2. Clone your repository locally (if not already done)::

    git clone https://github.com/your-username/your-repo.git
    cd your-repo

3. Initialize uv for your project

Run this in the root of your repository::

    uv init

see https://x.com/i/grok?conversation=2002198771770290596 for next steps and details

Also use::

    uv add --dev -r requirements_dev.txt


What to call the package::

    fishieye
    fish_calib
    fisheye_calibration
    calibratefisheye
    calibrate_fisheye
    calibfish
    fishcalib
    eyecalib
    f_calib

Final -> calibrate_fisheye

2025-12-11
==========

trans7.py is the only transparecy where something show thru underneath. Use this method to highlight the uncalibrated areas of the sunpath.

Big picture - on what to do next
--------------------------------

Neil lens sunpath

- mark the uncalibrated parts with a color - DONE Circle15.py
- calibrate the uncalibratedparts - later
- automate the calinration - later

placing photo

- place photo with tranceparency
- scale photo
- rotate photo


2025-12-10
==========

- do pleijel projection
- do lens projection

2025-12-07
==========

- match concentric circles on radains sunpath - DONE
- draw a couple of datetimes and match it with the radians output.
    - start using pyephem
- draw full sunpath on this.

- draw concentric circles on calibratied sunpath
