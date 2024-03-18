function sendCommand(command) {
    console.log(`TODO: send the command ${command}`);
}

function main() {
    console.log("Ready");

    document.querySelector("#reset").onclick = (event) => {
        console.log("You pressed the RESET button!");
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
}


main();
