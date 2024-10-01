#!/bin/sh 
### General options 
### -- specify queue -- 
#BSUB -q hpc
### -- set the job Name -- 
#BSUB -J Elastix_job
### -- ask for number of cores (default: 1) -- 
#BSUB -n 4 
### -- specify that the cores must be on the same host -- 
#BSUB -R "span[hosts=1]"
### -- specify that we need 4GB of memory per core/slot -- 
#BSUB -R "rusage[mem=16GB]"
### -- specify that we want the job to get killed if it exceeds 5 GB per core/slot -- 
#BSUB -M 5GB
### -- set walltime limit: hh:mm -- 
#BSUB -W 24:00 
### -- set the email address -- 
# please uncomment the following line and put in your e-mail address,
# if you want to receive e-mail notifications on a non-default address
##BSUB -u awias@dtu.dk
### -- send notification at start -- 
#BSUB -B 
### -- send notification at completion -- 
#BSUB -N 
### -- Specify the output and error file. %J is the job-id -- 
### -- -o and -e mean append, -oo and -eo mean overwrite -- 
#BSUB -o Output_%J.out 
#BSUB -e Output_%J.err 

# here follow the commands you want to execute with input.in as the input file
export LD_LIBRARY_PATH=/dtu/3d-imaging-center/QIM/elastix/elastix-4.9.0/lib/:$LD_LIBRARY_PATH

/dtu/3d-imaging-center/QIM/elastix/elastix-4.9.0/bin/elastix -f /work3/awias/MicroCracks/fixed_cropped.nii -m /work3/awias/MicroCracks/moved_cropped.nii -fMask /work3/awias/MicroCracks/fixed_cropped_mask.nii -mMask /work3/awias/MicroCracks/moved_cropped_mask.nii -out /work3/awias/MicroCracks/Outputs -p /work3/awias/MicroCracks/parameterFile.txt
