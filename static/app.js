$(function () {
  $(".delete-review").on("click", async function (e) {
    const $tgt = $(e.target);
    const { reviewId } = $tgt.data();
    const response = await axios.delete(`/reviews/${reviewId}`);

    if (response.data.status === "ok") {
      const $li = $tgt.parent()
      $li.slideUp("slow", function () {
        const $ul = $li.parent();
        $li.remove();
        if ($ul.children().length === 0) {
          $ul.text("No reviews yet :(");
        }
      });
    }
  });
});
