import matlab.net.*
import matlab.net.http.*
clc
r = RequestMessage;
uri = URI('http://137.112.212.80:5000/api/RESET');
% uri = URI('http://137.112.212.80:5000/api/MOVE 1 5');
resp = send(r,uri);
status = resp.StatusCode
response = resp.Body.Data