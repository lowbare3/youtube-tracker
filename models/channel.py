class ChannelAudit:
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.description_score = 0
        self.description_status = ""
        self.video_score = 0
        self.video_status = ""
        self.subscribers = 0
        self.video_count = 0