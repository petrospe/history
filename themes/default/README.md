# Default theme (extended)

This directory is Pico’s **default** theme with **site-specific** layout, palettes, and behaviour. It stays compatible with Pico 2.x and the usual `pico-theme.yml` meta headers.

[Pico CMS](https://picocms.org/) — flat-file, no database.

## Features

### Layout

- **Header** (CSS Grid): branding (logo + site title + tagline from `_meta.md`), **theme** dropdown (`Θέμα`), then **main navigation** (`#nav`).
- **Footer**: optional social links from `_meta.md`.
- **Responsive menu**: hamburger toggles `#nav` on small viewports (`js/pico.js` + `utils.js`).
- **Back to top**: floating button when the header scrolls out of view.

### Colour schemes

Three palettes, switched via a header `<select>` (choice stored in `localStorage` under `pico-color-scheme`):

| Option   | Class on `<html>` | Notes |
|----------|-------------------|--------|
| Θερμό    | *(none)*          | Warm sand/beige custom palette (`:root` in `css/style.css`). |
| Pico     | `theme-pico`      | Classic stock Pico teal / grey look. |
| Σκοτεινό | `theme-dark`      | Dark UI with teal accents. |

**Server default** (first visit, no `localStorage`): set in `config/config.yml`:

```yaml
theme_config:
    widescreen: false      # optional: wider `.container`
    color_scheme: default  # default | pico | dark
```

A small script in `<head>` applies `localStorage` before paint; `js/pico.js` keeps `theme-pico` / `theme-dark` when toggling the `js` class (it does **not** replace the whole `<html>` `className`).

### Logo (Pico SVG + dark theme)

If `content/_meta.md` points the logo at a path containing **`pico.svg`**, the **Σκοτεινό** scheme uses **`img/pico-white.svg`** automatically (`data-logo-light` / `data-logo-dark` + `syncThemeLogo` in `pico.js`). Other logo URLs are unchanged.

### Navigation order

Top-level pages are sorted by the numeric meta field **`order`** (ascending), configured in **`config/config.yml`**:

```yaml
pages_order_by: meta
pages_order_by_meta: order
pages_order: asc
```

Add to each page’s YAML, e.g. `order: 20`. Pages without `order` fall back after ordered pages (Pico’s meta sort rules).

### Typography and tables

- **Body paragraphs**: `text-align: justify` (outside tables).
- **Tables**: **`td`** — left-aligned; **`th`** — centered; paragraphs inside **`td`** are left-aligned so they don’t inherit justify.

### Site metadata (`content/_meta.md`)

Registered in `pico-theme.yml`:

```yaml
Logo: %theme_url%/img/pico.svg
Tagline: …
Social:
    - title: …
      url: …
      icon: …      # theme icon names (e.g. octocat, chat, link)
      newtab: true # optional
```

## Configuration reference

| Location | Purpose |
|----------|---------|
| `config/config.yml` | `site_title`, `theme`, `theme_config` (`widescreen`, `color_scheme`), `pages_order_by*` |
| `themes/default/pico-theme.yml` | Theme API version, meta header mapping, default `widescreen` |
| `themes/default/index.twig` | Markup: header, nav, footer, scripts |
| `themes/default/css/style.css` | Palettes (`:root`, `.theme-pico`, `.theme-dark`), layout, tables |
| `themes/default/js/pico.js` | Menu, back-to-top, colour scheme + logo sync |

## Copying this theme

To use it as a separate theme, copy `themes/default` to e.g. `themes/my_theme`, set `theme: my_theme` in `config/config.yml`, and adjust as needed.
