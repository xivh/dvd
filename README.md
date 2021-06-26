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

If you need the exact SPARTA file I used for some reason, it is on the spa_mpi branch.

## General Thoughts

I had a lot of trouble getting the pressure to work correctly. In theory, setting an inflow pressure below the nozzle should result in the lower chamber reaching a stable pressure gradient, and then the pressure can be measured at the outflow location and the simulation refined. In practice, getting a steady state was very difficult.

If I just set an inflow condition, the flow in the chamber was very turbulent. One way to mitigate this is to start it with particles already inside instead of as a vacuum. Another problem is that if the number of entering particles is too low, the flow is off because they are always introduced from the bottom right corner. So this can be fixed by decreasing fnum, which increases the number of simulation particles and then there are enough coming in that the effect isn't noticeable.

Here is what I suggest you do to learn how to use SPARTA and continue this project:

1. Create a closed 2D box and add particles inside of it.
2. Open a side of the box and see what happens to the particles.
3. Set some boundary condition on the open side to keep the pressure constant.
4. This is essentially the lower gas chamber in the DVD, so then look at what I did.
5. Think about whether the simulation box I made is sufficient. Right now it is a subsection of the chamber, but would expanding it to include the entire chamber be better?
7. Make the geometry of the nozzle more realistic.
8. Just like you can create particles on a boundary, you can create them on a face. So make a region around the middle of the nozzle, and you can emit metal particles out of it.

Feel free to reach out, talking in person will be more useful.
