import js  # 🤯


class Pylit:
    """Make a styled custom element for the browser 💅"""

    def __init__(self, element):
        self.element = element

    @property
    def css(self) -> str:
        return ""

    def attach_css(self):
        if self.css:
            el = js.document.createElement("style")
            el.textContent = self.css
            self.element.shadowRoot.appendChild(el)

    def connect(self):
        self.attach_css()
        self.render()
