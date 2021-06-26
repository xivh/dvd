# stats file format
# Step CPU WALL Np Natt Ncoll Maxlevel Nchild
set term png
set key autotitle columnheader
set output "cpu time.png"
set title "cpu time vs timestep"
plot "out.dat" u 1:2
unset output
set output "wall time.png"
set title "wall time vs timestep"
plot "out.dat" u 1:3
unset output
set output "particles.png"
set title "particles vs timestep"
plot "out.dat" u 1:4
unset output
set output "collisions.png"
set title "number of attempted and performed collisions vs timestep"
plot "out.dat" u 1:5, "out.dat" u 1:6
unset output
set output "max level and children.png"
set title "max level and children vs timestep"
set y2tics nomirror
plot "out.dat" u 1:7, "out.dat" u 1:8 axes x1y2
unset output
