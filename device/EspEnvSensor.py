import sqlite3

from core.device.model.Device import Device
from core.device.model.DeviceException import RequiresWIFISettings
from core.device.model.DeviceType import DeviceType
from core.dialog.model.DialogSession import DialogSession


class EspEnvSensor(DeviceType):
	ESPTYPE = 'envSensor'


	def __init__(self, data: sqlite3.Row):
		super().__init__(data, devSettings=self.DEV_SETTINGS, locSettings=self.LOC_SETTINGS, heartbeatRate=600)


	def discover(self, device: Device, replyOnSiteId: str = '', session: DialogSession = None) -> bool:
		if not self.ConfigManager.getAliceConfigByName('ssid'):
			raise RequiresWIFISettings()

		return self.parentSkillInstance.startTasmotaFlashingProcess(device, replyOnSiteId, session)


	def getDeviceIcon(self, device: Device) -> str:
		if not device.uid:
			return 'EspEnvSensor.png'
		if not device.connected:
			return 'temp_offline.png'
		# TODO check temperatur
		return 'temp_OK.png'