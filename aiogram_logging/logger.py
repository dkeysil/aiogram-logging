from aiogram import types
from datetime import datetime


class Logger:
    """
    Class parses data from telegram bot
    then send it to storage
    """
    def __init__(self, sender_class=None) -> None:
        self.sender_class = sender_class

    def parse_data(self,  bot_id: int,
                   message: types.Message,
                   parse_text) -> dict:
        data = {
            'is_command': message.is_command(),
            'bot_id': bot_id,
            'datetime': datetime.utcnow(),
            'message_type': 'command' if message.is_command() else 'text',
            'user_id': message.from_user.id
        }

        if message.content_type == types.ContentType.TEXT:
            data.update({
                'text': message.text
                if message.is_command() or parse_text
                else None
            })
        elif message.content_type == types.ContentType.PHOTO and parse_text:
            data.update({
                'text': message.caption
                if message.caption
                else None
            })

        return data

    async def write_logs(self, bot_id: int,
                         message: types.Message,
                         parse_text=False) -> None:
        """
        Pass data to sender class

        Args:
            bot_id (int): bot id (self._manager.bot.id)
            message (types.Message):
            parse_text (bool, optional): pass text to db. Defaults to False.
        """
        data = self.parse_data(bot_id, message, parse_text)
        await self.sender_class.write_message(data)
