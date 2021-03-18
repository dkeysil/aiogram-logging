# aiogram-logger
---
### Simplifies sending logs from your bots to DB.
![example](https://i.imgur.com/gFfQDmD.png)
---
## Quick start with InfluxDB + Grafana
Install package from pip
```
pip install aiogram_logging
```

Prepare InlfuxDB and Grafana with this [repo](https://github.com/DKeysil/influxdb-grafana-docker-compose).

Import and create instances
```python
from aiogram_logging import Logger, InfluxSender

sender = InfluxSender(host='localhost',
                      db='db-name',
                      username='db-user',
                      password='db-password')
logger = Logger(sender)
```

Create StatMiddleware to logging every incoming message
```python
class StatMiddleware(BaseMiddleware):

    def __init__(self):
        super(StatMiddleware, self).__init__()

    async def on_process_message(self, message: types.Message, data: dict):
        await logger.write_logs(self._manager.bot.id, message, parse_text=True)


dp.middleware.setup(StatMiddleware())
```

Create dashboard by yourself or import from `grafana-dashboard.json`

Yeah, you can connect several bots for one InfluxDB
## TODO:
1. Explain how to manage logs from several bots in Grafana
2. Parse more different data