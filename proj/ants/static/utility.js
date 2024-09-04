function formatAntButtons(antTypes) {
    // Create buttons for each type of ant

    let antSection = document.querySelector('.ants-section');
    for (i = 0; i < antTypes.length; i++) {
        let antButton = document.createElement('button');
        antButton.setAttribute('class', `ant-btn`);
        antButton.setAttribute('id', antTypes[i]);
        antButton.style.backgroundImage = `url('../static/assets/ants/${antTypes[i]}.gif')`;
        antSection.appendChild(antButton);
        selectedAntsTable[antTypes[i]] = false; // Add key value pairs to table (key = ant name, val = whether it's selected)
    }
    addListenerToAnts(); // Add event listener to ant button
}


function formatGameGrid(rows, cols, wetPlaces) {
    let gameSectionStyle = document.querySelector(".game-section").style;
    let maxWidth = 12; // Maximun tunnel length = 12

    if (0 < cols <= maxWidth) {
        // Determine space occupied by grids vs hive according to num of cols
        gameSectionStyle.gridTemplateColumns = `${cols / maxWidth}fr ${(maxWidth - cols) / maxWidth}fr`;
    } else {
        console.log("===== ERROR: number of columns not supported =====");
    }

    addRowsToGrid(rows); // Add rows to grid
    for (i = 0; i < rows; i++) {
        createButtonsForRow(cols, i, wetPlaces); // Add buttons to row
    }
    formatHive();
    addListenerToTile(); // Add event listener to tile
}


function addRowsToGrid(rows) {
    /* Add rows to game grid */

    let s = '';
    let tunnelGrid = document.querySelector(".tunnel-grid");

    for (i = 0; i < rows; i++){
        if (i === rows - 1) {
            s += `1fr`;
        } else {
            s += `1fr `;
        }
        let row = document.createElement('div');
        row.setAttribute('class', `tunnel-row-${i}`);
        row.style.display = 'flex'; // Make every row a flex box
        row.style.justifyContent = 'space-between';
        tunnelGrid.appendChild(row);
    }

    tunnelGrid.style.gridTemplateRows = s; // Set tunnelGrid as CSS grid with correct number of fr
}


function createButtonsForRow(buttonCount, row, wetPlaces) {
    // Add buttons (tiles) for given row

    for (let i = 0; i < buttonCount; i ++) {
        let button = document.createElement('button');
        button.setAttribute('class', `tile-btn`);
        button.setAttribute('id', `${row}-${i}`);
        let image = document.createElement('img');
        image.setAttribute('src', `../static/assets/tiles/${i % 3}.png`);

        for (let j = 0; j < wetPlaces.length; j++) { // Check every wet place to see if is current place
            if (wetPlaces[j][0] === row && wetPlaces[j][1] === i) {
                image.setAttribute('src', `../static/assets/tiles/wet.png`); // Set src as wet place
                break;
            }
        }

        image.setAttribute('class', `tile-img`);
        button.appendChild(image);
        document.querySelector(`.tunnel-row-${row}`).appendChild(button);
    }
}


function formatHive() {
    // Set up and add image to bee hive
    hive = document.querySelector(".beehive");
    hive.style.position = 'relative';
    hive.style.overflow = 'hideen';
    image = document.createElement('img');
    image.setAttribute('src', `../static/assets/fog.jpg`);
    image.style.width = '100%';
    image.style.height = '100%';
    image.style.objectFit = 'cover';
    image.style.opacity = '85%';
    hive.appendChild(image);
}


function makeAntSelector(antName) {
    /* Returns an antSelector func, which will be called when button pressed */

    function antSelector() {
        for (let ant in selectedAntsTable) {
            /* Loop thru every ant type.
            If type is selected, reflect in table and change border color.
            Reset all other types in table and color */
            let antButton = document.getElementById(ant);
            if (ant === antName) {
                selectedAntsTable[ant] = true;
                antButton.style.borderWidth = '5px';
                antButton.style.borderColor = 'rgba(50, 20, 200, 0.8)';

            } else {
                selectedAntsTable[ant] = false;
                antButton.style.borderWidth = '2px';
                antButton.style.borderColor = 'rgba(54, 57, 235, 0.2)';
            }
        }
    }

    return antSelector;
}


function addListenerToAnts() {
    /* Add event listener to every ant button */

    let buttons = document.getElementsByClassName('ant-btn');
    for (i = 0; i < buttons.length; i++) {
        buttons[i].addEventListener('click', makeAntSelector(buttons[i].id));
    }
}


function getSelectedAnt() {
    // Return selected ant from table, or undefined if no ants selected
    for (let ant in selectedAntsTable){
        if (selectedAntsTable[ant]){
            return ant;
        }
    }
}


function makeOnClickTile(buttonID) {
    /* Returns a func, which is called when tile button is clicked */

    function onClickTile() {

        // Check if an ant is selected
        selectedAnt = getSelectedAnt();
        if (selectedAnt == undefined){
            return;
        }

        // Prepare data to sent to server (which button and what ant)
        const data = {
            pos: buttonID,
            ant: selectedAnt
        };

        fetch('/deploy_ants', { // Send an AJAX request to Flask server by signaling deploy_ants
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        })
        .then(response => response.json())
        .then(data => { // Handle incoming data from server
            deployed = data.deployed;
            if (deployed){ // Successfuly deployed
                placeAnt(selectedAnt, buttonID, data.insect_id);
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });

    }

    return onClickTile;
}


function addListenerToTile() {
    // Add event listener to every tile button
    let buttons = document.getElementsByClassName('tile-btn');
    for (i = 0; i < buttons.length; i++) {
        buttons[i].addEventListener('click', makeOnClickTile(buttons[i].id));
    }
}


function placeAnt(antName, place, ant_id) {
    // Place an ant on GUI
    let image = document.createElement('img');
    let button = document.getElementById(place);

    image.setAttribute('class', 'insect-on-tile-img');
    image.setAttribute('src', `../static/assets/ants/${antName}.gif`);
    image.setAttribute('id', ant_id);
    button.appendChild(image);

    // Center the ant at the botton
    image.style.top = `50%`;
    image.style.left = `50%`;
    image.style.transform = 'translate(-50%, -50%)';
}


function adjustAntButtons(availableAnts) {
    // Increase brightness of available ants (enough food to de deployed), and decrease unavailable ants
    let antButtons = document.getElementsByClassName('ant-btn');
    for (i = 0; i < antButtons.length; i++) {
        let button = antButtons[i];
        if (availableAnts.includes(button.id)) {
            button.style.filter = 'brightness(100%)';
        } else {
            button.style.filter = 'brightness(35%)';
        }
    }
}


function showEndGameAlert(result) {
    // Display alert message. Called when game ends.
    let body = document.body;
    let alert = document.createElement('alert');
    alert.style.opacity = '0'; // Set initial opacity to 0
    body.appendChild(alert);
    alert.setAttribute('class', 'alert');
    let text = document.createElement('p');
    alert.appendChild(text);

    if (result) { // Ants won
        text.innerText = 'You Won!';
        alert.style.backgroundColor = 'rgba(30, 200, 50, 1)';
    } else {
        text.innerText = 'You Lost!';
        alert.style.backgroundColor = 'rgba(190, 40, 50, 1)';
    }

    alert.style.transition = 'opacity 2s ease-in-out';
    setTimeout(() => { // Need time out for animation
        alert.style.opacity = '0.9'; // Change alert opacity to 90% over 2 seconds
    }, 50);
}


function playMusic() {
    // Play music
    let audio = document.getElementById('backgroundmusic');
    audio.play();
}


