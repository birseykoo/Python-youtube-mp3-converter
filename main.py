from flask import Flask, request, render_template_string
from pytube import YouTube
from moviepy.editor import *
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        video_url = request.form['url']
        try:
            # Youtube videosunu çeker
            yt = YouTube(video_url)

            # Videoyu en yüksek kalitede indirir
            video = yt.streams.get_highest_resolution()
            video.download()

            # İndirilen video dosyasının yolunu ayarlar
            video_path = video.default_filename

            print(f"Video indirildi: {video_path}")

            # Sesi ayıklar ve MP3 olarak kaydeder
            mp4_file = video_path
            mp3_file = video_path[:-4] + '.mp3'
            video = VideoFileClip(mp4_file)
            video.audio.write_audiofile(mp3_file)

            video.close()
            os.remove(mp4_file)

            return f"MP3 dosyası '{mp3_file}' başarıyla oluşturuldu!"
        except Exception as e:
            return f"Error: {str(e)}"
    return '''
        <form method="POST">
            YouTube Video URL: <input type="text" name="url">
            <input type="submit" value="Convert to MP3">
        </form>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
