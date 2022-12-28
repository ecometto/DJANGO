$(document).ready(function () {

    movDate.focus()

    const getDato = async ()=>{
        let id=selectArticulo.value
        let response = await fetch(`getOneArticle/${id}`)
        let data = await response.json()
        console.log(data)
    }

    selectArticulo.addEventListener('change',()=>{
        console.log('buscando')
        datos = getDato()
        console.log(datos.articulo['id']);
    })


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

    });


});