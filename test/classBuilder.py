class Post:
    def __init__(self, title:str, text:str, category:str) -> None:
        self.title: str = title
        self.text: str = text
        self.category: str = category

    class Builder:

        def __init__(self):
            self._title: str | None = None
            self._text: str | None = None
            self._category: str | None = None

        def title(self, value:str):
            self._title = value
            return self

        def text(self, value: str):
            self._text = value
            return self

        def category(self, value: str):
            self._category = value
            return self

        def build(self):
            missing: list[str] = []

            if self._title is None:
                missing.append("title")
            if self._text is None:
                missing.append("text")
            if self._category is None:
                missing.append("category")

            if missing:
                raise ValueError(
                    f"Missing required fields: {', '.join(missing)}"
                )

            assert self._title is not None
            assert self._text is not None
            assert self._category is not None

            return Post(
                self._title,
                self._text,
                self._category
            )
        
bost = Post.Builder().title("a").text("a").category("a").build()