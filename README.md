# dvd

## Structure

The main files you need to run the simulation are in the top level directory (aside from SPARTA itself).

The finetuning directory contains some of my attempt to automatically change the grid based on mean free path. I'm not sure if it will run anymore but it could be useful to look at.

The processing directory contains some code to process output files and visualize with gnuplot. Use these files as references and not for your own processing. You need to start up pizza.py (https://lammps.github.io/pizza/index.html) inside python before using stats.py - I found pizza.py confusing in general though. There should be some helper scripts in the SPARTA code that export data into Tecplot/other formats, I suggest using these if possible and not pizza.py directly.

The other_dimensions directory contains some other DVD chamber layouts.

## Running

You can either run SPARTA in the command line or use the dvd.sh script to submit a job. If you are just testing things out, you can make an ijob on Rivanna and use the command line with multiple cores. Then you load open mpi and run the program according to the SPARTA docs.

If you use the dvd.sh script, make sure your SPARTA executable and all the simulation files are located in the right relative locations to the script.

You can look at the videos I made or contact me if you need more help. I went through the input files and tried to leave helpful comments as well.
