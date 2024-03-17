$(document).ready(function() {
    $("#owl-demo").owlCarousel({
        navigation: true, // Show next and prev buttons
        autoplay: true, // Start autoplay
        autoplayTimeout: 3000, // Autoplay interval for the first carousel (in milliseconds)
        slideSpeed: 600,
        pagination: true, // Enable pagination
        dots: true, // Enable dots
        items: 1, 
        loop: true, // Set loop to true for infinite carousel
        itemsDesktop: false,
        itemsDesktopSmall: false,
        itemsTablet: false,
        itemsMobile: false
    });

    // Handle next button click
    $(".owl-next").click(function() {
        $("#owl-demo").trigger("next.owl.carousel");
    });

    // Handle previous button click
    $(".owl-prev").click(function() {
        $("#owl-demo").trigger("prev.owl.carousel");
    });

    // Initialize the second carousel
    initSecondCarousel();
});

function initSecondCarousel() {
    $("#another-owl-demo").owlCarousel({
        navigation: false, // Show next and prev buttons
        autoplay: true, // Start autoplay
        autoplayTimeout: 1500, // Autoplay interval for the second carousel (in milliseconds)
        slideSpeed: 600,
        pagination: false, // Disable pagination
        dots: false, // Enable dots
        items: 1, 
        loop: true, // Set loop to true for infinite carousel
        itemsDesktop: false,
        itemsDesktopSmall: false,
        itemsTablet: false,
        itemsMobile: false
    });
}
