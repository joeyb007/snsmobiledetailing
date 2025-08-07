let index = 0;
const images = document.querySelectorAll('.carouselImage');
const track = document.getElementById('carouselTrack');

setInterval(() => {
  index = (index + 1) % images.length;
  track.style.transform = `translateX(-${index * 100}%)`;
}, 3000); 