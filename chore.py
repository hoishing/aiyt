from aiyt.utils import metadata

name = metadata["name"]
description = metadata["description"]
caption = "https://www.youtube.com/watch?v=uYZ4J7ctpio"
no_caption = "https://youtube.com/shorts/NbY29sW7gbU"


readme = f"""\
# {name}

> {description}

## Usage

- run with `uvx`

```bash
uvx {name}
```

- install locally

```bash
uv tool install {name}

# then run it
{name}
```

- upgrade to the lastest version

```bash
uvx {name}@latest

# upgrade installed tool
uv tool upgrade {name}@latest
```

## Questions

- [Github issue]
- [LinkedIn]

[Github issue]: https://github.com/hoishing/aiyt/issues
[LinkedIn]: https://www.linkedin.com/in/kng2
"""

if __name__ == "__main__":
    with open("./README.md", 'w') as f:
        f.write(readme)
