async function sendCommand(command) {
    console.log(`Sending the command: ${command}`);

    var response = await fetch(`/api/${command}`);
    var replyText = await response.text();
    console.log(`Received: ${replyText}`);

    document.querySelector("#response").innerHTML = replyText;

    
}

function main() {
    console.log("Ready for a new day!");

    document.querySelector("#reset").onclick = (event) => {
        sendCommand("RESET");
    };
    document.querySelector("#open").onclick = (event) => {
        sendCommand("GRIPPER OPEN");
    };
    document.querySelector("#close").onclick = (event) => {
        sendCommand("GRIPPER CLOSE");
    };
    document.querySelector("#extend").onclick = (event) => {
        sendCommand("Z-AXIS EXTEND");
    };
    document.querySelector("#retract").onclick = (event) => {
        sendCommand("Z-AXIS RETRACT");
    };
    document.querySelector("#x1").onclick = (event) => {
        sendCommand("X-AXIS 1");
    };
    document.querySelector("#x2").onclick = (event) => {
        sendCommand("X-AXIS 2");
    };
    document.querySelector("#x3").onclick = (event) => {
        sendCommand("X-AXIS 3");
    };
    document.querySelector("#x4").onclick = (event) => {
        sendCommand("X-AXIS 4");
    };
    document.querySelector("#x5").onclick = (event) => {
        sendCommand("X-AXIS 5");
    };


    document.querySelector("#move").onclick = (event) => {
        var moveFromValue = document.querySelector("#moveFrom").value;
        var moveToValue = document.querySelector("#moveTo").value;
        sendCommand(`MOVE ${moveFromValue} ${moveToValue}`);
    };
    document.querySelector("#loaderStatus").onclick = (event) => {
        sendCommand("LOADER_STATUS");
    };
}

main();
