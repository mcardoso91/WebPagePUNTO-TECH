import re

html_path = "index.html"
with open(html_path, "r") as f:
    html = f.read()

new_sobre_nosotros = """
        <!-- SOBRE NOSOTROS SECTION (PREMIUM) -->
        <section id="sobre-nosotros" class="editorial-premium">
            <div class="scene-bg">
                <div class="bg-grid"></div>
            </div>

            <!-- SCENE 01: HERO -->
            <div class="scroll-scene scene-01">
                <div class="sticky-container">
                    <div class="scene-content">
                        <div class="tech-graphic">
                            <div class="cyan-dot"></div>
                            <div class="tech-line h-line"></div>
                            <div class="tech-line v-line"></div>
                        </div>
                        <p class="about-tag">SOBRE PUNTO-TECH</p>
                        <h2 class="hero-title-massive">Tecnología que realmente sirve.</h2>
                    </div>
                </div>
            </div>

            <!-- SCENE 02: EL CONCEPTO -->
            <div class="scroll-scene scene-02">
                <div class="sticky-container">
                    <div class="scene-content">
                        <h3 class="concept-intro">PUNTO-TECH nace de una idea simple.</h3>
                        <h2 class="concept-massive">HACER QUE LA TECNOLOGÍA SEA REALMENTE <span class="text-util text-gradient">ÚTIL.</span></h2>
                    </div>
                </div>
            </div>

            <!-- SCENE 03: PROBLEMA -> IDEA -> PRODUCTO -->
            <div class="scroll-scene scene-03">
                <div class="sticky-container">
                    <div class="scene-content">
                        <div class="evolution-flow">
                            <div class="evo-item evo-problem">PROBLEMA</div>
                            <div class="evo-line-container"><div class="evo-line"></div></div>
                            <div class="evo-item evo-idea">IDEA</div>
                            <div class="evo-line-container"><div class="evo-line"></div></div>
                            <div class="evo-item evo-product text-gradient">PRODUCTO</div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- SCENE 04: FILOSOFÍA -->
            <div class="scroll-scene scene-04">
                <div class="sticky-container">
                    <div class="scene-content">
                        <div class="philosophy-stack">
                            <div class="phil-item phil-simple">
                                <h2 class="phil-title">SIMPLE</h2>
                                <p class="phil-desc">La tecnología debe ser fácil de entender.</p>
                            </div>
                            <div class="phil-item phil-util">
                                <h2 class="phil-title">ÚTIL</h2>
                                <p class="phil-desc">Debe resolver una necesidad real.</p>
                            </div>
                            <div class="phil-item phil-escalable">
                                <h2 class="phil-title">ESCALABLE</h2>
                                <p class="phil-desc">Debe poder crecer junto con el proyecto.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- SCENE 05: CÓMO TRABAJAMOS -->
            <div class="scroll-scene scene-05">
                <div class="sticky-container">
                    <div class="scene-content">
                        <div class="process-wrapper">
                            <h2 class="process-title">De la idea a algo que funciona.</h2>
                            <div class="process-interactive">
                                <div class="process-timeline">
                                    <div class="process-progress"></div>
                                </div>
                                <div class="process-steps-list">
                                    <div class="proc-step step-1"><h3>01 ENTENDER</h3></div>
                                    <div class="proc-step step-2"><h3>02 PENSAR</h3></div>
                                    <div class="proc-step step-3"><h3>03 CONSTRUIR</h3></div>
                                    <div class="proc-step step-4"><h3>04 EVOLUCIONAR</h3></div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- SCENE 06: MANIFIESTO -->
            <div class="scroll-scene scene-06">
                <div class="sticky-container">
                    <div class="scene-content">
                        <h3 class="manifesto-intro">La mejor tecnología no siempre es la más compleja.</h3>
                        <h2 class="manifesto-huge text-gradient">Es la que hace que todo parezca más simple.</h2>
                    </div>
                </div>
            </div>

            <!-- SCENE 07: CIERRE -->
            <div class="scroll-scene scene-07">
                <div class="sticky-container">
                    <div class="scene-content text-center">
                        <h3 class="about-tag closing-tag">PUNTO-TECH</h3>
                        <div class="closing-sequence">
                            <div class="close-word w1">Pensamos.</div>
                            <div class="close-word w2">Desarrollamos.</div>
                            <div class="close-word w3">Construimos.</div>
                        </div>
                        <p class="closing-final">Tecnología para hacer las cosas mejor.</p>
                    </div>
                </div>
            </div>
        </section>"""

regex = re.compile(r'\s*<!-- SOBRE NOSOTROS SECTION -->\s*<section id="sobre-nosotros".*?</section>', re.DOTALL)
html = regex.sub(new_sobre_nosotros, html)

with open(html_path, "w") as f:
    f.write(html)
print("Updated advanced HTML.")
