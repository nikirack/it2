```python
from collections.abc import Callable

handler: Callable[[str], None]
```

`handler` is something you can call with one str argument, and it returns `None`

for å legge til flere agrumenter legger man det til i listen

[example](../test/register_pattern.py)