from __future__ import print_function
import logging

from icinga2api.base import Base
from icinga2api.exceptions import Icinga2ApiException

LOG = logging.getLogger(__name__)

class Config(Base):
    '''
    Icinga 2 API config class
    '''

    base_url_path = 'v1/config'

    def create_package(self, package_name):
        url = '{}/{}/{}'.format(self.base_url_path, 'packages', package_name)
        return self._request('POST', url)

    def upload_package(self, package_name, files):
        url = '{}/{}/{}'.format(self.base_url_path, 'stages', package_name)
        payload = {
            "files": files,
        }

        return self._request('POST', url, payload)

    def list_packages(self):
        url = '{}/{}'.format(self.base_url_path, 'packages')
        return self._request('GET', url)
    
    def get_package_error(self, package_name, stage):
        url = '{}/{}/{}/{}/{}'.format(self.base_url_path, 'stages/files', package_name, stage, 'startup.log')
        return self._request('GET', url)

    def remove_stage(self, package_name, stage):
        url = '{}/{}/{}/{}'.format(self.base_url_path, 'stages', package_name, stage)
        return self._request('DELETE',url, {})