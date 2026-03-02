# Arnav Giri — Portfolio 🚀

A sleek, **full-stack developer portfolio** built with modern tools like **Vite**, **Tailwind CSS**, **GSAP**, and **Lenis** for buttery-smooth animations. Built by Arnav Giri, Full Stack Developer specialising in Java, Spring Boot, React, and PostgreSQL.

## ✨ Features

- **Hero Section**: Magnetic cursor, typewriter effect, and parallax text for an immersive intro.
- **Smooth Scrolling**: Powered by Lenis + GSAP ScrollTrigger – no jank, just flow.
- **Horizontal Work Scroll**: Sticky, pinned gallery with grayscale hover reveals and rotate animations.
- **Live Chronometer**: Real-time age calculator (years/months/days/hours/minutes/seconds) with progress bars.
- **Interactive Map**: SVG-based location pin with radar ping and bounce effects.
- **Timeline Skills**: Vertical progress line with staggered reveals for expertise showcase.
- **Marquee & Badges**: Infinite scrolling tags and floating credentials.
- **Single-File Build**: Obfuscated JS + inlined assets for easy deployment (under 1MB!).
- **Responsive & Accessible**: Mobile-first, with ARIA hints and semantic HTML.
- **Advanced Animations**: Bi-directional scrolls, clip-path masks, and shadow lifts.

| Feature | Tech | Why? |
|---------|------|------|
| Animations | GSAP + ScrollTrigger | Pixel-perfect, performant timelines. |
| Styling | Tailwind CSS | Rapid, utility-first design. |
| Bundling | Vite + SingleFile | Lightning-fast builds & deploys. |
| Obfuscation | JS Obfuscator Plugin | "Encrypted" code for security flair. |
| Smooth Scroll | Lenis | Native-feel scrolling without libraries. |

## 🛠 Quick Start

### Prerequisites
- Node.js (v18+)
- Git

### Installation
1. **Install Dependencies**:
   ```bash
   npm install
   ```

2. **Development Server**:
   ```bash
   npm run dev
   ```
   Open [http://localhost:5173](http://localhost:5173)

3. **Build for Production**:
   ```bash
   npm run build
   ```
   Outputs a single `dist/index.html` (obfuscated & minified).

4. **Preview Build**:
   ```bash
   npm run preview
   ```

### Customization
- **Images**: Swap files in `/public/` (e.g., `arnav-giri.jpeg` for hero).
- **Content**: Edit `index.html` sections (hero text, work cards, skills list).
- **Colors/Themes**: Tweak `--bg-color`, `--text-main` in `src/main.css`.
- **Animations**: Adjust GSAP timelines in `src/main.js`.
- **Add Projects**: Duplicate work cards in HTML; update `src` paths.

## ☁️ Deployment

### Vercel (Recommended – Free & Instant)
1. Push to GitHub.
2. Import repo at [vercel.com](https://vercel.com/import).
3. Set `vercel.json` (auto-detected for Vite).
4. Deploy – Custom domain optional!

### Other Options
- **Netlify**: Drag `/dist` or link GitHub.
- **GitHub Pages**: Use `gh-pages` branch.
- **Self-Host**: Serve `dist/` via Apache/Nginx.

## 📚 Tech Stack

![Vite](https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)
![GSAP](https://img.shields.io/badge/GSAP-88CE02?style=for-the-badge&logo=greensock&logoColor=white)
![Lenis](https://img.shields.io/badge/Lenis-000?style=for-the-badge&logo=studio-freight&logoColor=white)
![Remix Icon](https://img.shields.io/badge/Remix_Icon-18191A?style=for-the-badge&logo=remixicon&logoColor=white)

- **Build Tools**: Vite, PostCSS, Tailwind.
- **Animations**: GSAP (3.12.5), ScrollTrigger, TextPlugin.
- **Icons**: Remix Icon (4.1.0).
- **Fonts**: Inter & Space Mono (Google Fonts).
- **CDNs**: Minimal – GSAP/Lenis for speed.

## 📄 License

This project is [MIT](LICENSE) licensed – use it freely, even commercially.

---

**Arnav Giri** — Full Stack Developer | [GitHub](https://github.com/arnavv-giri) | [LinkedIn](https://www.linkedin.com/in/arnav-giri-2498101b9/) | [LeetCode](https://leetcode.com/u/arnav_giri/)
