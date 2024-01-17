import random

from . import config

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from llpy import *


def automessage():
    for player in mc.getOnlinePlayers():
        player.sendText(random.choice(config.messages), config.type_message)

setInterval(automessage, config.time_delay * 1000)