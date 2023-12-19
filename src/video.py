import os
from googleapiclient.discovery import build

api_key: str = os.getenv('API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)


class Video:
    def __init__(self, video_id):
        """Инициализация атрибутов экземпляра класса Video"""
        self.video_id = video_id
        video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                               id=video_id
                                               ).execute()

        self.video_title: str = video_response['items'][0]['snippet']['title']
        self.url_video = f'https://www.youtube.com/watch?v={self.video_id}'
        self.view_count: int = video_response['items'][0]['statistics']['viewCount']
        self.like_count: int = video_response['items'][0]['statistics']['likeCount']

    def __str__(self):
        return f'{self.video_title}'


class PLVideo(Video):
    def __init__(self, ip_video, playlist_id):
        super().__init__(ip_video)
        self.playlist_id = playlist_id
