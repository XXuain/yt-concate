import ssl

# No ssl verification
ssl._create_default_https_context = ssl._create_unverified_context
from yt_concate.pipeline.steps.get_video_list import GetVideoList
from yt_concate.pipeline.pipeline import Pipeline

CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'


def main():
    steps = [
        GetVideoList(),
    ]

    inputs = {
        'channel_id': CHANNEL_ID
    }

    p = Pipeline(steps)
    p.run(inputs)


if __name__ == '__main__':
    main()
