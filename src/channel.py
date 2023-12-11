import json
import os

from googleapiclient.discovery import build
from icecream import ic

api_key: str = os.getenv('API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        # self.__api_key: str = os.getenv('API_KEY')
        # self.youtube = build('youtube', 'v3', developerKey=self.__api_key)
        self.__channel_id = channel_id
        self.channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        self.title = self.channel['items'][0]['snippet']['title']
        self.description = self.channel['items'][0]['snippet']['description']
        self.url = f'https://www.youtube.com/channel/{self.__channel_id}'
        self.subscriber_count = self.channel['items'][0]['statistics']['subscriberCount']
        self.video_count = self.channel['items'][0]['statistics']['videoCount']
        self.view_count = self.channel['items'][0]['statistics']['viewCount']

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        info_channel = youtube.channels().list(
            part='contentDetails,snippet,statistics',
            id='UC-OVMPlMA3-YCIeg4z5z23A'
        )
        result = info_channel.execute()
        ic(info_channel)
        ic(result)

    @classmethod
    def get_service(cls):
        """возвращает объект для работы с YouTube API"""
        cls.api_key = os.getenv('YT_API_KEY')
        return build('youtube', 'v3', developerKey=api_key)

    def to_json(self, date):
        channel_data = {"channel_id": self.__channel_id,
                        "title": self.title,
                        "description": self.description,
                        "url": self.url,
                        "subscriber_count": self.subscriber_count,
                        "video_count": self.video_count,
                        "view_count": self.view_count}
        with open(date, "w", encoding="utf-8") as file:
            json.dump(channel_data, file, indent=2, ensure_ascii=False)

    def __str__(self):
        """магический метод возвращает название и ссылку """
        return f'{self.title} ({self.url})'

    def __add__(self, other):
        """магический метод для операции сложения"""

        return int(self.subscriber_count) + int(other.subscriber_count)

    def __sub__(self, other):
        """магический метод для операции вычитания"""
        return int(self.subscriber_count) - int(other.subscriber_count)

    def __gt__(self, other):
        """магический метод для операции сравнения «больше»"""
        return self.subscriber_count > other.subscriber_count

    def __ge__(self, other):
        """магический метод для операции «больше или равно»"""
        return self.subscriber_count >= other.subscriber_count

    def __lt__(self, other):
        """магический метод для операции сравнения «меньше»"""
        return self.subscriber_count < other.subscriber_count

    def __le__(self, other):
        """магический метод для операции «меньше или равно»"""
        return self.subscriber_count <= other.subscriber_count

    def __eq__(self, other):
        """магический метод для операции «сравнение»"""
        return self.subscriber_count == other.subscriber_count


