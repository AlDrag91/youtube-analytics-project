import os

from googleapiclient.discovery import build
from icecream import ic


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.__api_key: str = os.getenv('API_KEY')
        self.youtube = build('youtube', 'v3', developerKey=self.__api_key)

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        info_channel = self.youtube.channels().list(
            part='contentDetails,snippet,statistics',
            id='UC-OVMPlMA3-YCIeg4z5z23A'
        )
        result = info_channel.execute()
        ic(info_channel)
        ic(result)
