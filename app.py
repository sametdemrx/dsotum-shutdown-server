from flask import Flask

# Flask uygulamasını başlatıyoruz
app = Flask(__name__)

# Ana sayfa route'u
@app.route('/')
def home():
    return "DSOTUM: Gölge Komut Merkezi"

# Shutdown komutunu alacak route
@app.route('/shutdown', methods=['POST'])
def shutdown():
    # Sistem kapanma işlemi burada yapılacak
    import os
    os.system("shutdown /s /f /t 1")  # Windows için, Linux/Mac için farklı komutlar kullanabilirsiniz
    return "Bilgisayar kapanıyor..."

# Uygulama başlatılıyor
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
