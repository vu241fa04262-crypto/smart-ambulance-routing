let startPoint = null;
let endPoint = null;
let markers = [];

map.on('click', function(e) {

  if (!startPoint) {
    startPoint = [e.latlng.lat, e.latlng.lng];
    markers.push(L.marker(startPoint).addTo(map).bindPopup("Start").openPopup());
  }
  else if (!endPoint) {
    endPoint = [e.latlng.lat, e.latlng.lng];
    markers.push(L.marker(endPoint).addTo(map).bindPopup("Destination").openPopup());

    getRealRoute();
  }
});
function animateAmbulance(route) {

  if (ambulance) map.removeLayer(ambulance);

  let i = 0;
  ambulance = L.marker(route[0]).addTo(map).bindPopup("🚑 Ambulance");

  let move = setInterval(() => {
    if (i >= route.length) {
      clearInterval(move);
      return;
    }
    ambulance.setLatLng(route[i]);
    i++;
  }, 100);
}