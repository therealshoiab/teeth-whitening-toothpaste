# 🦷 Teeth Whitening Toothpaste E-Commerce Store

[![Shopify](https://img.shields.io/badge/Platform-Shopify%20Liquid-95BF47?logo=shopify&logoColor=white)](https://theperforaa.myshopify.com)
[![GitHub Pages](https://img.shields.io/badge/Demo-GitHub%20Pages-222222?logo=github&logoColor=white)](https://therealshoiab.github.io/teeth-whitening-toothpaste/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

A luxury, high-converting direct-to-consumer (D2C) e-commerce storefront for **Perfora Teeth Whitening Toothpaste & Oral Wellness**. Built with a custom Shopify Liquid theme featuring modern glassmorphism aesthetics, fluid micro-interactions, responsive mobile-first layouts, and authentic social proof integration.

---

## 🌐 Live Demos
* **Official Live Store**: [https://theperforaa.myshopify.com](https://theperforaa.myshopify.com)
* **GitHub Pages Preview**: [https://therealshoiab.github.io/teeth-whitening-toothpaste/](https://therealshoiab.github.io/teeth-whitening-toothpaste/)

---

## ✨ Key Features & Architecture

### 1. 🎬 Luxury Hero Banner & Video Ad Showcase
* High-definition autoplay video showcasing instant color-correction science.
* Responsive viewport handling with optimized contrast overlays and typography hierarchy.

### 2. 🛡️ Trust & Guarantee Badges
* Custom vector SVG icons (Enamel-Safe, Clean & Toxic-Free, Secure UPI & COD, Free Shipping across India).
* Glassmorphism cards with smooth hover micro-interactions.

### 3. 🛍️ Dynamic Product Catalog & Quick Add
* Product cards with crisp rectangular CTAs (`border-radius: 0`).
* Dynamic pricing, sale tags, and stock indicators.
* One-click Add to Cart integrated with asynchronous cart drawer.

### 4. 📸 Verified Customer UGC Social Proof (47 Photo Reviews)
* 47 real, high-resolution unboxing and product-in-hand customer review photos.
* Responsive photo grid with expandable "Show All 47 Reviews" toggle.
* Custom Lightbox Modal displaying uncropped portrait UGC photos (`object-fit: contain`).
* Robust data-attribute event binding safe from character quotes/apostrophes.

### 5. 🛒 Glassmorphism Cart Drawer
* Sleek sliding AJAX cart drawer with backdrop blur.
* Real-time cart updates and rectangular Checkout action button.

### 6. ❓ Interactive FAQ Accordion
* Answers to common buyer questions regarding enamel safety, usage directions, and ingredients.

---

## 🛠️ Tech Stack
* **E-Commerce Platform**: Shopify
* **Templating Language**: Shopify Liquid
* **Frontend Styles**: Vanilla CSS (Custom Design System with tokens for purple brand accents, glassmorphic cards, and crisp button geometry)
* **Client Logic**: Vanilla JavaScript (ES6+)
* **Tooling**: Shopify CLI

---

## 📂 Project Structure

```text
├── theme/
│   ├── assets/           # CSS stylesheets, JS modules, and optimized UGC review images
│   ├── config/           # Theme settings schema and default presets
│   ├── layout/           # Base HTML layout templates (theme.liquid)
│   ├── locales/          # Multi-language translation files
│   ├── sections/         # Custom Liquid sections (hero, reviews, trust bar, FAQ)
│   ├── snippets/         # Modular Liquid components (buy-buttons, cart-drawer)
│   └── templates/        # JSON page templates
├── images/               # High-resolution product photography
├── new_reviews/          # Master customer review imagery
├── products-blueprint.json # Catalog specification and product metadata
├── index.html            # Standalone static showcase for GitHub Pages
└── README.md             # Project documentation
```

---

## 👨‍💻 Author

Created by **[therealshoiab](https://github.com/therealshoiab)**.
