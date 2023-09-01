from extras.plugins import PluginConfig

class NetboxTimetableConfig(PluginConfig):
    name = 'netbox_timetable'
    verbose_name = 'Netbox Timetable'
    description = 'Netbox Timetable management'
    version = '0.1'
    base_url = 'netbox-timetable'

config = NetboxTimetableConfig

import logging

logger = logging.getLogger("netbox.plugins.netbox_timetable")