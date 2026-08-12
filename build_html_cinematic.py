import re

html_path = "index.html"
with open(html_path, "r") as f:
    html = f.read()

new_sobre_nosotros = """
        <!-- SOBRE NOSOTROS SECTION (CINEMATIC) -->
        <section id="sobre-nosotros" class="cinematic-experience">
            
            <!-- SCENE 01: IDENTIDAD -->
            <div class="cinematic-scene scene-hero">
                <div class="cinematic-viewport">
                    <div class="scene-layer bg-layer">
                        <svg class="abstract-nodes" viewBox="0 0 100 100" preserveAspectRatio="none">
                            <path class="node-line" d="M -10 80 Q 30 90 40 40 T 110 20" />
                            <circle class="node-dot" cx="40" cy="40" r="1" />
                            <circle class="node-dot active-dot" cx="75" cy="27" r="1.5" />
                        </svg>
                    </div>
                    <div class="scene-layer content-layer">
                        <div class="hero-block">
                            <span class="label-tech">SOBRE PUNTO-TECH</span>
                            <h1 class="mega-title">Tecnología<br>que realmente<br>sirve.</h1>
                        </div>
                    </div>
                </div>
            </div>

            <!-- SCENE 02: LA IDEA -->
            <div class="cinematic-scene scene-idea">
                <div class="cinematic-viewport">
                    <div class="scene-layer content-layer centered">
                        <h2 class="idea-intro">PUNTO-TECH nace de una idea simple.</h2>
                        <h1 class="mega-title idea-main">
                            HACER QUE LA TECNOLOGÍA SEA REALMENTE<br>
                            <span class="text-util text-gradient">ÚTIL.</span>
                        </h1>
                    </div>
                </div>
            </div>

            <!-- SCENE 03: MANIFIESTO 1 (PROBLEMA -> SOLUCIÓN) -->
            <div class="cinematic-scene scene-manifesto-1">
                <div class="cinematic-viewport">
                    <div class="scene-layer content-layer centered">
                        <h3 class="manifesto-small m1-intro">NO SE TRATA DE SUMAR TECNOLOGÍA PORQUE SÍ.</h3>
                        <h1 class="mega-title manifesto-large m1-outro">SE TRATA DE<br>RESOLVER ALGO.</h1>
                    </div>
                </div>
            </div>

            <!-- SCENE 04: FILOSOFÍA (SIMPLE / ÚTIL / ESCALABLE) -->
            <div class="cinematic-scene scene-philosophy">
                <div class="cinematic-viewport">
                    <div class="scene-layer content-layer centered">
                        <div class="phil-item phil-simple">
                            <h1 class="mega-title">SIMPLE</h1>
                            <p class="phil-desc">La tecnología debe ser fácil de entender.</p>
                        </div>
                        <div class="phil-item phil-util">
                            <h1 class="mega-title text-gradient">ÚTIL</h1>
                            <p class="phil-desc">Debe resolver una necesidad real.</p>
                        </div>
                        <div class="phil-item phil-escalable">
                            <h1 class="mega-title">ESCALABLE</h1>
                            <p class="phil-desc">Debe poder crecer junto con el proyecto.</p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- SCENE 05: CÓMO TRABAJAMOS -->
            <div class="cinematic-scene scene-process">
                <div class="cinematic-viewport">
                    <div class="scene-layer content-layer flex-layout">
                        <div class="process-left">
                            <h2 class="process-title">De la idea a algo que funciona.</h2>
                        </div>
                        <div class="process-right">
                            <div class="process-line-bg">
                                <div class="process-line-fill"></div>
                            </div>
                            <div class="process-steps">
                                <div class="p-step s-1">
                                    <span class="p-num">01</span>
                                    <h3 class="p-name">ENTENDER</h3>
                                </div>
                                <div class="p-step s-2">
                                    <span class="p-num">02</span>
                                    <h3 class="p-name">PENSAR</h3>
                                </div>
                                <div class="p-step s-3">
                                    <span class="p-num">03</span>
                                    <h3 class="p-name">CONSTRUIR</h3>
                                </div>
                                <div class="p-step s-4">
                                    <span class="p-num">04</span>
                                    <h3 class="p-name">EVOLUCIONAR</h3>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- SCENE 06: MANIFIESTO FINAL -->
            <div class="cinematic-scene scene-manifesto-final">
                <div class="cinematic-viewport">
                    <div class="scene-layer content-layer centered">
                        <h3 class="manifesto-small mf-intro">La mejor tecnología no siempre es la más compleja.</h3>
                        <h1 class="mega-title manifesto-large text-gradient mf-outro">ES LA QUE HACE QUE TODO PAREZCA MÁS SIMPLE.</h1>
                    </div>
                </div>
            </div>

            <!-- SCENE 07: CIERRE -->
            <div class="cinematic-scene scene-cierre">
                <div class="cinematic-viewport">
                    <div class="scene-layer content-layer centered">
                        <span class="label-tech cierre-label">PUNTO-TECH</span>
                        <div class="cierre-words">
                            <h1 class="mega-title cw-1">Pensamos.</h1>
                            <h1 class="mega-title cw-2">Desarrollamos.</h1>
                            <h1 class="mega-title cw-3">Construimos.</h1>
                        </div>
                        <p class="cierre-final">Tecnología para hacer las cosas mejor.</p>
                    </div>
                </div>
            </div>

        </section>
"""

# Match both old versions if they exist
regex = re.compile(r'\s*<!-- SOBRE NOSOTROS SECTION.*?<section id="sobre-nosotros".*?</section>', re.DOTALL)
html = regex.sub(new_sobre_nosotros, html)

with open(html_path, "w") as f:
    f.write(html)
print("Updated cinematic HTML.")
