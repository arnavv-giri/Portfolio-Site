# Customization Guide — Arnav Giri Portfolio

This guide covers how to customize the portfolio. Fire up `npm run dev` and changes will live-reload instantly.

## 🎨 Quick Wins: Basic Customizations

All edits are in `index.html` unless noted.

### 1. **Hero Section**
   - **Name & Tagline**: The `<h1>` displays "ARNAV / GIRI". Update the typewriter text in `src/main.js` (`gsap.to('#typewriter', { text: "...", ... });`).
   - **Profile Image**: Replace `/public/arnav-giri.jpeg` with your photo (aspect 4:5, <500KB). Update `src` in `<img>`.
   - **Badge**: Edit the floating "FULL STACK DEVELOPER" div for your title.
   - **Resume**: Swap `/public/arnav-giri-resume.pdf` with your own PDF. The `download` attribute triggers a file download.

### 2. **About Section**
   - **Location**: Change "ROORKEE, IND" in the heading and update the SVG map path if needed.
   - **Bio Text**: Rewrite the `<p>` paragraphs to tell your story.
   - **Stats**: In `src/main.js`, tweak `updateTimeBasedStats()` — set `birthDate` and `careerStartDate` accurately.

### 3. **Works Gallery**
   - **Add/Remove Cards**: Duplicate the `<div class="work-item">` blocks in `#works-wrapper`. Update:
     - Icon: Remix Icon class (e.g., `ri-store-3-line`).
     - Title/Desc: `<h3>` and `<p>`.
     - Tech chips: `<span>` tags in the flex-wrap div.
     - Tag badge: top-right label (e.g., "FULL STACK").
     - Number: Sequential "05", etc.
   - **Horizontal Scroll**: Adjust `gap-20` in flex for spacing.

### 4. **Skills Timeline**
   - **Add Categories**: Duplicate `<div data-gsap="service-item">` blocks. Customise:
     - Icon: Remix Icon class (e.g., `ri-cloud-line` for cloud).
     - Title/Desc: `<h3>` and `<p>`.
     - List: `<ul>` items.
   - **Alternating Layout**: Odd items go left, even items go right — keep `order-*` classes consistent.

### 5. **Contact Section**
   - **Social Links**: Update hrefs for GitHub, email, LinkedIn, LeetCode.
   - **Footer**: Change copyright name/year in `<p>&copy; ...`.

| Quick Edit | File | Pro Tip |
|------------|------|---------|
| Text/Content | `index.html` | Use semantic tags for SEO. |
| Images | `/public/` | Optimise with TinyPNG (<100KB each). |
| Stats/Age | `src/main.js` | Birthdate affects chronometer — set accurately! |
| Colors | `src/main.css` (CSS vars) | `--accent: #your-hex;` for global tweaks. |

## ⚡ Advanced Customizations

### 1. **Themes & Dark Mode**
   - Add a toggle in nav: `<button id="theme-toggle">🌙</button>`.
   - In `src/main.js`:
     ```js
     const toggle = document.getElementById('theme-toggle');
     toggle.addEventListener('click', () => {
       document.body.classList.toggle('dark');
       gsap.to('body', { backgroundColor: document.body.classList.contains('dark') ? '#111' : '#fff', duration: 0.5 });
     });
     ```
   - In `src/main.css`: Add dark variants (`@media (prefers-color-scheme: dark) { ... }`).

### 2. **Custom Animations**
   - **Hero Reveal**: Extend the loader timeline in `src/main.js` for new staggers.
   - **Magnetic Elements**: Add class `magnetic-btn` to any interactive element.
   - **Parallax**: Duplicate `.parallax-element` with custom `data-speed`.

### 3. **Performance Tweaks**
   - **Bundle Size**: In `vite.config.js`, increase `maxSizeInKb` if adding large assets.
   - **Lazy Load**: Add `loading="lazy"` to work card images.
   - **Obfuscation**: Set `controlFlowFlattening: false` in config if GSAP breaks.

### 4. **Integrations**
   - **Contact Form**: Replace social links with Netlify Forms (add `netlify` attribute to `<form>`).
   - **Analytics**: Drop GA or Plausible script in `<head>`.

## 🔧 Troubleshooting

| Issue | Cause | Fix |
|-------|-------|-----|
| **Build Fails (PostCSS)** | Missing Tailwind directives | Ensure `@tailwind base/components/utilities` are in `src/main.css`. |
| **Animations Lag** | GSAP/Lenis conflict | Call `ScrollTrigger.refresh()` after loader completes. |
| **Images 404** | Wrong path | Ensure file is in `/public/`; use absolute path `/filename.ext`. |
| **Mobile Scroll Jumps** | Lenis touch | Set `smoothTouch: true` in Lenis init. |
| **Obfuscation Breaks JS** | Heavy flattening | Set `controlFlowFlattening: false` in `vite.config.js`. |

## 📚 Resources

- **GSAP Docs**: [greensock.com/docs](https://greensock.com/docs)
- **Tailwind Playground**: [play.tailwindcss.com](https://play.tailwindcss.com)
- **Vite Guide**: [vitejs.dev/guide](https://vitejs.dev/guide)
- **Remix Icons**: [remixicon.com](https://remixicon.com)

[Back to README](README.md)
