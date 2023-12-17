// blog/static/blog/js/script.js

document.addEventListener('DOMContentLoaded', function () {
    // Coordenadas fixas para São Paulo, Brasil
    var coordenadasFixas = [-23.550, -46.633];

    // Inicialize o mapa
    var mapa = L.map('mapid').setView(coordenadasFixas, 12);

    // Adicione uma camada de mapa (OpenStreetMap)
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors'
    }).addTo(mapa);

    // Adicione um marcador
    L.marker(coordenadasFixas).addTo(mapa)
        .bindPopup('Este é um marcador!').openPopup();
});
