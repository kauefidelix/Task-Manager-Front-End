const cards = document.querySelectorAll('.card')
const dropzones = document.querySelectorAll('.dropzone')

cards.forEach(card => {
    card.addEventListener('dragstart', dragstart)
    card.addEventListener('drag', drag)
    card.addEventListener('dragend', dragend)
})

function dragstart() {
    dropzones.forEach(dropzone => dropzone.classList.add('highlight'))
}
function drag() {
    
}
function dragend() {
    dropzones.forEach(dropzone => dropzone.classList.remove('highlight'))
}
dropzones.forEach(dropzone => {
    dropzone.addEventListener('dragenter', dragenter)
    dropzone.addEventListener('dragover', dragover)
    dropzone.addEventListener('dragleave', dragleave)
    dropzone.addEventListener('drop', drop)
})
function dragenter() {

}
function dragover() {

}
function dragleave() {

}
function drop() {

}