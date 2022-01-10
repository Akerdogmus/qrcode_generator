"""
Basic QR Code Generator.
Author: @akerdogmus
"""
import sys
import pyqrcode

class QRCodeGenerator():
    """
    QR Code Generator class
    """
    def __init__(self):
        # String which represents the QR code
        self.qr_string = sys.argv[1]

        if self.qr_string == ("-h" or "--help"):
            self.help_section()
        else:
            # generated QR name
            self.qr_code_name = sys.argv[2]
            self.qrcode_generator()

    def qrcode_generator(self):
        """ QR Code generator function"""
        # Generate QR code
        generated_url = pyqrcode.create(self.qr_string)
        # Create and save the svg file.
        generated_url.svg(self.qr_code_name + ".svg", scale = 8)
        # Create and save the png file.
        generated_url.png(self.qr_code_name + '.png', scale = 6)

    @classmethod
    def help_section(cls):
        """Help section function"""
        print("QR Code Generator. Use 'python3 qrcode_generator.py"+\
            " {qr_code_string} {generated_qr_code_name}'")

if __name__ == '__main__':
    try:
        QRCodeGenerator()
    except IndexError:
        print("QR Code Generator. For usage help, use 'python3 qrcode_generator.py -h'")
