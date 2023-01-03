
window.addEventListener('resize', function() {
    // Update the layout of the page
    // Get the width of the window
    const windowWidth = window.innerWidth;

    // Set the width of the .boards element to be 100% of the window width
    const boards = document.querySelector('.boards');
    boards.style.width = `${windowWidth}px`;
});

/** help */
function log(message) {
    console.log('> ' + message)
}

/** app */
const cards = document.querySelectorAll('.card')
const dropzones = document.querySelectorAll('.dropzone')


/** our cards */
cards.forEach(card => {
    card.addEventListener('dragstart', dragstart)
    card.addEventListener('drag', drag)
    card.addEventListener('dragend', dragend)
    card.addEventListener('click', showCardModal)
})

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
const closeButton = document.querySelector('.close');

closeButton.addEventListener('click', () => {
  const cardModal = document.getElementById('cardModal');
  closeCardModal();
});

function closeCardModal() {
  // Hide modal
  const cardModal = document.getElementById('cardModal');
  cardModal.style.display = 'none';

  // Hide backdrop
  const backdrop = document.querySelector('.backdrop');
  backdrop.classList.remove('show');
}

  
  


function dragstart() {
    // log('CARD: Start dragging ')
    dropzones.forEach( dropzone => dropzone.classList.add('highlight'))

    // this = card
    this.classList.add('is-dragging')
}

function drag() {
    // log('CARD: Is dragging ')
}

function dragend() {
    // log('CARD: Stop drag! ')
    dropzones.forEach( dropzone => dropzone.classList.remove('highlight'))

    // this = card
    this.classList.remove('is-dragging')
}

/** place where we will drop cards */
dropzones.forEach( dropzone => {
    dropzone.addEventListener('dragenter', dragenter)
    dropzone.addEventListener('dragover', dragover)
    dropzone.addEventListener('dragleave', dragleave)
    dropzone.addEventListener('drop', drop)
})

function dragenter() {
    // log('DROPZONE: Enter in zone ')
}

function dragover() {
    // this = dropzone
    this.classList.add('over')

    // get dragging card
    const cardBeingDragged = document.querySelector('.is-dragging')

    // this = dropzone
    this.appendChild(cardBeingDragged)
}

function dragleave() {
    // log('DROPZONE: Leave ')
    // this = dropzone
    this.classList.remove('over')

}

function drop() {
    // log('DROPZONE: dropped ')
    this.classList.remove('over')
}

