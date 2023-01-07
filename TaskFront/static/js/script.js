/** help */
function log(message) {
    console.log('> ' + message)
}

/** app */
const cards = document.querySelectorAll('.card')
const dropzones = document.querySelectorAll('.dropzone')
const csrfToken = document.querySelector('meta[name=csrf-token]').getAttribute('content');


/** our cards */
cards.forEach(card => {
    card.addEventListener('dragstart', dragstart)
    card.addEventListener('drag', drag)
    card.addEventListener('dragend', dragend)
    card.addEventListener('click', showCardModal)
})

function dragstart() {
    // log('CARD: Start dragging ')
    dropzones.forEach(dropzone => dropzone.classList.add('highlight'))

    // this = card
    this.classList.add('is-dragging')
}

function drag() {
    // log('CARD: Is dragging ')
}

function dragend() {
    // log('CARD: Stop drag! ')
    dropzones.forEach(dropzone => dropzone.classList.remove('highlight'))

    // this = card
    this.classList.remove('is-dragging')
}

/** place where we will drop cards */
dropzones.forEach(dropzone => {
    dropzone.addEventListener('dragenter', dragenter)
    dropzone.addEventListener('dragover', dragover)
    dropzone.addEventListener('dragleave', dragleave)
    dropzone.addEventListener('drop', drop)
})

function dragenter() {
    // log('DROPZONE: Enter in zone ')
}

function dragover(event) {
    event.preventDefault();
    // this = dropzone
    this.classList.add('over')

    // get dragging card
    const cardBeingDragged = document.querySelector('.is-dragging')

    // this = dropzone
    this.appendChild(cardBeingDragged)
}


function dragleave() {
    log('DROPZONE: Leave ')
    // this = dropzone
    this.classList.remove('over')

}

function drop() {
    log('drop ')
    // this = dropzone
    this.classList.remove('over');

    // Get the id of the card being dragged
    const cardBeingDragged = document.querySelector('.is-dragging');
    const cardId = cardBeingDragged.dataset.cardId;

    // Get the new column that the card was dropped in
    const newColumn = this.parentNode.querySelector('h3').getAttribute('id').toLowerCase()

    // Update the column of the card on the server
    update_card_column(cardId, newColumn);
    log(`Updating card ${cardId} to column ${newColumn}`)
}

function update_card_column(card_id, new_column) {
    log(`Updating card ${card_id} to column ${new_column}`)
    // Send a PATCH request to the server to update the column of the card
    fetch(`/cards/${card_id}/update_column/${new_column}`, {
        method: 'PATCH',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
    })
        .then(response => response.json())
        .then(json => {
            // Update the card element with the new column value
            const cardElement = document.querySelector(`[data-card-id='${card_id}']`);
            cardElement.dataset.column = new_column;
        });
}



function showCardModal() {
    // Get card information
    const cardId = this.dataset.cardId;
    const cardInfoUrl = `/cards/${cardId}/`;

    // Show modal
    const cardModal = document.getElementById('cardModal');
    cardModal.style.display = 'block';

    // Get card container element
    const cardContainer = document.getElementById('cardContainer');

    // Show backdrop
    const backdrop = document.querySelector('.backdrop');
    backdrop.classList.add('show');

    // Use fetch API to get card information from the server
    fetch(cardInfoUrl)
        .then(response => response.text())
        .then(html => {
            // Insert card information into card container element
            cardContainer.innerHTML = html;

            // Close modal when close button is clicked
            const closeButton = cardContainer.querySelector('.close');
            closeButton.addEventListener('click', closeCardModal);
        });
}


function closeCardModal() {
    // Hide modal
    const cardModal = document.getElementById('cardModal');
    cardModal.style.display = 'none';

    // Hide backdrop
    const backdrop = document.querySelector('.backdrop');
    backdrop.classList.remove('show');
}
const saveButton = document.querySelector('.saveButton');
if (saveButton) {
  saveButton.addEventListener('click', saveChanges);
}
// Select the elements that should be editable
const editableElements = document.querySelectorAll('[contenteditable="true"]');

// Add the 'dblclick' event listener to each element
editableElements.forEach((element) => {
    element.addEventListener('dblclick', (event) => {
        // When the element is double clicked, make it editable
        event.target.setAttribute('contenteditable', 'true');
    });
});

function saveChanges() {
    // Get the card information from the card_detail template
    const cardId = document.querySelector('.card-detail').dataset.cardId;
    const cardName = document.querySelector('.card-title h1').textContent;
    const cardContent = document.querySelector('.card-content pre').textContent;
    const cardColumn = document.querySelector('.card-detail .column').textContent;
    // Send a PATCH request to update the card information in the database
    log(`Updating card ${cardId} with name ${cardName} and content ${cardContent}`)
    fetch(`/cards/${cardId}/saveCardInfo`, {
        method: 'PATCH',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
        },
        body: JSON.stringify({
            name: cardName,
            content: cardContent,
            column: cardColumn,
        }),
    })
        .then((response) => response.json())
        .then((data) => {
            // Update the card information in the Kanban board
            const cardElements = document.querySelectorAll(`.card[data-card-id="${cardId}"] .card-right .content`);
            cardElements.forEach((cardElement) => {
                cardElement.textContent = data.name;
            });

            
        });
}



window.addEventListener('resize', function () {
    // Update the layout of the page
    // Get the width of the window
    const windowWidth = window.innerWidth;

    // Set the width of the .boards element to be 100% of the window width
    const boards = document.querySelector('.boards');
    boards.style.width = `${windowWidth}px`;
});