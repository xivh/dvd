#!/bin/bash
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=20
#SBATCH --time=0:30:00
#SBATCH --output=out.txt
#SBATCH --partition=parallel
#SBATCH -A wadleygroup

srun ../spa_mpi < speedtest.dvd
