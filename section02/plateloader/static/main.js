function sendCommand(command) {
    console.log(`TODO: Send the command: ${command}`);
}

function main() {
    console.log("Ready");

    document.querySelector("#reset").onclick = (event) => {
        console.log("You clicked RESET!");
        sendCommand("RESET");
    };
}

main();
