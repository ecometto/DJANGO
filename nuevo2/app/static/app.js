
//definiendo variables:
const lngElement = document.getElementById('lng');
const latElement = document.getElementById('lat');
var lng = 0;
var lat = 0;

const url = "http://api.open-notify.org/iss-now.json";

function getData() {
    fetch(url)
        .then(res => res.json())
        .then(data => {
            console.log(data)
            if (newMarker) {
                map.removeLayer(newMarker)
                oldMarker = L.marker([(lat), (lng)], { opacity: 0.1, icon: grayCircle }).addTo(map);
                oldMarker.bindPopup(`Latitud: ${lat}, longitud: ${lng} <br>${fecha}`)
            }
            lng = data.iss_position.longitude
            lat = data.iss_position.latitude
            lngElement.innerText = lng
            latElement.innerText = lat

            fechaTT = new Date(data.timestamp*1000)
            fecha=fechaTT.getDate()+"/"+fechaTT.getMonth()+"/"+fechaTT.getFullYear()+" - "+fechaTT.getHours()+":"+fechaTT.getMinutes()+":"+fechaTT.getSeconds()
            newMarker = L.marker([lat, lng], { opacity: 1, title: "International Spacial Station (ISS) \nCurrent Position" }).addTo(map)
            newMarker.bindPopup(`Latitud: ${lat}, longitud: ${lng} \n${fechaTT}`)
            // marker.bindPopup(popupContent).openPopup();
        }
        )
}

var map = L.map('map').setView([lat, lng], 2);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    // maxZoom: 31,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);
var oldMarker = null
var newMarker = null


var grayCircle = L.icon({
    iconUrl: "/static/img/circulo.png",
    iconSize: [20, 20], // size of the icon
});

getData()
setInterval(() => {
    getData()
}, 2000);

