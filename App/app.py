from flask import Flask, request, send_file
import qrcode
from io import BytesIO

app = Flask(__name__)

@app.route('/generate-qr', methods=['GET'])
def generate_qr():
    # Obține URL-ul din parametrul 'url' al cererii
    url = request.args.get('url')
    
    if not url:
        return "Te rog să furnizezi un URL folosind parametrul 'url'.", 400
    
    # Creează un obiect QR code
    qr = qrcode.QRCode(
        version=1,  # Dimensiunea codului QR (1-40, 1 fiind cel mai mic)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Nivel de corecție a erorilor
        box_size=10,  # Dimensiunea fiecărui "box" din QR code
        border=4,     # Grosimea bordurii
    )
    
    # Adaugă URL-ul în codul QR
    qr.add_data(url)
    qr.make(fit=True)
    
    # Creează o imagine QR code
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Salvează imaginea într-un buffer de memorie
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    
    # Returnează imaginea ca răspuns HTTP
    return send_file(buffer, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)