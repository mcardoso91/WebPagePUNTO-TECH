css_content = """
/* --- EDITORIAL SOBRE NOSOTROS --- */
.about-narrative {
  position: relative;
  width: 100%;
  background-color: var(--clr-bg-main);
  padding-top: var(--spacing-xl);
  padding-bottom: var(--spacing-xl);
}

.scene-container {
  min-height: 80vh; /* Allow enough scrolling space */
  display: flex;
  align-items: center;
  justify-content: center;
  padding: var(--spacing-xl) var(--spacing-sm);
}

.about-tag {
  color: var(--clr-accent-1);
  font-weight: 600;
  letter-spacing: 2px;
  margin-bottom: var(--spacing-md);
  text-transform: uppercase;
  font-size: 0.9rem;
}

.scene-title-lg {
  font-size: clamp(3rem, 6vw, 5rem);
  font-weight: 800;
  line-height: 1.1;
  color: var(--clr-text-primary);
  letter-spacing: -1px;
}

.scene-title-md {
  font-size: clamp(2rem, 4vw, 3.5rem);
  font-weight: 800;
  line-height: 1.2;
  color: var(--clr-text-primary);
  letter-spacing: -0.5px;
  margin-bottom: var(--spacing-md);
}

.scene-subtitle {
  font-size: clamp(1.2rem, 2vw, 1.5rem);
  font-weight: 500;
  color: var(--clr-text-muted);
  margin-bottom: var(--spacing-sm);
}

.scene-paragraph {
  font-size: clamp(1.1rem, 2vw, 1.4rem);
  color: var(--clr-text-secondary);
  line-height: 1.6;
  max-width: 800px;
  margin: 0 auto;
}

/* Philosophy Grid */
.philosophy-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: var(--spacing-lg);
  max-width: 1000px;
  margin: 0 auto;
}

.philosophy-item h3 {
  font-size: 2rem;
  color: var(--clr-primary);
  margin-bottom: var(--spacing-sm);
  font-weight: 800;
}

.philosophy-item p {
  color: var(--clr-text-secondary);
  font-size: 1.1rem;
  line-height: 1.5;
}

@media (max-width: 768px) {
  .philosophy-grid {
    grid-template-columns: 1fr;
    gap: var(--spacing-md);
    text-align: center;
  }
}

/* Process Steps */
.process-steps {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-md);
  max-width: 600px;
  margin: 0 auto;
  text-align: left;
}

.process-step {
  padding-left: var(--spacing-md);
  border-left: 2px solid var(--clr-border);
  position: relative;
}

.process-step::before {
  content: '';
  position: absolute;
  left: -6px;
  top: 0;
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: var(--clr-accent-2);
}

.step-num {
  font-size: 1.2rem;
  font-weight: 800;
  color: var(--clr-accent-1);
  margin-bottom: var(--spacing-xs);
  display: block;
}

.process-step p {
  color: var(--clr-text-secondary);
  font-size: 1.1rem;
}

/* Closing */
.closing-words {
  font-size: clamp(3rem, 6vw, 5rem);
  font-weight: 900;
  line-height: 1.1;
  color: var(--clr-text-primary);
  margin-bottom: var(--spacing-md);
}

.closing-slogan {
  font-size: clamp(1.2rem, 2.5vw, 1.8rem);
  color: var(--clr-text-muted);
  font-weight: 500;
}

/* Animations */
.reveal-slow {
  opacity: 0;
  transform: translateY(40px);
  transition: opacity 1.2s cubic-bezier(0.2, 0.8, 0.2, 1), transform 1.2s cubic-bezier(0.2, 0.8, 0.2, 1);
}

.reveal-slow.visible {
  opacity: 1;
  transform: translateY(0);
}
"""

with open("css/components.css", "a") as f:
    f.write(css_content)

print("CSS updated.")
