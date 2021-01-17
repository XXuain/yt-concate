import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('API_KEY')

# 下載
DOWNLOADS_DIR = 'downloads'
VIDEOS_DIR = os.path.join(DOWNLOADS_DIR, 'videos') # 影片 URL
CAPTIONS_DIR = os.path.join(DOWNLOADS_DIR, 'captions') # 字幕資料夾
