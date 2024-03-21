
import matlab.net.*
import matlab.net.http.*
clc
r = RequestMessage;
uri = URI('http://localhost:5000/api/RESET');
% uri = URI('http://localhost:5000/api/MOVE 1 5');
resp = send(r,uri);
status = resp.StatusCode
resp.Body
robot_response = resp.Body.Data
