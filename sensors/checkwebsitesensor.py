import eventlet
import requests

from st2reactor.sensor.base import Sensor


class CheckWebsiteSensor(Sensor):
    def __init__(self, sensor_service, config):
        super(CheckWebsiteSensor, self).__init__(sensor_service=sensor_service, config=config)
        self._logger = self.sensor_service.get_logger(name=self.__class__.__name__)
        self._stop = False
        self._webiste_url = None 
        self._trigger_name = 'websitedown'
        self._trigger_pack = 'checksite'
        self._trigger_ref = '.'.join([self._trigger_pack, self._trigger_name])

    def setup(self):
        self._website_url = self._config['url']

    def run(self):
        while not self._stop:
            self._logger.debug('[checkwebsite sensor] Checking Website status... ')
            # sending get request and saving the response as response object 
            try:
                r = requests.get(url = self._website_url)
                data = r.json()
                # extracting data in json format
            except requests.exceptions.RequestException as e:
                payload = {'website': self._webiste_url}
                self._logger.info(f'Website {self._webiste_url} is down: Action triggered to start service')
                self.sensor_service.dispatch(trigger='checkwebsite.websitedown', payload=payload)
            else:
                self._logger.info(data['status'])
                payload = {'website': self._webiste_url}
                if data['status'] != 'OK':
                    self._logger.info("Webiste "+self._webiste_url+" is down: Action triggered to start service")
                    self.sensor_service.dispatch(trigger='checkwebsite.websitedown', payload=payload)
            eventlet.sleep(5)

    def cleanup(self):
        self._stop = True

    # Methods required for programmable sensors.
    def add_trigger(self, trigger):
        pass

    def update_trigger(self, trigger):
        pass

    def remove_trigger(self, trigger):
        pass