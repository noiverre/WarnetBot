import os
from dotenv import load_dotenv

load_dotenv()

BOT_DEBUG = os.getenv("BOT_DEBUG")

BOT_TOKEN = os.getenv("BOT_TOKEN")
DEV_BOT_TOKEN = os.getenv("DEV_BOT_TOKEN")

GUILD_ID = int(os.getenv("GUILD_ID"))
DEV_GUILD_ID = int(os.getenv("GUILD_ID"))

LOCAL_DB_HOST = os.getenv("LOCAL_DB_HOST")
LOCAL_DB_NAME = os.getenv("LOCAL_DB_NAME")
LOCAL_DB_USERNAME = os.getenv("LOCAL_DB_USERNAME")
LOCAL_DB_PASSWORD = os.getenv("LOCAL_DB_PASSWORD")
LOCAL_DB_PORT = int(os.getenv("LOCAL_DB_PORT"))

HOSTED_DB_HOST = os.getenv("HOSTED_DB_HOST")
HOSTED_DB_NAME = os.getenv("HOSTED_DB_NAME")
HOSTED_DB_USERNAME = os.getenv("HOSTED_DB_USERNAME")
HOSTED_DB_PASSWORD = os.getenv("HOSTED_DB_PASSWORD")
HOSTED_DB_PORT = int(os.getenv("HOSTED_DB_PORT"))

# These are administrator role on Warnet guild
ADMINISTRATOR_ROLE_ID = {
    'admin': '761650159833841674',
    'mod': '761662280541798421'
}
STAFF_ROLE_ID = 951170972671701063

DEFAULT = {
    'guild_id': GUILD_ID,
    'prefix': ['war!', 'War!', 'WAR!'],
}


class TCGConfig:
    TCG_TITLE_ROLE_ID = (
        1051867676202512415,  # Novice Duelist
        1051865453208801361,  # Expert Duelist
        1051865448980942948,  # Master Duelist
        1051865444073611365,  # Immortal Duelist
    )
    TCG_EVENT_STAFF_ROLE_ID = 977488765234855986
    TCG_MATCH_REPORT_CHANNEL_ID = 1053525411725836428
    TCG_MATCH_LOG_CHANNEL_ID = 1053525862982631516
    TCG_TITLE_EMOJI = {
        TCG_TITLE_ROLE_ID[0]: '<:NoviceDuelist:1052440393461022760>',
        TCG_TITLE_ROLE_ID[1]: '<:ExpertDuelist:1052440396489314304>',
        TCG_TITLE_ROLE_ID[2]: '<:MasterDuelist:1052440400822018078>',
        TCG_TITLE_ROLE_ID[3]: '<:ImmortalDuelist:1052440404135518228>'
    }
