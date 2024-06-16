from flask import Flask, request, render_template 
import qrcode
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.secret_key = '12345678'
@app.route('/', methods=['POST', 'GET'])
def generate_qr():    
    if request.method == 'POST':
        data = request.form.get('txt')
        name = request.form.get('name')
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=3,border=4)
        qr.add_data(data)
        qr.make(fit=True)
        colors = {
            "قرمز": "red",
            "آبی پررنگ": "blue",
            "آبی": "blue",
            "آبی کم رنگ": "cyan",
            "بنفش": "purple",
            "صورتی": "violet",
            "مشکی": "black",
            "سیاه": "black",
            "سفید": "white",
            "خاکستری": "gray",
        }
        try:
            kwf = request.form.get('color')
            kwb = request.form.get('bg')
            if kwf in colors:
                fill_color = colors[kwf]
            else: 
                fill_color = 'black'
            if kwb in colors:
                back_color = colors[kwb]
            else: 
                back_color = 'white'
        except:
            fill_color = 'black'
            back_color = 'white'
        img = qr.make_image(fill_color=fill_color, back_color=back_color)
        img.save(f"static/qrcodes_img/{name}.png")
        return render_template('QR code.html', qr=f'static/qrcodes_img/{name}.png')
    return render_template('QR code.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)