

document.getElementById('h4Title').addEventListener('click', () => {
    form = document.getElementById('formNewArt')
    form.classList.toggle('d-none');
    document.getElementById('divTable').classList.toggle('d-none')
})

function confirmar() {
    res = confirm('Are you sure...')
    return res
}




