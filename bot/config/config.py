OWNER_ID = 278821688894947328
PRIVATE_DEV_GUILD_ID = 835725357423919104
WARNET_GUILD_ID = 761644411486339073

ADMINISTRATOR_ROLE_ID = {
    'admin': '761650159833841674',
    'mod': '761662280541798421'
}

ACHIEVEMENT_RANK_ROLE_ID = (
    00000,  # placeholder
    11111,  # placeholder
    22222,  # placeholder
    33333,  # placeholder
    44444,  # placeholder
)

DEFAULT = {
    'guild_id': '761644411486339073',
    'prefix': 'war!',
}

class TCGConfig:
    TCG_TITLE_ROLE_ID = (
        # 1043864006370267146,  # test role
        # 1044980740238098452,  # test role
        # 1052443871117848637,  # test role
        # 1052443930152681473,  # test role
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
