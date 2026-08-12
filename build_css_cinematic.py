import re

css_path = "css/components.css"
with open(css_path, "r") as f:
    css = f.read()

# Remove the old EDITORIAL SOBRE NOSOTROS block and everything after it
marker1 = "/* --- EDITORIAL SOBRE NOSOTROS --- */"
marker2 = "/* --- EDITORIAL SOBRE NOSOTROS (PREMIUM SCROLL-DRIVEN) --- */"
if marker1 in css:
    css = css[:css.find(marker1)]
elif marker2 in css:
    css = css[:css.find(marker2)]

new_css = """
/* --- CINEMATIC ABOUT --- */
.cinematic-experience {
    position: relative;
    width: 100%;
    background-color: var(--clr-bg-main);
    color: var(--clr-text-primary);
    /* NO OVERFLOW HIDDEN HERE! It breaks sticky */
}

/* Base Scene Structure */
.cinematic-scene {
    position: relative;
    width: 100%;
    /* Default height for all scenes */
    height: 250vh; 
    --p: 0; /* Updated by JS */
}

/* 100vh Sticky Viewport for each scene */
.cinematic-viewport {
    position: sticky;
    top: 0;
    width: 100%;
    height: 100vh;
    overflow: hidden; /* This is fine here, it clips internal content */
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: var(--clr-bg-main); /* Hides previous scene as this one scrolls over */
    /* Add a subtle top border to create a "curtain" effect when a new scene scrolls up over the sticky previous scene */
    border-top: 1px solid rgba(255, 255, 255, 0.03);
}

.scene-layer {
    position: absolute;
    top: 0; left: 0; width: 100%; height: 100%;
    pointer-events: none;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: var(--spacing-xl);
}

.bg-layer { z-index: 1; }
.content-layer { z-index: 2; }

/* Global Cinematic Typography */
.mega-title {
    font-size: clamp(3rem, 7vw, 6.5rem);
    font-weight: 900;
    line-height: 1.05;
    letter-spacing: -0.03em;
    margin: 0;
}
.label-tech {
    font-size: 0.8rem;
    letter-spacing: 0.3em;
    color: var(--clr-accent-1);
    text-transform: uppercase;
    display: block;
    margin-bottom: var(--spacing-md);
}

/* -----------------------------
   SCENE 01: IDENTIDAD
----------------------------- */
.scene-hero {
    height: 200vh;
}
.abstract-nodes {
    width: 100%;
    height: 100%;
    opacity: 0.15;
}
.node-line {
    fill: none;
    stroke: var(--clr-accent-1);
    stroke-width: 0.2;
    stroke-dasharray: 200;
    /* Draw the line based on scroll */
    stroke-dashoffset: calc(200 - (var(--p) * 200)); 
}
.node-dot {
    fill: var(--clr-accent-1);
    opacity: calc(var(--p) * 2);
}

.hero-block {
    text-align: left;
    width: 100%;
    max-width: 1200px;
    /* Slowly move down and fade out */
    transform: translateY(calc(var(--p) * 100px));
    opacity: calc(1 - var(--p) * 1.5);
}

/* -----------------------------
   SCENE 02: LA IDEA
----------------------------- */
.scene-idea {
    height: 200vh;
}
.centered { text-align: center; flex-direction: column; }
.idea-intro {
    font-size: clamp(1.2rem, 3vw, 2rem);
    font-weight: 400;
    color: var(--clr-text-secondary);
    margin-bottom: var(--spacing-xl);
    /* Fades out completely by 0.3 */
    opacity: calc(1 - var(--p) * 3);
    transform: translateY(calc(var(--p) * -50px));
}
.idea-main {
    /* Fades in after 0.2 */
    opacity: calc( (var(--p) - 0.2) * 5 );
}
.text-util {
    display: inline-block;
    /* Scale massively */
    transform: scale(calc(1 + max(0, var(--p) - 0.4) * 4));
}

/* -----------------------------
   SCENE 03: MANIFIESTO 1
----------------------------- */
.scene-manifesto-1 {
    height: 200vh;
}
.manifesto-small {
    font-size: clamp(1.2rem, 3vw, 2rem);
    font-weight: 500;
    color: var(--clr-text-secondary);
    letter-spacing: -0.02em;
}
.m1-intro {
    position: absolute;
    /* Disappears by 0.4 */
    opacity: calc(1 - var(--p) * 2.5);
    transform: translateY(calc(var(--p) * -100px));
}
.m1-outro {
    /* Appears after 0.4 */
    opacity: calc( (var(--p) - 0.4) * 3 );
    transform: translateY(calc(50px - max(0, var(--p) - 0.4) * 100px));
}

/* -----------------------------
   SCENE 04: FILOSOFÍA
----------------------------- */
.scene-philosophy {
    height: 300vh;
}
.phil-item {
    position: absolute;
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
}
.phil-desc {
    font-size: clamp(1rem, 2vw, 1.5rem);
    color: var(--clr-text-muted);
    margin-top: var(--spacing-sm);
}
/* Peak at 0.16 */
.phil-simple {
    opacity: calc(max(0, 1 - max(var(--p) - 0.16, (var(--p) - 0.16) * -1) * 6));
    transform: translateY(calc((var(--p) - 0.16) * -150px));
}
/* Peak at 0.5 */
.phil-util {
    opacity: calc(max(0, 1 - max(var(--p) - 0.5, (var(--p) - 0.5) * -1) * 6));
    transform: translateY(calc((var(--p) - 0.5) * -150px));
}
/* Peak at 0.83 */
.phil-escalable {
    opacity: calc(max(0, 1 - max(var(--p) - 0.83, (var(--p) - 0.83) * -1) * 6));
    transform: translateY(calc((var(--p) - 0.83) * -150px));
}

/* -----------------------------
   SCENE 05: CÓMO TRABAJAMOS
----------------------------- */
.scene-process {
    height: 300vh;
}
.flex-layout {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    max-width: 1200px;
    width: 100%;
    margin: 0 auto;
    gap: 4rem;
}
.process-left {
    flex: 1;
    opacity: calc(max(0, var(--p) * 4));
}
.process-title {
    font-size: clamp(2.5rem, 5vw, 4rem);
    font-weight: 800;
    line-height: 1.1;
    letter-spacing: -0.03em;
}
.process-right {
    flex: 1;
    display: flex;
    gap: 2rem;
    /* Pushes up as we scroll */
    transform: translateY(calc(150px - (var(--p) * 300px)));
    opacity: calc(max(0, var(--p) * 3));
}
.process-line-bg {
    width: 2px;
    background: var(--clr-border);
    position: relative;
    border-radius: 1px;
}
.process-line-fill {
    position: absolute;
    top: 0; left: 0; width: 100%;
    background: var(--clr-accent-1);
    height: calc(var(--p) * 100%);
    box-shadow: 0 0 10px var(--clr-accent-1);
}
.process-steps {
    display: flex;
    flex-direction: column;
    gap: 4rem;
    padding-bottom: 2rem;
}
.p-step {
    display: flex;
    flex-direction: column;
}
.p-num {
    font-size: 1rem;
    font-weight: 700;
    color: var(--clr-accent-1);
    letter-spacing: 0.1em;
    margin-bottom: 0.5rem;
}
.p-name {
    font-size: clamp(2rem, 4vw, 3rem);
    font-weight: 800;
    color: var(--clr-text-muted);
}
/* Highlight steps as p passes their threshold */
.s-1 .p-name { color: var(--clr-text-primary); opacity: calc(max(0.3, 1 - max(var(--p) - 0.25, (var(--p) - 0.25) * -1) * 5)); }
.s-2 .p-name { color: var(--clr-text-primary); opacity: calc(max(0.3, 1 - max(var(--p) - 0.45, (var(--p) - 0.45) * -1) * 5)); }
.s-3 .p-name { color: var(--clr-text-primary); opacity: calc(max(0.3, 1 - max(var(--p) - 0.65, (var(--p) - 0.65) * -1) * 5)); }
.s-4 .p-name { color: var(--clr-text-primary); opacity: calc(max(0.3, 1 - max(var(--p) - 0.85, (var(--p) - 0.85) * -1) * 5)); }

/* -----------------------------
   SCENE 06: MANIFIESTO FINAL
----------------------------- */
.scene-manifesto-final {
    height: 250vh;
}
.mf-intro {
    position: absolute;
    opacity: calc(1 - max(var(--p) - 0.2, (var(--p) - 0.2) * -1) * 4);
}
.mf-outro {
    opacity: calc( (var(--p) - 0.4) * 4 );
    transform: scale(calc(0.9 + max(0, var(--p) - 0.4) * 0.2));
}

/* -----------------------------
   SCENE 07: CIERRE
----------------------------- */
.scene-cierre {
    height: 200vh;
}
.cierre-label {
    opacity: calc(var(--p) * 5);
}
.cierre-words {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: 2rem 0;
}
.cw-1 { opacity: calc((var(--p) - 0.2) * 5); transform: translateY(calc((1 - max(0, min(1, (var(--p) - 0.2)*5))) * -30px)); }
.cw-2 { opacity: calc((var(--p) - 0.4) * 5); transform: translateY(calc((1 - max(0, min(1, (var(--p) - 0.4)*5))) * -30px)); }
.cw-3 { opacity: calc((var(--p) - 0.6) * 5); transform: translateY(calc((1 - max(0, min(1, (var(--p) - 0.6)*5))) * -30px)); }

.cierre-final {
    font-size: clamp(1.2rem, 2.5vw, 1.8rem);
    color: var(--clr-text-muted);
    opacity: calc((var(--p) - 0.8) * 5);
}

@media (max-width: 768px) {
    /* Compress scroll heights on mobile to prevent extreme fatigue, but keep the effect intact */
    .cinematic-scene { height: 180vh; }
    .scene-philosophy { height: 250vh; }
    .scene-process { height: 250vh; }
    
    .flex-layout {
        flex-direction: column;
        justify-content: center;
        gap: 2rem;
    }
    .process-left { text-align: center; }
    .process-right { 
        width: 100%; 
        transform: translateY(calc(50px - (var(--p) * 150px)));
    }
}
"""

with open(css_path, "w") as f:
    f.write(css + "\n" + new_css)
print("Updated CSS with strict cinematic viewport logic.")
