#Server
pulled with some minor modifications from: https://www.facebook.com/groups/320714721299206/doc/320789261291752/

 *  HTTP key distribution and validation service
 *  Generates and distributes key ranges
 *  Keeps track of the progress and current active users
 *  Validates received keys if a client responds with a decryption key
 *  Python based implementation (?)
 *  EC2 / Linode hosting option
 *  Should support master-master replication with fallover, in order to avoid the risk of loss of progress
