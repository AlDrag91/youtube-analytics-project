import os
from datetime import timedelta

import isodate
from googleapiclient.discovery import build

api_key: str = os.getenv('API_KEY')


class PlayList:

    def __init__(self, playlist_id):
        """Инициализируется атрибуты для работать"""
        self.youtube = build('youtube', 'v3', developerKey=api_key)
        self.playlist_id = playlist_id
        self.playlist = self.youtube.playlists().list(part='snippet', id=playlist_id).execute()
        self.title = self.playlist['items'][0]['snippet']['title']
        self.url = f"https://www.youtube.com/playlist?list={self.playlist_id}"
        self.playlist_videos = self.youtube.playlistItems().list(playlistId=playlist_id,
                                                                 part='contentDetails',
                                                                 maxResults=50,
                                                                 ).execute()
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.playlist_videos['items']]
        self.video_response = self.youtube.videos().list(part='contentDetails,statistics',
                                                         id=','.join(video_ids)
                                                         ).execute()

    @property
    def total_duration(self):
        """Находим сумму длительности плейлиста"""
        total_duration = timedelta()

        for video in self.video_response['items']:
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            total_duration += duration
        return total_duration

    def show_best_video(self):
        """Возвращаем ссылку на самое популярное видео из плейлиста"""
        id_video_maxlike = ""
        max_like = 0
        for video in self.video_response['items']:
            video_id = video["id"]
            like_count = int(video['statistics']['likeCount'])
            if like_count > max_like:
                id_video_maxlike = video_id
        return f"https://youtu.be/{id_video_maxlike}"
