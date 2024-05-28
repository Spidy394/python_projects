import qrcode

def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    return img

def display_qr_code(img):
    img.show()

if __name__ == "__main__":
    print("|| Welcome to QR Code Generator ||")
    data = input("Enter link: ")
    
    qr_image = generate_qr_code(data)

    display_qr_code(qr_image)
