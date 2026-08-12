import re

html_path = "index.html"
with open(html_path, "r") as f:
    html = f.read()

# 1. Update Nav (Header)
old_nav_header = """            <nav class="nav-links">
                <a href="#home">Inicio</a>
                <a href="#development">Development</a>
                <a href="#market">Market</a>
                <a href="#proyectos">Proyectos</a>
            </nav>"""
new_nav_header = """            <nav class="nav-links">
                <a href="#home">Inicio</a>
                <a href="#development">Development</a>
                <a href="#market">Market</a>
                <a href="#proyectos">Proyectos</a>
                <a href="#sobre-nosotros">Sobre Nosotros</a>
                <a href="#contacto">Contacto</a>
            </nav>"""
html = html.replace(old_nav_header, new_nav_header)

# 2. Update Nav (Footer)
old_nav_footer = """                <nav class="nav-links">
                    <a href="#development">Development</a>
                    <a href="#market">Market</a>
                    <a href="#proyectos">Proyectos</a>
                </nav>"""
new_nav_footer = """                <nav class="nav-links">
                    <a href="#development">Development</a>
                    <a href="#market">Market</a>
                    <a href="#proyectos">Proyectos</a>
                    <a href="#sobre-nosotros">Sobre Nosotros</a>
                    <a href="#contacto">Contacto</a>
                </nav>"""
html = html.replace(old_nav_footer, new_nav_footer)

# 3. Add id="contacto" to footer
html = html.replace('<footer class="footer">', '<footer id="contacto" class="footer">')

# 4. Insert Sobre Nosotros Section before </main>
sobre_nosotros_html = """
        <!-- SOBRE NOSOTROS SECTION -->
        <section id="sobre-nosotros" class="about-narrative">
            
            <!-- ESCENA 01 -->
            <div class="scene-container">
                <div class="container text-center reveal-slow">
                    <p class="about-tag">SOBRE PUNTO-TECH</p>
                    <h2 class="scene-title-lg">Tecnología que realmente sirve.</h2>
                </div>
            </div>

            <!-- ESCENA 02 -->
            <div class="scene-container">
                <div class="container text-center">
                    <h3 class="scene-subtitle reveal-slow">PUNTO-TECH nace de una idea simple:</h3>
                    <h2 class="scene-title-md text-gradient reveal-slow" style="transition-delay: 0.2s;">hacer que la tecnología sea realmente útil.</h2>
                    <p class="scene-paragraph reveal-slow" style="transition-delay: 0.4s;">
                        Creamos productos y herramientas digitales para personas y negocios que buscan trabajar mejor, simplificar procesos y aprovechar nuevas oportunidades.
                    </p>
                </div>
            </div>

            <!-- ESCENA 03 -->
            <div class="scene-container">
                <div class="container text-center">
                    <h3 class="scene-subtitle reveal-slow">No hacemos tecnología por hacer tecnología.</h3>
                    <h2 class="scene-title-md reveal-slow" style="transition-delay: 0.2s;">Entendemos el problema antes de construir la solución.</h2>
                </div>
            </div>

            <!-- ESCENA 04 -->
            <div class="scene-container">
                <div class="container">
                    <div class="philosophy-grid">
                        <div class="philosophy-item reveal-slow">
                            <h3>SIMPLE</h3>
                            <p>La tecnología debe ser fácil de entender y utilizar.</p>
                        </div>
                        <div class="philosophy-item reveal-slow" style="transition-delay: 0.2s;">
                            <h3>ÚTIL</h3>
                            <p>Cada producto debe resolver una necesidad real.</p>
                        </div>
                        <div class="philosophy-item reveal-slow" style="transition-delay: 0.4s;">
                            <h3>ESCALABLE</h3>
                            <p>Las soluciones deben poder crecer junto con el proyecto.</p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- ESCENA 05 -->
            <div class="scene-container">
                <div class="container text-center">
                    <h2 class="scene-title-md reveal-slow" style="margin-bottom: var(--spacing-xl);">De la idea a algo que funciona.</h2>
                    
                    <div class="process-steps">
                        <div class="process-step reveal-slow">
                            <span class="step-num">01 &mdash; ENTENDER</span>
                            <p>Conocemos la necesidad y el contexto.</p>
                        </div>
                        <div class="process-step reveal-slow" style="transition-delay: 0.1s;">
                            <span class="step-num">02 &mdash; PENSAR</span>
                            <p>Definimos qué solución tiene sentido.</p>
                        </div>
                        <div class="process-step reveal-slow" style="transition-delay: 0.2s;">
                            <span class="step-num">03 &mdash; CONSTRUIR</span>
                            <p>Diseñamos y desarrollamos el producto.</p>
                        </div>
                        <div class="process-step reveal-slow" style="transition-delay: 0.3s;">
                            <span class="step-num">04 &mdash; EVOLUCIONAR</span>
                            <p>Mejoramos y adaptamos la solución.</p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- ESCENA 06 -->
            <div class="scene-container">
                <div class="container text-center">
                    <h2 class="scene-title-lg text-gradient reveal-slow">La mejor tecnología no siempre es la más compleja.</h2>
                    <h2 class="scene-title-lg reveal-slow" style="transition-delay: 0.3s; margin-top: var(--spacing-md);">Es la que hace que todo parezca más simple.</h2>
                </div>
            </div>

            <!-- ESCENA 07 -->
            <div class="scene-container">
                <div class="container text-center reveal-slow">
                    <h3 class="about-tag">PUNTO-TECH</h3>
                    <div class="closing-words">
                        <span>Pensamos.</span><br>
                        <span>Desarrollamos.</span><br>
                        <span>Construimos.</span>
                    </div>
                    <p class="closing-slogan">Tecnología para hacer las cosas mejor.</p>
                </div>
            </div>
            
        </section>
"""
html = html.replace('    </main>', sobre_nosotros_html + '    </main>')

with open(html_path, "w") as f:
    f.write(html)
print("Updated HTML.")
