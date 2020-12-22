var headingArray = ["Steve Franz", "Web Developer", "Python Developer", "iOS Developer"]
var counter = 0;
animateHeading(headingArray[0]);

function animateHeading(text) {
  $(".heading-text").text(text);
  $(".heading-text").css("opacity", "0");
  $(".heading-text").animate({
    opacity: .9
  }, 3000);
  $(".heading-text").animate({
    opacity: .00
  }, 1500, function() {

    counter++;
    if (counter < headingArray.length) {
      animateHeading(headingArray[counter])
    } else {
      counter = 0;
      animateHeading(headingArray[counter])
    }

  });
}
