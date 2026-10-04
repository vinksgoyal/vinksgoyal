from pathlib import Path
from html import escape

INPUT = "portrait.txt"
OUTPUT = "dark.svg"  # Save directly as your target SVG file

# SVG placement settings
START_X = 64
START_Y = 66
LINE_HEIGHT = 22

# Optional trimming
TRIM_LEFT = 0
TRIM_RIGHT = 0
REMOVE_EMPTY = False

# Read input lines
lines = Path(INPUT).read_text(
    encoding="utf-8",
    errors="ignore"
).splitlines()

lines = [l.rstrip() for l in lines]

if REMOVE_EMPTY:
    lines = [l for l in lines if l.strip()]

processed = []
for line in lines:
    if TRIM_RIGHT > 0:
        line = line[:-TRIM_RIGHT]
    if TRIM_LEFT > 0:
        line = line[TRIM_LEFT:]
    processed.append(line)

# Generate tspans with relative vertical positioning
tspans = []
y = START_Y
for line in processed:
    tspans.append(f'<tspan x="{START_X}" y="{y}" xml:space="preserve">{escape(line)}</tspan>')
    y += LINE_HEIGHT

# Wrap in a clean SVG template container
svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" width="1180" height="610" viewBox="0 0 1180 610">
<style>
  .ascii {{ font-family: 'Courier New', Consolas, monospace; font-size: 15px; fill: #00F2FE; }}
</style>
<rect width="1180" height="610" rx="18" fill="#0A0B10"/>
<text class="ascii">
{''.join(tspans)}
</text>
</svg>
"""

Path(OUTPUT).write_text(svg_content, encoding="utf-8")
print(f"Successfully generated {OUTPUT} with {len(tspans)} text lines.")
