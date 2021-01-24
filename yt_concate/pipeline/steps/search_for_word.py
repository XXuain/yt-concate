from yt_concate.pipeline.steps.step import Step

class SearchWord(Step):
    def process(self, data, inputs, utils):
        search_word = inputs['search_word']

        found = []
        for yt in data:
            captions = yt.captions
            for caption in captions:
                if search_word in caption:
                    time = captions[caption]
                    found.append((yt, caption, time))
        
        return found