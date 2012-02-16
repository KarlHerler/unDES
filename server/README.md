#Server

Location: http://ec2.karlherler.com:5000/


##Spec

pulled with some minor modifications from: https://www.facebook.com/groups/320714721299206/doc/320789261291752/

 *  HTTP key distribution and validation service
 *  Generates and distributes key ranges
 *  Keeps track of the progress and current active users
 *  Validates received keys if a client responds with a decryption key
 *  Python based implementation (?)
 *  EC2 / Linode hosting option
 *  Should support master-master replication with fallover, in order to avoid the risk of loss of progress

 
##Server communication spec


 <table>
  <tr>
	<th>Route</th>
	<th>Verb</th>
	<th>Action</th>
	<th>Status</th>
 </tr>
  <tr>
    <td>/</td>
    <td>GET</td>
    <td>Loads the server GUI for webbrowsers</td>
    <td>Responds, unimplemented</td>
  </tr>
  <tr>
    <td>/key</td>
    <td>GET</td>
    <td>Returns a keyrange startpoint and size</td>
    <td>Implemented</td>
  </tr>
  <tr>
    <td>/key</td>
    <td>POST</td>
    <td>Reads statusreport (`range=<range>&key=<key>&found=<true/false>`), Returns a keyrange, shortcut for POST /report, GET /key </td>
    <td>Implemented, silent</td>
  </tr>
  <tr>
    <td>/report</td>
    <td>POST</td>
    <td>Reads statusreport as contained in POSTDATA (`range=<range>&key=<key>&found=<true/false>`)</td>
    <td>Implemented</td>
  </tr>
 </table>



##Running the server

Requirements:

 *  Python (2.6+)
 *  virtualenv (`easy_install virualenv`)
 *  Flask (`pip install Flask`)

Running:
```
python undes.py
```


