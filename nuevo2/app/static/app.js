
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
            // console.log(data)
            lng = data.iss_position.longitude
            lat = data.iss_position.latitude
            console.log("longitud: ");
            console.log(lng);
            lngElement.innerText = lng
            latElement.innerText = lat
            if (marker){
                map.removeLayer(marker)
            }
            var marker = L.marker([lat, lng]).addTo(map)

        }
        )
}

var map = L.map('map').setView([lat, lng], 2);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    // maxZoom: 31,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);


getData()
setInterval(() => {
    getData()
}, 2000);

