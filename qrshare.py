import argparse
import logging
import os
from pathlib import Path
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import SquareModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask

logging.basicConfig(level=logging.INFO, format="%(levelname)s | %(message)s")

def resolve_args() -> argparse.Namespace:
    NAME    = "QR Share"
    FILE    = os.path.splitext(os.path.basename(__file__))[0]
    VERSION = "1.1.0"
    DESC    = "Receives text and displays it as a QR code."

    parser = argparse.ArgumentParser(
        prog        = FILE,
        description = DESC
    )

    parser.add_argument("data",
                        help="the text encoded in the QR code, e. g. 'https://www.qrcode.com'.")
    parser.add_argument("-e", "--embed",
                        help="embed a custom image in the centre of the QR code by specifying "\
                        "a path as [EMBED] or use a default image by omitting the positional "\
                        "argument",
                        default=None, # value if -e is not specified
                        const="",     # value if -e is specified but no argument is given
                        nargs="?")
    parser.add_argument("-v", "--version",
                        action="version",
                        version=f"{NAME} {VERSION}")
    return parser.parse_args()

def make_qr(data: str, embed: str = None) -> StyledPilImage:
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(data)
    qr.make(fit=True)

    img: StyledPilImage = qr.make_image(image_factory=StyledPilImage,
                                        color_mask=SolidFillColorMask(),
                                        module_drawer=SquareModuleDrawer(),
                                        embeded_image_path=embed)

    return img

if __name__ == "__main__":
    args = resolve_args()
    data = args.data
    embed = args.embed

    basedir = os.path.dirname(__file__)
    logging.debug(f'Base directory: {basedir}')

    if embed is not None:
        logging.debug(f'Embed enabled with value: "{embed}"')

        if embed == "":
            embed = os.path.join(basedir, 'embed.jpg')
            logging.debug(f'Selecting default embed: {embed}')
        elif not Path(embed).is_file():
            logging.warning(f'Could not find file to embed: "{embed}"')
            embed = None

    img = make_qr(data, embed)
    img.show()
