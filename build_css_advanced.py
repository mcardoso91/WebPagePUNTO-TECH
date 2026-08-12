import re

css_path = "css/components.css"
with open(css_path, "r") as f:
    css = f.read()

# Find where the old block starts
marker = "/* --- EDITORIAL SOBRE NOSOTROS --- */"
if marker in css:
    css = css[:css.find(marker)]

new_css = """/* --- EDITORIAL SOBRE NOSOTROS --- */
.editorial-premium {
    position: relative;
    width: 100%;
    background-color: var(--clr-bg-main);
    color: var(--clr-text-primary);
    overflow: hidden;
}

/* Background Depth */
.scene-bg {
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    pointer-events: none;
    z-index: 0;
    background: radial-gradient(circle at 50% 50%, rgba(37, 99, 235, 0.03) 0%, transparent 70%);
}
.bg-grid {
    width: 100%;
    height: 100%;
    background-image: 
        linear-gradient(rgba(255, 255, 255, 0.02) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255, 255, 255, 0.02) 1px, transparent 1px);
    background-size: 50px 50px;
    opacity: 0.5;
}

/* Base Scene Structure */
.scroll-scene {
    position: relative;
    width: 100%;
    --p: 0; /* Updated by JS */
}

/* Sticky Container */
.sticky-container {
    position: sticky;
    top: 0;
    height: 100vh;
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    z-index: 1;
}

.scene-content {
    width: 100%;
    max-width: 1200px;
    padding: 0 var(--spacing-sm);
    position: relative;
}

/* Heights for scrolling duration */
.scene-01 { height: 150vh; }
.scene-02 { height: 200vh; }
.scene-03 { height: 200vh; }
.scene-04 { height: 250vh; }
.scene-05 { height: 250vh; }
.scene-06 { height: 250vh; }
.scene-07 { height: 150vh; }

/* -----------------------------
   SCENE 01: HERO
----------------------------- */
.tech-graphic {
    position: absolute;
    top: -100px;
    left: 50%;
    transform: translateX(-50%);
    width: 200px;
    height: 200px;
    opacity: calc(1 - (var(--p) * 2));
}
.cyan-dot {
    position: absolute;
    top: 50%; left: 50%;
    width: 8px; height: 8px;
    background: var(--clr-accent-1);
    border-radius: 50%;
    transform: translate(-50%, -50%);
    box-shadow: 0 0 20px var(--clr-accent-1);
}
.tech-line {
    position: absolute;
    background: var(--clr-border);
}
.h-line { top: 50%; left: 0; width: 100%; height: 1px; }
.v-line { left: 50%; top: 0; height: 100%; width: 1px; }

.scene-01 .about-tag {
    text-align: center;
    color: var(--clr-accent-1);
    letter-spacing: 4px;
    font-size: 0.8rem;
    margin-bottom: var(--spacing-md);
    transform: translateY(calc(var(--p) * -50px));
    opacity: calc(1 - var(--p) * 1.5);
}

.hero-title-massive {
    text-align: center;
    font-size: clamp(3.5rem, 8vw, 7rem);
    font-weight: 800;
    line-height: 1;
    letter-spacing: -2px;
    transform: scale(calc(1 + var(--p) * 0.2)) translateY(calc(var(--p) * -100px));
    opacity: calc(1 - var(--p) * 1.5);
}

/* -----------------------------
   SCENE 02: EL CONCEPTO
----------------------------- */
.scene-02 .concept-intro {
    text-align: center;
    font-size: clamp(1.5rem, 3vw, 2.5rem);
    color: var(--clr-text-muted);
    font-weight: 400;
    margin-bottom: var(--spacing-md);
    opacity: calc( (var(--p) * 4) - (max(0, var(--p) - 0.5) * 8) );
    transform: translateY(calc(20px - var(--p) * 40px));
}

.scene-02 .concept-massive {
    text-align: center;
    font-size: clamp(2rem, 5vw, 4rem);
    font-weight: 800;
    line-height: 1.1;
    opacity: calc( (max(0, var(--p) - 0.2) * 3) );
}

.scene-02 .text-util {
    display: inline-block;
    transform: scale(calc(1 + max(0, var(--p) - 0.5) * 2));
}

/* -----------------------------
   SCENE 03: PROBLEMA -> IDEA -> PRODUCTO
----------------------------- */
.evolution-flow {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: var(--spacing-sm);
}

.evo-item {
    font-size: clamp(2rem, 5vw, 4rem);
    font-weight: 800;
    letter-spacing: -1px;
}
.evo-problem {
    color: var(--clr-text-muted);
    opacity: calc(max(0, 1 - max(var(--p) - 0.2, (var(--p) - 0.2) * -1) * 5));
    transform: scale(calc(0.8 + (1 - max(var(--p) - 0.2, (var(--p) - 0.2) * -1)) * 0.2));
}
.evo-line-container {
    height: 60px;
    width: 2px;
    background: var(--clr-border);
    position: relative;
    overflow: hidden;
}
.evo-line {
    position: absolute;
    top: 0; left: 0; width: 100%; height: 100%;
    background: var(--clr-accent-1);
    transform-origin: top;
    transform: scaleY(calc((var(--p) - 0.3) * 5));
}
.evo-idea {
    color: var(--clr-text-secondary);
    opacity: calc(max(0, 1 - max(var(--p) - 0.5, (var(--p) - 0.5) * -1) * 5));
    transform: scale(calc(0.8 + (1 - max(var(--p) - 0.5, (var(--p) - 0.5) * -1)) * 0.2));
}
.evo-product {
    opacity: calc(max(0, (var(--p) - 0.7) * 4));
    transform: scale(calc(0.8 + max(0, var(--p) - 0.7) * 1));
}

/* -----------------------------
   SCENE 04: FILOSOFÍA
----------------------------- */
.philosophy-stack {
    position: relative;
    height: 300px;
    display: flex;
    align-items: center;
    justify-content: center;
}
.phil-item {
    position: absolute;
    text-align: center;
}
.phil-title {
    font-size: clamp(4rem, 10vw, 8rem);
    font-weight: 900;
    line-height: 1;
    color: var(--clr-text-primary);
}
.phil-desc {
    font-size: clamp(1.2rem, 2vw, 1.5rem);
    color: var(--clr-accent-1);
    margin-top: var(--spacing-sm);
}

.phil-simple {
    opacity: calc(max(0, 1 - max(var(--p) - 0.16, (var(--p) - 0.16) * -1) * 6));
    transform: translateY(calc((var(--p) - 0.16) * -200px));
}
.phil-util {
    opacity: calc(max(0, 1 - max(var(--p) - 0.5, (var(--p) - 0.5) * -1) * 6));
    transform: translateY(calc((var(--p) - 0.5) * -200px));
}
.phil-escalable {
    opacity: calc(max(0, 1 - max(var(--p) - 0.83, (var(--p) - 0.83) * -1) * 6));
    transform: translateY(calc((var(--p) - 0.83) * -200px));
}

/* -----------------------------
   SCENE 05: CÓMO TRABAJAMOS
----------------------------- */
.process-wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
}
.process-title {
    font-size: clamp(2rem, 4vw, 3.5rem);
    font-weight: 800;
    margin-bottom: var(--spacing-xl);
    opacity: calc(max(0, var(--p) * 5));
}
.process-interactive {
    display: flex;
    gap: var(--spacing-lg);
}
.process-timeline {
    width: 4px;
    background: var(--clr-border);
    position: relative;
    border-radius: 2px;
}
.process-progress {
    position: absolute;
    top: 0; left: 0; width: 100%;
    background: var(--clr-accent-1);
    box-shadow: 0 0 10px var(--clr-accent-1);
    height: calc(var(--p) * 100%);
    border-radius: 2px;
}
.process-steps-list {
    display: flex;
    flex-direction: column;
    gap: var(--spacing-lg);
}
.proc-step h3 {
    font-size: clamp(1.5rem, 3vw, 2.5rem);
    font-weight: 700;
    color: var(--clr-text-muted);
}
.step-1 h3 { color: var(--clr-text-primary); opacity: calc(max(0.3, 1 - max(0, var(--p) - 0.25)*10)); }
.step-2 h3 { color: var(--clr-text-primary); opacity: calc(max(0.3, 1 - max(var(--p) - 0.4, (var(--p) - 0.4) * -1) * 10)); }
.step-3 h3 { color: var(--clr-text-primary); opacity: calc(max(0.3, 1 - max(var(--p) - 0.65, (var(--p) - 0.65) * -1) * 10)); }
.step-4 h3 { color: var(--clr-text-primary); opacity: calc(max(0.3, min(1, (var(--p) - 0.75) * 10))); }

/* -----------------------------
   SCENE 06: MANIFIESTO
----------------------------- */
.scene-06 .manifesto-intro {
    font-size: clamp(1.5rem, 3vw, 2.5rem);
    font-weight: 400;
    color: var(--clr-text-secondary);
    text-align: center;
    position: absolute;
    top: 50%; left: 50%;
    transform: translate(-50%, -50%);
    width: 100%;
    opacity: calc(max(0, 1 - max(var(--p) - 0.25, (var(--p) - 0.25) * -1) * 4));
}
.scene-06 .manifesto-huge {
    font-size: clamp(2.5rem, 6vw, 5.5rem);
    font-weight: 900;
    line-height: 1.1;
    text-align: center;
    position: absolute;
    top: 50%; left: 50%;
    transform: translate(-50%, -50%) scale(calc(0.9 + var(--p) * 0.2));
    width: 100%;
    opacity: calc(max(0, (var(--p) - 0.5) * 4));
}

/* -----------------------------
   SCENE 07: CIERRE
----------------------------- */
.scene-07 .closing-tag {
    opacity: calc(min(1, var(--p) * 5));
}
.closing-sequence {
    margin: var(--spacing-md) 0;
}
.close-word {
    font-size: clamp(3.5rem, 8vw, 7rem);
    font-weight: 900;
    line-height: 1.1;
    color: var(--clr-text-primary);
}
.w1 { opacity: calc(max(0, (var(--p) - 0.2) * 5)); transform: translateX(calc((1 - max(0, min(1, (var(--p) - 0.2)*5))) * -50px)); }
.w2 { opacity: calc(max(0, (var(--p) - 0.4) * 5)); transform: translateX(calc((1 - max(0, min(1, (var(--p) - 0.4)*5))) * -50px)); }
.w3 { opacity: calc(max(0, (var(--p) - 0.6) * 5)); transform: translateX(calc((1 - max(0, min(1, (var(--p) - 0.6)*5))) * -50px)); }

.closing-final {
    font-size: clamp(1.2rem, 2.5vw, 1.8rem);
    color: var(--clr-text-muted);
    font-weight: 500;
    opacity: calc(max(0, (var(--p) - 0.8) * 5));
    margin-top: var(--spacing-lg);
}

@media (max-width: 768px) {
    .scene-01, .scene-02, .scene-03, .scene-04, .scene-05, .scene-06 { height: 150vh; }
    .tech-graphic { opacity: 0; display: none; }
    .phil-title { font-size: 3.5rem; }
    .evo-item { font-size: 2.5rem; }
    .process-interactive { flex-direction: row; }
}
"""

with open(css_path, "w") as f:
    f.write(css + "\n" + new_css)
print("Updated CSS with advanced logic.")
