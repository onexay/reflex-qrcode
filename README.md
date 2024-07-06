# QRCode

A Reflex custom component for QRCodes based on [react-qr-code](https://github.com/onexay/reflex-qrcode/blob/main/qrcode_demo/qrcode_demo/qrcode_demo.py) component.

## Installation

### PIP

```bash
pip install reflex-qrcode
```

### Poetry

```bash
poetry add reflex-qrcode
```

## Usage

### Props

* `title`: [`str`] - Title of the QRCode, shows up as tooltip
* `value`: [`str`] - Value for which QRCode is generated
* `level`: [`str`] - QRCode level, valid values are `L`, `M`, `Q` and `H`. Default is `L`
* `size`: [`int`] - QCode size (square), maximum value is `256`

```python
from reflex_qrcode import QRCode

def index():
    return QRCode(
        title="Title", 
        value="Value"
    )

```

See [demo code]() for details.
