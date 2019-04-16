# fccm-ttm-experiments-vlab
The way to use this repository is like this.
1. Configure FPGA environment.  
`source vlab.sh`  
2. Compiles the opencl file ttm-drain.cl into .aocx bitstream.  
`python run-drain.py`  
Once you run this command you will not see any compiler messages on your screen since it runs the aoc compiler in background. Compiler messages are dumped in build.log file.
You can use this command to see the status of the process:  
`qstat -u $USER`  
The compile process will take a long time (about 12 hours).  
3. Compile the host file ttm-host.cpp.  
`python ttm-host.py`  
5. When you got the .aocx file, you can run the host code. First, Open the interactive shell on FPGA compute node.  
`qsub-fpga`  
6. Then, configure a new FPGA design onto your board.  
`aocl program acl0 filename.aocx`  
7. Finally, run the host code which programs the FPGA with the .aocx file.  
`./device-ttm`  
After running, you can get the performace report in dir_name/acl_quartus_report.txt. The dir_name is same with the file name of .aocx file.   
