# Air and Space Dictionary

Comprehensive technical dictionary covering aerodynamics, aerospace, rocket and missile systems, drones, and space science.

## Overview

- **Pages**: 201
- **Entries**: ~1,499
- **Format**: Two-column dictionary style
- **Build**: pdflatex, clean compilation

## Contents

| Chapter | Entries | Lines |
|---------|---------|-------|
| 1. Aerodynamics | 390 | 430 |
| 2. Aerospace | 261 | 569 |
| 3. Rocket and Missile | 286 | 573 |
| 4. Drones | 301 | 307 |
| 5. Space Science | 261 | 528 |

## Build

```bash
pdflatex main.tex
makeglossaries main
pdflatex main.tex
pdflatex main.tex
```

Or single pass:
```bash
pdflatex -interaction=nonstopmode main.tex
```

## Structure

```
main.tex              # Master document
chapters/
  chapter1_aerodynamics.tex
  chapter2_aerospace.tex
  chapter3_rocket_missile.tex
  chapter4_drones.tex
  chapter5_spacescience.tex
main.pdf              # Compiled output
```

## Format

Each entry uses the `\dictentry{term}{definition}{color_category}` command.

Color categories:
- `catAD` - Aerodynamics (blue)
- `catAE` - Aerospace (light blue)
- `catRM` - Rocket/Missile (red)
- `catD` - Drones (teal)
- `catSS` - Space Science (purple)

## Requirements

- TeX Live 2023+ or MiKTeX
- LaTeX packages: glossaries, multicol, fancyhdr, hyperref, xcolor
