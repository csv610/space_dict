# Air and Space Dictionary

A comprehensive technical reference covering **1,499 entries** across five domains of aerospace science. Built with LaTeX using a two-column dictionary layout with color-coded categories and auto-generated index.

## Contents

| # | Chapter | Entries | Lines |
|---|---------|---------|-------|
| 1 | Aerodynamics | 390 | 430 |
| 2 | Aerospace | 261 | 569 |
| 3 | Rocket and Missile | 286 | 573 |
| 4 | Drones | 301 | 307 |
| 5 | Space Science | 261 | 528 |

## Quick Start

### Prerequisites

- TeX Live 2023+ or MiKTeX
- Python 3.6+ (for deduplication script)

### Build the PDF

```bash
pdflatex space_dict.tex
makeglossaries space_dict
pdflatex space_dict.tex
pdflatex space_dict.tex
```

### Single Pass (Quick Preview)

```bash
pdflatex -interaction=nonstopmode space_dict.tex
```

## Project Structure

```
SpaceDict/
├── space_dict.tex                        # Master document
├── main.pdf                              # Compiled output (201 pages)
├── chapters/
│   ├── chapter1_aerodynamics.tex         # 390 entries
│   ├── chapter2_aerospace.tex            # 261 entries
│   ├── chapter3_rocket_missile.tex       # 286 entries
│   ├── chapter4_drones.tex               # 301 entries
│   └── chapter5_spacescience.tex         # 261 entries
├── dedupe.py                             # Cross-chapter deduplication tool
└── lines.txt                             # Line count reference
```

## Adding Entries

Each entry uses the `\dictentry` command:

```latex
\dictentry{Term}{Definition text}{category}
```

### Color Categories

| Category | Code | Color | Domain |
|----------|------|-------|--------|
| `catAD` | Blue | RGB(0, 90, 150) | Aerodynamics |
| `catAE` | Light Blue | RGB(50, 120, 200) | Aerospace |
| `catRM` | Red | RGB(180, 30, 30) | Rocket & Missile |
| `catD` | Teal | RGB(20, 140, 130) | Drones |
| `catSS` | Purple | RGB(120, 40, 160) | Space Science |

## Deduplication

The `dedupe.py` script resolves duplicate entries across chapters, keeping the most detailed version. To run:

```bash
python3 dedupe.py
```

## Requirements

| Package | Purpose |
|---------|---------|
| `glossaries` | Auto-generated index |
| `multicol` | Two-column layout |
| `fancyhdr` | Page headers |
| `hyperref` | Clickable cross-references |
| `xcolor` | Entry color coding |
| `microtype` | Typography refinement |
| `geometry` | Page margins |

## License

This is a personal reference work. For reuse, contact the author.
