import os
from yt_concate.settings import VIDEOS_DIR
from yt_concate.settings import CAPTIONS_DIR

class YT:
    def __init__(self, url):
        self.url = url
        self.id = self.get_video_id_from_url(self.url)
        self.caption_filePath = self.get_caption_path()
        self.video_filePath = self.get_video_path()
        self.captions = None

    @staticmethod
    def get_video_id_from_url(url):
        return url.split('watch?v=')[-1]

    # 用 id 命名為字幕檔案名稱
    def get_caption_path(self):
        return os.path.join(CAPTIONS_DIR, self.id + '.txt')

    def get_video_path(self):
        return os.path.join(VIDEOS_DIR, self.id + '.txt')

    def __str__(self):
        return '<YT(yt=' + self.id + ')>'

    def __repr__(self):
        content = ' : '.join([
            'id=' + str(self.id),
            'caption_filePath=' + str(self.caption_filePath),
            'video_filePath=' + str(self.video_filePath)
        ])
        return '<YT(' + content + ')>'