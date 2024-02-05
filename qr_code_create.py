import qrcode

imagem = qrcode.make('https://20parkhotel.com.br')
imagem.save('qrcode.png')

