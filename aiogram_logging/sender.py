from aioinflux import InfluxDBClient, InfluxDBWriteError
import logging


class Sender:
    """
    Interface for sender class
    """
    def __init__(self) -> None:
        pass

    async def write_message(self, data: dict) -> None:
        """
        Upload message to db

        Args:
            data (dict): data from logger class
        """
        pass


class InfluxSender(Sender):
    def __init__(self,
                 host: str,
                 db: str,
                 username: str,
                 password: str) -> None:
        self.host = host
        self.db = db
        self.username = username
        self.password = password
        self.client = InfluxDBClient(host=host,
                                     db=db,
                                     username=username,
                                     password=password,
                                     mode='blocking')

        try:
            self.client.ping()
        except InfluxDBWriteError as ex:
            logging.error(f'InfluxDB init error: {str(ex)}')
        else:
            self.client.mode = 'async'

    def parse_data(self, data: dict) -> dict:
        _data = {
            'measurement': 'bot',
            'time': data.get('datetime'),
            'fields': {
                "event": 1
            },
            'tags': {
                'user': str(data.get('user_id')),
                'bot_id': str(data.get('bot_id'))
            }
        }

        if data.get('is_command'):
            _data['tags'].update({
                'command': data.get('text')
            })
        if data.get('text'):
            _data['fields'].update({
                'text': data.get('text')
            })
        return _data

    async def write_message(self, data) -> None:
        data = self.parse_data(data)

        async with InfluxDBClient(host=self.host,
                                  db=self.db,
                                  username=self.username,
                                  password=self.password) as client:

            response = await client.write(data)
            logging.debug(f'write status={response}\n'
                          f'data={data}')
