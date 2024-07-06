from typing import List
from rxconfig import config

import reflex as rx

from reflex_qrcode import QRCode

filename = f"{config.app_name}/{config.app_name}.py"

font = "https://fonts.googleapis.com/css2?family=Manrope:wght@200..800&display=swap"

gradient = "linear-gradient( 58.2deg,  rgba(40,91,212,0.73) -3%, rgba(171,53,163,0.45) 49.3%, rgba(255,204,112,0.37) 97.7% );"

class State(rx.State):
    """The app state."""

    qrSize: List[int] = [256, 128, 64, 32, 16]

    qrLevel: List[str] = ["L", "M", "Q", "H"]

    @rx.var
    def sv_qrSize(self) -> List[int]:
        return self.qrSize
    
    @rx.var
    def sv_qrLevel(self) -> List[str]:
        return self.qrLevel

QRVALUE = "https://reflex.dev"

def index() -> rx.Component:
    return rx.center(
        rx.flex(
            rx.text("Reflex ", rx.text.strong("QRCode"), " Demo", size="8"),
            rx.text("Based on ", rx.link("react-qr-code", href="https://www.npmjs.com/package/react-qr-code"), size="2"),
            rx.foreach(
                State.sv_qrSize, 
                lambda size:
                    rx.flex(
                        rx.foreach(
                            State.sv_qrLevel, 
                            lambda level:
                                rx.card(
                                    rx.flex(
                                        QRCode(
                                            title=QRVALUE,
                                            value=QRVALUE,
                                            level=level,
                                            size=size
                                        ),
                                        rx.flex(
                                            rx.text(
                                                "Title: ",
                                                rx.text.strong(QRVALUE),
                                                size="2"
                                            ),
                                            rx.text(
                                                "Value: ", 
                                                rx.text.strong(QRVALUE),
                                                size="2"
                                            ),
                                            rx.text(
                                                "Level: ", 
                                                rx.text.strong(level),
                                                size="2"
                                            ),
                                            rx.text(
                                                "Size: ", 
                                                rx.text.strong(size),
                                                size="2"
                                            ),
                                            direction="column",
                                            spacing="0"
                                        ),
                                        direction="column",
                                        spacing="2"
                                    )
                                )
                        ),
                        direction="row",
                        spacing="4"
                    )
            ),
            rx.flex(
                rx.badge(
                    rx.text(
                        "Made with and for "
                    ),
                    rx.color_mode_cond(
                        dark=rx.image(
                            src="https://reflex.dev/logos/dark/reflex.svg", width="45px",
                        ),
                        light=rx.image(
                            src="https://reflex.dev/logos/light/reflex.svg", width="45px",
                        )
                    )
                ),
                rx.color_mode.button(
                    size="1", 
                    variant="ghost"
                ),
                direction="row",
                spacing="2",
                align="center",
            ),
            direction="column",
            justify="center",
            align="center",
            spacing="4",
            padding="4",
            margin_top="2em",
            margin_bottom="2em",
            height="100%",
            width="100%",
            wrap="wrap",
        ),
        height="100%",
        background=gradient,
    )


# Add state and page to the app.
app = rx.App(stylesheets=[font], style={"fontFamily": "Manrope"})
app.add_page(index)
