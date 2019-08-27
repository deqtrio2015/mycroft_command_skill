from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG
import json
import re
import os

class SpokenCMDSkill(MycroftSkill):

    def __init__(self):

        super(SpokenCMDSkill, self).__init__(name="SpokenCMDSkill")

    @intent_handler(IntentBuilder("").require("SpokenCommandKeyword"))
    def handle_spoken_cmd(self, message):

        cmd = message.data["SpokenCommandKeyword"]

        if message.data["SpokenCommandKeyword"] == "sit":
            self.speak_dialog("o.k.i'll.sit.down")
        elif message.data["SpokenCommandKeyword"] == "jump":
            self.speak_dialog("eh")
        else:
            self.speak_dialog("Sorry.I.dont.know.that.skill.yet")


def create_skill():
    return SpokenCMDSkill()
