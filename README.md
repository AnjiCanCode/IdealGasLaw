# Beyond Ideal — Interactive Gas Laws

An interactive, simulation-based exploration of the ideal gas law, kinetic theory, and real gas behavior. Built as a GitHub Pages site.

## Live Demo

Visit the site at: `https://[your-username].github.io/IdealGasLaw/`

## What is this?

This is a series of interactive explanations that use real-time 2D particle simulations to build intuition about:

1. **What is a Gas?** — The microscopic picture
2. **The Ideal Gas Law (PV = nRT)** — Boyle's Law, Gay-Lussac's Law, and the combined law
3. **Kinetic Theory** — Why temperature is motion and pressure is momentum transfer
4. **When Ideal Breaks Down** — Excluded volume and intermolecular attraction
5. **The Van der Waals Equation** — Correcting for real gas behavior, phase transitions
6. **Mixtures & Solutions** — Dalton's Law and non-ideal mixtures
7. **Playground** — Free exploration with all controls

## How to Run Locally

Simply serve the directory with any static file server:

```bash
# Using Python
python3 -m http.server 8000

# Using Node.js
npx serve .

# Using PHP
php -S localhost:8000
```

Then open `http://localhost:8000` in your browser.

## Deploying to GitHub Pages

1. Push to a GitHub repository
2. Go to Settings → Pages
3. Set source to "Deploy from a branch" → `main` → `/ (root)`
4. The site will be live at `https://[username].github.io/[repo-name]/`

## Credits

Simulation engine adapted from [ManyTinyThings](https://manytinythings.com), an interactive introduction to statistical thermodynamics.

## License

MIT
