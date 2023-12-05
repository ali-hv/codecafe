$(document).ready(function() {
    $(".delete-button").on("click", function() {
        var courseId = $(this).data("course-id");
      var csrftoken = $("#csrf-token [name=csrfmiddlewaretoken]").val();

      $.ajax({
        type: "POST",
        url: "/cart/delete-course-from-cart/",  // Replace with your actual URL
        data: {
          csrfmiddlewaretoken: csrftoken,
          course_id: courseId
        },
        success: function(response) {
          console.log("Course removed successfully");

          var courseContainer = $("#course-" + courseId);
          courseContainer.remove();

          if ($(".cart-container").find(".cart-item").length === 0) {
            $(".temp-empty-message").show();
            $(".cart-total").hide();
            $(".checkout-button").hide();
            $(".empty-message").hide();
    }
        },
        error: function(error) {
          console.error("Error removing course:", error);
        }
        });
    });
});