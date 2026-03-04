def poweroff() -> dict:
    """ Формируем задачу выключения устройства """
    return {
        "queue": True,
        "command": "poweroff",
        "source": "voice_command"  # откуда пришла команда
    }


def reboot() -> dict:
    """ Формируем задачу перезагрузки устройства """
    return {
        "queue": True,
        "command": "reboot",
        "source": "voice_command"
    }


def set_volume(volume: int) -> dict:
    """ Формируем задачу по уровню громкости """
    return {
        "queue": True,
        "command": "set_volume",
        "volume": volume,
        "source": "voice_command"
    }


def get_data() -> dict:
    """ Получение текущей даты и времени через инет """
    import requests
    from datetime import datetime
    dt = ""

    try:
        data = requests.get('http://worldtimeapi.org/api/timezone/Europe/Moscow', timeout=3).json()
        dt = datetime.fromisoformat(data['datetime'])
    except:
        # Если нет интернета, возвращаем локальное время
        dt = datetime.now()
    
    dt = f"{dt:%Y-%m-%d %H:%M:%S %A}"
    return {
        "queue": False, # Без очереди, уже готов результат
        "name": "get_data",
        "value": dt,
        "source": "voice_command"
    }






FUNCTIONS = {

    "get_data": {
        "description": "Вызывай эту функцию если пользователь спрашивает котрый час, день недели, год, месяц.",
        "function": get_data,
        "schema": {
            "type": "object",
            "properties": {
            },
            "required": []
        }
    },

    "reboot": {
        "description": "Вызывай эту функцию если пользователь просит перезагрузить устройство",
        "function": reboot,
        "schema": {
            "type": "object",
            "properties": {
            },
            "required": []
        }
    },
    "poweroff": {
        "description": "Вызывай эту функцию если пользователь просит выключить устройство",
        "function": poweroff,
        "schema": {
            "type": "object",
            "properties": {
            },
            "required": []
        }
    },
    "set_volume": {
        "description": "ВСЕГДА вызывай эту функцию когда пользователь просит изменить громкость устройства от 0 до 100% в целых числах. \
                        Если пользователь просит установить громкость 0, постарайся отговорить, ведь вы не будете слышать друг-друга.",
        "function": set_volume,
        "schema": {
            "type": "object",
            "properties": {
                "volume": {
                    "type": "integer",
                    "description": "Уровень громкости от 0 до 100%"
                }
            },
            "required": ["volume"]
        }
    }

}

