from pyscript import Plugin

from client.pylit import Pylit


plugin = Plugin("ResponsiveImage")


@plugin.register_custom_element("responsive-image")
class ResponsiveImage(Pylit):
    """An image that fluidly resizes to its container width"""

    @property
    def css(self) -> str:
        return """:host {
    display: inline-block;
}

::slotted(img) {
    max-width: 100%;
}

:host([grow="true"]) {
    width: 100%;
}

:host([grow="true"]) ::slotted(img) {
    width: 100%;
}"""
