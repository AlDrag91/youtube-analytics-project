import os
from googleapiclient.discovery import build
from icecream import ic

api_key: str = os.getenv('API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)
ic(youtube)


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        info_channel = youtube.channels().list(
            part='contentDetails,snippet,statistics',
            id='UC-OVMPlMA3-YCIeg4z5z23A'
        )
        result = info_channel.execute()
        ic(info_channel)
        ic(result)
        # print(result)
