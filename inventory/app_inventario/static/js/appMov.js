$(document).ready(function () {
    let arrayMovimientos = []    
    movDate.focus()

    const getDato = async ()=>{
        let id=selectArticulo.value
        let response = await fetch(`getOneArticle/${id}`)
        let data = await response.json()
        return data
    }

    selectArticulo.addEventListener('change', async ()=>{
        datos = await getDato()
        umedida.value = datos.umedida
        cantidad.focus()
    })


    agregarRenglon.addEventListener('click', (function (e) {
        e.preventDefault();
        let idArt = selectArticulo.options[selectArticulo.selectedIndex].value
        let descArt = selectArticulo.options[selectArticulo.selectedIndex].text
        let unid = umedida.value
        let cant = cantidad.value
        arrayMovimientos.push([idArt, descArt, unid, cant])
        
        let contenidoTabla = document.getElementById('tbodyMovimientos')
        contenidoTabla.innerHTML = ""        
        arrayMovimientos.forEach((element) => {
            contenidoTabla.innerHTML += `
                            <tr>
                                <td>${element[0]}</td>
                                <td>${element[1]}</td>
                                <td>${element[2]}</td>
                                <td>${element[3]}</td>
                            </tr>
            `
        })

    }));


});