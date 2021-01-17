import urllib.request
import json

from yt_concate.settings import API_KEY
from yt_concate.pipeline.steps.step import Step


class GetVideoList(Step):
    def process(self, data, inputs, utils):
        channel_id = inputs['channel_id']

        # 檢查
        if utils.video_list_file_exits(channel_id):
            print('Check existing video list file for channel id', channel_id)
            return self.read_to_file(utils.get_video_list_filePath(channel_id))

        # 下載
        api_key = API_KEY
        base_video_url = 'https://www.youtube.com/watch?v='
        base_search_url = 'https://www.googleapis.com/youtube/v3/search?'
        first_url = base_search_url + 'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(api_key,
                                                                                                            channel_id)

        video_links = []
        url = first_url
        while True:
            inp = urllib.request.urlopen(url)
            resp = json.load(inp)

            for i in resp['items']:
                if i['id']['kind'] == "youtube#video":
                    video_links.append(base_video_url + i['id']['videoId'])

            try:
                next_page_token = resp['nextPageToken']
                url = first_url + '&pageToken={}'.format(next_page_token)
            except KeyError:
                break

        print(video_links)
        self.write_to_file(video_links, utils.get_video_list_filePath(channel_id))
        return video_links

    def write_to_file(self, vedio_links, file_path):
        with open(file_path, 'w') as f:
            for url in vedio_links:
                f.write(url + '\n')

    def read_to_file\
                    (self, file_path):
        video_links = []
        with open(file_path, 'r') as f:
            for url in f:
                video_links.append(url.strip())
        return video_links