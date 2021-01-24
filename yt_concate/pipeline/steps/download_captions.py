#download the package by:  pip install pytube
import pytube
from pytube import YouTube
from .step import Step

import time


class DownLoadCaptions(Step):
    def process(self, data, inputs, utils):
        start = time.time()
        for yt in data:
            print('DownLoadCaptions: ', yt.id)
            if utils.caption_file_exists(yt.url):
                print('Check existing caption file for url', yt.url)
                continue

            try:
                source = YouTube(yt.url)
                en_caption = source.captions.get_by_language_code('a.en')
                en_caption_convert_to_srt = en_caption.generate_srt_captions()
            except (KeyError, AttributeError, pytube.exceptions.RegexMatchError) as e:
                print('Found an Error: ', e, 'while downloading the caption for')
                continue

            # save the caption to a file named Output.txt
            text_file = open(utils.get_caption_path(yt.url), "w", encoding='utf-8')
            text_file.write(en_caption_convert_to_srt)
            text_file.close()

        end = time.time()
        print('took', end - start, 'second')
