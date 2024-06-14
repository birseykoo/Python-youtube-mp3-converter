# YouTube to MP3 Converter

Bu proje, YouTube videolarını MP3 dosyalarına dönüştürmek için basit bir web uygulaması sağlar. Kullanıcı, YouTube video URL'sini girerek videoyu MP3 formatında indirebilir.

## Gereksinimler

- Python 3.x
- Flask
- Pytube
- MoviePy

## Kurulum

1. Bu projeyi kendi Replit hesabınıza fork edin veya klonlayın.
2. Gerekli bağımlılıkları yükleyin:
   ```sh
   pip install flask pytube moviepy

## Kullanım

- 'main.py' dosyasını çalıştırın:

```sh
python main.py
```
- Açılan web sayfasında, YouTube video URL'sini girin ve "Convert to MP3" butonuna tıklayın.
- Dönüştürme işlemi tamamlandıktan sonra sonuç mesajını göreceksiniz.

## Dosya Yapısı
`main.py`: Flask tabanlı web uygulaması.
`requirements.txt`: Projenin bağımlılıklarını listeleyen dosya (isteğe bağlı).
`README.md`: Proje hakkında bilgi veren dosya.

## Örnek Kullanım

Web arayüzü şu şekildedir:

```html
<form method="POST">
    YouTube Video URL: <input type="text" name="url">
    <input type="submit" value="Convert to MP3">
</form>
```
<form method="POST">
    YouTube Video URL: <input type="text" name="url">
    <input type="submit" value="Convert to MP3">
</form>

Kullanıcı, YouTube video URL'sini girip "Convert to MP3" butonuna tıkladığında video indirilir, ses dosyası MP3 formatına dönüştürülür ve işlem tamamlandığında kullanıcıya bir mesaj gösterilir.