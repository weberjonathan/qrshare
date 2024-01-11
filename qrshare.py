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
    VERSION = "1.0.2"
    DESC    = "Receives text and displays it as a QR code. When embedding an image "\
              "in the centre of the QR code and both -e and -d are used, the option "\
              "that is specified last takes precedence."

    parser = argparse.ArgumentParser(
        prog        = FILE,
        description = DESC
    )

    parser.add_argument("data",
                        help="the text encoded in the QR code, e. g. 'https://www.qrcode.com'.")
    parser.add_argument("-d", "--embed-default",
                        action="store_const",
                        const="embed.jpg",
                        dest="embed",
                        help='embed the default image "embed.jpg" in the center of the QR code')
    parser.add_argument("-e", "--embed",
                        help="path to an image file that will be embedded in the centre of the QR code",
                        default="test")
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
        if embed == "embed.jpg": # TODO decouple embed-default and embed, so magic "embed.jpg" is no longer reserved
            embed = os.path.join(basedir, embed)

        if not Path(embed).is_file():
            logging.warning(f'Could not find file to embed: "{embed}"')
            embed = None

    img = make_qr(data, embed)
    img.show()
