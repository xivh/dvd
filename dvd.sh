#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=20
#SBATCH --time=1:00:00
#SBATCH --output=out.txt
#SBATCH --partition=standard
#SBATCH -A wadleygroup

srun ../spa_mpi < in.dvd
