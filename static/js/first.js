var t1 = gsap.timeline();
t1.from(".elmt", 1, {
    y: -50,
    opacity: 0
});
t1.from(".img1 img", 0.5, {
    y: -100, // Move downwards
    scale: 1.4,
    stagger: 0.2,
    opacity: 0
}, "+=0.8");
t1.from(".img1 img", 2, {
    y: -20, // Move upwards
    stagger: 0.2
});
