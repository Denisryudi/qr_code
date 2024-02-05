import qrcode
from qrcode.image.styledpil import StyledPilImage

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
qr.add_data('https://20parkhotel.com.br/')

imagem = qr.make_image(
    image_factory=StyledPilImage,
    embeded_image_path='logo1.png'
)
imagem.save('qrcode_logo1.png')
