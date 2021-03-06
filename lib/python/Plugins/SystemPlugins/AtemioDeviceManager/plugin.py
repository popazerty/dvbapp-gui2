# for localized messages
from . import _

from HddSetup import HddSetup
from HddMount import HddFastRemove
from Plugins.Plugin import PluginDescriptor

def deviceManagerSetup(menuid, **kwargs):
	session.open(HddSetup)

def deviceManagerFastRemove(session, **kwargs):
	session.open(HddFastRemove)


def Plugins(**kwargs):
	return [PluginDescriptor(name = _("Atemio Device Manager"), description = _("Format/Partition your Devices and manage Mountpoints"), where = PluginDescriptor.WHERE_EXTENSIONSMENU, fnc = deviceManagerSetup),
			PluginDescriptor(name = _("Atemio Device Manager - Fast Mounted Remove"), description = _("Quick and safe remove for your mounted devices "), where = PluginDescriptor.WHERE_EXTENSIONSMENU, fnc = deviceManagerFastRemove)]

