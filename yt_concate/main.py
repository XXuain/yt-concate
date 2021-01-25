import ssl

# No ssl verification
ssl._create_default_https_context = ssl._create_unverified_context

from yt_concate.pipeline.steps.preflight import Preflight
from yt_concate.pipeline.steps.get_video_list import GetVideoList
from yt_concate.pipeline.steps.initializeYT import InitializeYT
from yt_concate.pipeline.steps.download_captions import DownLoadCaptions
from yt_concate.pipeline.steps.read_caption import ReadCaption
from yt_concate.pipeline.steps.search_for_word import SearchWord
from yt_concate.pipeline.steps.download_videos import DownloadVideos
from yt_concate.pipeline.steps.postflight import Postflight
from yt_concate.pipeline.pipeline import Pipeline
from yt_concate.utils import Utils

CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'


def main():
    steps = [
        Preflight(),
        GetVideoList(),
        InitializeYT(),
        DownLoadCaptions(),
        ReadCaption(),
        SearchWord(),
        DownloadVideos(),
        Postflight(),
    ]

    inputs = {
        'channel_id': CHANNEL_ID,
        'search_word': 'incredible',
    }

    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == '__main__':
    main()
