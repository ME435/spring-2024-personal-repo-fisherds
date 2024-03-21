function response = sendCommand(command)
   import matlab.net.*
   import matlab.net.http.*
              
   r = RequestMessage;
   uri = URI('http://fisherds-pi5.rose-hulman.edu:5000/api/' + command);
   resp = send(r, uri);
   response = resp.Body.Data;
   fprintf("Response to %s --> %s", command, response);           
end