# lifehacks.colour [![publish](https://github.com/mightbesimon/lifehacks.colour/actions/workflows/publish.yml/badge.svg)](https://github.com/mightbesimon/lifehacks.colour)

## Structure

```plaintext
📦lifehacks.colour
├── Colour
├── hsla
├── rgba
└── 📦palette
    ├── Apple
    └── Mariana
```

## Installation

```bash
pip install lifehacks.colour
```

## Usage

- [`Colour` abstract class](#colour-abstract-class)
- [`hsla`](#hsla)
- [`rgba`](#rgba)
- [`Mariana` palette](#mariana-palette)

### `Colour` abstract class

Abstract base class, not instantiable.
Can be used in type hinting for `hsla` and `rgba` instances

```python
def print_hex(colour:Colour) -> None:
	print(colour.to_hex())

print_hex(rgba(15, 15, 15))	#0f0f0f
print_hex(hsla( 0,  0,  6))	#0f0f0f
```

### `hsla`

- optional `h`: hue `[0, 359]`
- optional `s`: saturation `[0, 100]` or `[0.0, 1.0]`
- optional `l`: lightness `[0, 100]` or `[0.0, 1.0]`
- optional `a`: alpha (opacity) `[0, 100]` or `[0.0, 1.0]`

### `rgba`

- optional `r`: red `[0, 255]`
- optional `g`: green `[0, 255]`
- optional `b`: blue `[0, 255]`
- optional `a`: alpha `[0, 100]` or `[0.0, 1.0]`

### `Mariana` palette

Remember to import from `lifehacks.colour.palette`.
This palette contains the colours from Mariana theme in Sublime Text.

```python
from lifhacks.colour.palette import Mariana

for name, colour in Mariana:
    content = content.replace(name, colour.to_hex())
```

## Contributors

- **Simon** - [mightbesimon](https://github.com/mightbesimon)
- you?
