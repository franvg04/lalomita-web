var NUM = "5493492338908"; // Reemplazar por el número real, con código de país
document.querySelectorAll("[data-msg]").forEach(function (a) {
  a.href =
    "https://wa.me/" + NUM + "?text=" + encodeURIComponent(a.dataset.msg);
  a.target = "_blank";
  a.rel = "noopener";
});
var io = new IntersectionObserver(
  function (es) {
    es.forEach(function (e) {
      if (e.isIntersecting) {
        e.target.classList.add("in");
        io.unobserve(e.target);
      }
    });
  },
  { threshold: 0.15 },
);
document.querySelectorAll(".rv").forEach(function (el) {
  io.observe(el);
});
