const socket = io.connect(); // connect to websocket
var selectedAntsTable = {}; // store name for every type of ant as key, and boolean whether that ant is selected as value
const moveBeeAnimationDuration = 1.2; // seconds
const throwLeafAnimationDuration = 0.75; // seconds
const insectDieAnimationDuration = 0.6; // seconds
const insectsHurtAnimationDuration = 0.2; // seconds
const insectsActionInterval = 4; // Insects take actions every 5 seconds


function inLobby(data) {
    /* Triggered by backend once player connects to server
    Player is in lobby. Game waiting to be started. */

    let main = document.querySelector(".main-window");
    main.style.opacity = '0'; // Hide main window so lobby background image is visible
    let startButton = document.querySelector('.start-button');
    startButton.addEventListener('click', startGame); // Add event listener to Start button
}


function startGame() {
    /* Trigered when player clicks Start button
    Fecth initial data from server. Set up game grid. */

    console.log("===== Game Started! =====");

    fetch('/initialize_game', { // Send initialize_game signal to backend
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({}), // Sending empty data
    })
    .then(response => response.json())
    .then(data => { // Handling incoming data from server

        let main = document.querySelector(".main-window");
        main.style.opacity = '1'; // Make main window visible

        let body = document.getElementsByTagName("BODY")[0];
        body.style.backgroundImage = 'none'; // Remove lobby background image
        let startButton = document.querySelector('.start-button');
        startButton.remove(); // Remove start button

        formatAntButtons(data.ant_types); // Set up ant buttons according to available ant types
        formatGameGrid(data.dimensions_x, data.dimensions_y, data.wet_places); // Set up game grid
        playMusic();

        // Set calling these functions every 4 seconds and 50 milliseconds.
        setInterval(insectsTakeActions, insectsActionInterval * 1000);
        setInterval(updateStats, 50);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}


function moveBee(data) {
    /* Triggered by backend. Moves a bee */

    let animationDelay = 50;

    setTimeout(() => { // Must use timeout to enable animations
        let destination = document.getElementById(`${data.destination[0]}-${data.destination[1]}`);
        let currentTile = document.getElementById(`${data.current_pos[0]}-${data.current_pos[1]}`);
        let distance = destination.getBoundingClientRect().right - currentTile.getBoundingClientRect().right; // Calculate distance
        let beeImg = document.getElementById(`${data.bee_id}`);

        beeImg.style.transition = `transform ${moveBeeAnimationDuration}s ease-in-out`; // Translate bee in 1.5 seconds
        beeImg.style.transform = `translateX(${distance}px)`;
        beeImg.style.top = `${(destination.offsetHeight - beeImg.offsetHeight) / 2}px`; // Sets the sprite to be in the middle of the tunnel

        // Remove from current tile and add to destination
        setTimeout(() => {
            beeImg.remove();
            destination.appendChild(beeImg);
            beeImg.style.transform = `translateX(0px)`;
            beeImg.style.top = `${(destination.offsetHeight - beeImg.offsetHeight) / 2}px`;
        }, moveBeeAnimationDuration * 1000 + animationDelay);

    }, animationDelay * 2);
}


function moveBeeFromHive(data) {
    // Triggered by backend. Move a bee from hive.

    let animationDelay = 75; // milliseconds

    setTimeout(() => {
        let beeImg = document.createElement('img');
        let destination = document.getElementById(`${data.destination[0]}-${data.destination[1]}`);
        destination.appendChild(beeImg);
        beeImg.setAttribute('class', 'insect-on-tile-img');
        beeImg.setAttribute('id', data.bee_id);
        beeImg.setAttribute('src', `../static/assets/bees/${data.bee_name}.gif`)
        beeImg.style.zIndex = '5'; // Set bee image on top of tile image

        let offset = destination.getBoundingClientRect().right - beeImg.getBoundingClientRect().right;
        beeImg.style.transition = `transform ${moveBeeAnimationDuration}s ease-in-out`;
        beeImg.style.top = `${(destination.offsetHeight - beeImg.offsetHeight) / 2}px`;

        setTimeout(() => {
            beeImg.style.transform = `translateX(${offset}px)`;
            beeImg.style.top = `${(destination.offsetHeight - beeImg.offsetHeight) / 2}px`;
        }, animationDelay);


        setTimeout(() => { // Append to new parent, reset translate
            beeImg.style.transition = '';
            beeImg.style.transform = `translateX(0px)`;
            beeImg.style.left = `0px`;
        }, moveBeeAnimationDuration * 1000 + animationDelay * 2);

    }, animationDelay * 2);
}


function removeInsect(data) {
    // Triggered by backend. Remove insect from GUI. However, this is a little buggy with the feature of insects turning red upon receiving damage

    setTimeout(() => {
        let insect = document.getElementById(data.insect_id);
        let animationDelay = 50; // milliseconds
        insect.style.transition = `opacity ${insectDieAnimationDuration}s ease-out`;
        insect.style.opacity = '0';
        setTimeout(() => {
            insect.remove(); // Remove html element
        }, insectDieAnimationDuration * 1000 + animationDelay)
    }, throwLeafAnimationDuration * 1000 + insectsHurtAnimationDuration * 1000)
}


function endGame(data) {
    // Triggered by backend. End game.

    showEndGameAlert(data.antsWon)
    let mainWindow = document.querySelector('.main-window');
    mainWindow.style.transition = 'filter 2s ease-in-out';
    mainWindow.style.filter = 'brightness(35%)'; // Decrease brightness of game
}


function insectsTakeActions() {
    /* Called on interval. Ask insects to take actions */

    const timeDelay = 100; // milliseconds

    fetch('/ants_take_actions') // Triger insects_take_actions signal in backend for ants to take actions
    .then(response => response.json())
    .then(data => { // Handle data from backend
    })
    .catch(error => {
        console.error('Error:', error);
    });

    setTimeout(() => { // Leave time between ants taking action and bees taking action for the animation to play (leaf reach bee and bee turning red)
        fetch('/bees_take_actions') // Triger insects_take_actions signal in backend for bees to take actions
        .then(response => response.json())
        .then(data => {
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }, throwLeafAnimationDuration * 1000 + insectsHurtAnimationDuration * 1000 + timeDelay);
}


function updateStats() {
    /* Called on interval. Ask server for food count and turn count */

    fetch('/update_stats') // Triger update_stats signal in server
    .then(response => response.json())
    .then(data => { // Handle data from server

        setTimeout(() => { // Use time out to avoid crashes
            let food = data.food;
            let turn = data.turn;
            food_display = document.querySelector('.display-food-div');
            food_display.innerText = `Food: ${food}`;
            food_display = document.querySelector('.display-turn-div');
            food_display.innerText = `Turn: ${turn}`;
            adjustAntButtons(data.available_ants); // Update GUI on what ants are available
        }, 50);
    })

    .catch(error => {
        console.error('Error:', error);
    });
}


function reduceHealth(data) {
    /* Triggered by backend. Animates insects turning red upon receiving damage */

    const animationDelay = 100; // milliseconds

    setTimeout(() => {
        let insectImg = document.getElementById(data.insect_id);
        setTimeout(() => {
            insectImg.style.transition = '';
            insectImg.style.filter = "invert(67%) sepia(89%) saturate(7492%) hue-rotate(346deg) brightness(84%) contrast(146%)";
        }, animationDelay)
        setTimeout(() => {
            insectImg.style.transition = '';
            insectImg.style.filter = 'none';
        }, animationDelay + 1000 * insectsHurtAnimationDuration)
    }, throwLeafAnimationDuration * 1000)
}


function throwAt(data) {
    // Triggered by back end. Animates an ant throwing a leaf at a bee

    let target = document.getElementById(`${data.target_pos[0]}-${data.target_pos[1]}`);
    let thrower = document.getElementById(`${data.thrower_pos[0]}-${data.thrower_pos[1]}`);
    let distance = target.getBoundingClientRect().left - thrower.getBoundingClientRect().right;
    let offset = thrower.getBoundingClientRect().left - thrower.getBoundingClientRect().right;
    let leafImg = document.createElement('img');
    let animationDelay = 25 // milliseonds

    thrower.appendChild(leafImg);
    leafImg.setAttribute('src', '../static/assets/testLeaf.png');
    leafImg.setAttribute('class', 'leaf-on-tile-img');

    leafImg.style.transform = `translateX(${offset}px)`;
    leafImg.style.transition = `transform ${throwLeafAnimationDuration}s ease-in`;
    leafImg.style.top = `${(target.offsetHeight - leafImg.offsetHeight) / 2}px`;
    setTimeout(() => {
        leafImg.style.transform = `translateX(${distance}px)`;
        leafImg.style.top = `${(target.offsetHeight - leafImg.offsetHeight) / 2}px`;
    }, animationDelay);

    setTimeout(() => {
        leafImg.remove();
    }, animationDelay * 2 + throwLeafAnimationDuration * 1000);

}


// Handle incoming signals from server. These functions are triggered by backend.
socket.on('loadLobby', inLobby);
socket.on('moveBee', moveBee);
socket.on('moveBeeFromHive', moveBeeFromHive);
socket.on('onInsectDeath', removeInsect);
socket.on('endGame', endGame);
socket.on('throwAt', throwAt);
socket.on('reduceHealth', reduceHealth);

