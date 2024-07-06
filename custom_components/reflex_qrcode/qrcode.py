"""Reflex custom component QRCode."""

# For wrapping react guide, visit https://reflex.dev/docs/wrapping-react/overview/

from typing import Literal
import reflex as rx

LiteralLevelTypes = Literal["L", "M", "Q", "H"]

class QRCode(rx.Component):
    """QRCode component."""

    library = "react-qr-code" # https://www.npmjs.com/package/react-qr-code

    tag = "QRCode"

    is_default = True

    # Props
    title: rx.Var[str] = ""
    
    value: rx.Var[str] = ""
    
    level: rx.Var[LiteralLevelTypes] = "L"
    
    size: rx.Var[int] = 256

QRCode = QRCode.create