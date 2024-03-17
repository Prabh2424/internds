// Variables to keep track of carousel state
let currentIndex = 0;
const items = document.querySelectorAll('.classic-item');
const totalItems = items.length;
const carouselInner = document.querySelector('.classic-inner');
const itemWidth = items[0].offsetWidth; // Width of each carousel item
let isPaused = false; // Flag to track if carousel is paused
let intervalId; // Declaring intervalId as a let variable

// Clone the initial set of images and append them to the end
items.forEach(item => {
  const clone = item.cloneNode(true);
  carouselInner.appendChild(clone);
});

// Function to move carousel to the next slide
function moveToNextSlide() {
  if (!isPaused) {
    currentIndex++;
    updateCarousel();
  }
}

// Function to update carousel position
function updateCarousel() {
  const newPosition = -currentIndex * itemWidth + 'px';
  carouselInner.style.transition = 'transform 0.5s ease';
  carouselInner.style.transform = `translateX(${newPosition})`;
  
  // If we reach the end, reset to the beginning without transition
  if (currentIndex === totalItems) {
    setTimeout(() => {
      currentIndex = 0;
      carouselInner.style.transition = 'none';
      carouselInner.style.transform = 'translateX(0)';
    }, 500);
  }
}

// Automatically move to next slide every 5 seconds (slower interval)
intervalId = setInterval(moveToNextSlide, 5000); // Using let to declare intervalId

// Add event listeners to pause carousel on mouseenter
items.forEach(item => {
  item.addEventListener('mouseenter', () => {
    isPaused = true;
    clearInterval(intervalId); // Pause the carousel
  });
  
  // Resume carousel on mouseleave
  item.addEventListener('mouseleave', () => {
    isPaused = false;
    clearInterval(intervalId); // Clear interval to prevent multiple intervals
    intervalId = setInterval(moveToNextSlide, 5000); // Resume carousel with slower interval
  });
});
