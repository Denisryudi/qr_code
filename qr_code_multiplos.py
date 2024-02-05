import qrcode
from qrcode.image.styledpil import StyledPilImage

redes_sociais = {
    'Site': 'https://20parkhotel.com.br',
    'Facebook': 'https://www.facebook.com/20parkhotelltda',
    'Instagram': 'https://www.instagram.com/20parkhotel?igsh=MWs4Y3h2bTdwMjI4OA=='
}

for rede_social, url in redes_sociais.items():
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(url)

    imagem = qr.make_image(
        image_factory=StyledPilImage,
        embeded_image_path='logo1.png'

    )
    imagem.save(f'sociais_{rede_social}.png')




