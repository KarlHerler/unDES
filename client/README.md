#Client
pulled with some minor modifications from: https://www.facebook.com/groups/320714721299206/doc/320789261291752/

 *  Connect to the key distribution centre and request a key range. Requests are done using HTTP
 *  BruteForce the key range and report success / failure as HTTP requests (either alone or in conjunction with key requests)
 *  Must be compiled for different operating systems
 *  Must *try* not to overload the host machine (use only free resources)
 *  DES implementation in C (or OCaml) for speed
 *  Optional CUDA/OpenCL support
 *  Client could be a C/C++/Java implementation
