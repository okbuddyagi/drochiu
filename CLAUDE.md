# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Chinese health and wellness book titled "趙醫生的人生之道" (Dr. Chiu's Philosophy of Life) published using MkDocs with Material theme. The content is organized into chapters covering sleep, nutrition, exercise, happiness, and common health issues.

## Build & Deployment

**Build locally:**
```bash
pip install mkdocs-material mkdocs-roamlinks-plugin mkdocs-rss-plugin
mkdocs serve
```

**Deploy to GitHub Pages:**
- Deployment is automated via GitHub Actions (`.github/workflows/ci.yml`)
- Triggers on pushes to `main` or `master` branch
- Installs dependencies and runs `mkdocs gh-deploy --force`

## Content Structure

- **docs/**: Main content directory containing Markdown files
  - Organized by chapters (睡眠/, 營養/, 運動/, 長期病/)
  - Uses Traditional Chinese throughout
  - Supports [[wikilinks]] for cross-references via roamlinks plugin
- **mkdocs.yml**: Main configuration file
- **docs/stylesheets/extra.css**: Custom styling (increases font size to 2.5em)

## Configuration Details

- **Language**: Traditional Chinese (zh-Hant)
- **Theme**: Material with light/dark mode toggle
- **Font**: Noto Sans Traditional Chinese
- **Extensions**: Supports footnotes, task lists, mathematical expressions via MathJax, Mermaid diagrams
- **Plugins**: Search and roamlinks (for Obsidian-style linking)

## Content Guidelines

- All content is in Traditional Chinese
- Health-focused topics covering lifestyle, nutrition, sleep, exercise
- Uses Markdown with extensions for enhanced formatting
- Cross-references use [[wikilink]] syntax
- Mathematical expressions supported via MathJax

## Development Notes

- This is a documentation-only project with no application code
- Content can be edited directly in Markdown files
- Preview changes locally with `mkdocs serve` before committing
- GitHub Actions handles automatic deployment to GitHub Pages
- The content pages have section / subsection titles, and also in-line titles (i.e.. **Title** Content text...)