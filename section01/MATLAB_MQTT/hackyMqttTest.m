function hackyMqttTest()
clc
mqClient = mqttclient("tcp://broker.hivemq.com");
mqClient.subscribe("fisherds", "Callback", @myCallback);
% mqClient.Connected

for k = 1:3
    pause(1)
    message = sprintf("My number is %d.", k);
    write(mqClient, "fisherds", message);
end
pause(1)  % To allow the last message to display

end

function myCallback(topic, message)
    topic
    message
end