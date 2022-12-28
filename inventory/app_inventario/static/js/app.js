
$(document).ready(function () {
    $('#myTable').DataTable();

    let arrayMovimientos = []
    
    $('#agregarRenglon').click(function (e) {
        e.preventDefault();
        let idArt = $('#articulo').val();
        let descArt = $('#articulo option:selected').text();

        let cant = $('#cantidad').val();
        let um = $('#umedida').val();
        arrayMovimientos.push([idArt, descArt, cant])

        let contenidoTabla = document.getElementById('tbodyMovimientos')
        contenidoTabla.innerHTML = ""        
        arrayMovimientos.forEach((element) => {
            contenidoTabla.innerHTML += `
                            <tr>
                                <td>${element[0]}</td>
                                <td>${element[1]}</td>
                                <td>${element[2]}</td>
                            </tr>
            `
        })

        console.log(contenidoTabla.innerHTML);


    });
});

document.getElementById('h4Title').addEventListener('click', () => {
    form = document.getElementById('formNewArt')
    form.classList.toggle('d-none');
    document.getElementById('divTable').classList.toggle('d-none')
})

function confirmar() {
    res = confirm('Are you sure...')
    return res
}




