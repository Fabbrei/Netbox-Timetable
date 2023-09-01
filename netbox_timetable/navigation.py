from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices


certificate_buttons = [
    PluginMenuButton(
        link='plugins:netbox_timetable:certificate_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]


menu_items = (
    PluginMenuItem(
        link='plugins:netbox_timetable:certificate_list',
        link_text='Certificati',
        buttons=certificate_buttons
    ),
)