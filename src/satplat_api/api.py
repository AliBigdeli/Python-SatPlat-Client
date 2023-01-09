import requests
from enum import Enum
import warnings

class Authentication:
    def is_authenticated(func):
        def wrapper(*args, **kwargs):
            response = func(*args, **kwargs)
            if response.status_code == 403:
                raise Exception("Authentication Failed")
            return response.json()
        return wrapper


class SatPlatAPI:
    api_base_url = "https://api.satplat.com/api/v1"
    has_authenticated = False

    class FileType(Enum):
        NDVI = "NDVI"
        NDRE = "NDRE"
        CHL = "CHL"
        LAI = "LAI"
        NDWI = "NDWI"

    def __init__(self, verify_ssl=True):
        self.client = requests.Session()
        if not verify_ssl:
            self.client.verify = verify_ssl
            warnings.filterwarnings(
                'ignore', message='Unverified HTTPS request')

    def set_access_token(self, access_token):
        self.access_token = access_token
        self.client.headers.update(
            {'Authorization': self.access_token})

    @Authentication.is_authenticated
    def get_farms_list(self):
        url = f"{self.api_base_url}/legal-customers/farms/"
        return self.client.get(url)

    @Authentication.is_authenticated
    def get_farm_detail(self, id):
        url = f"{self.api_base_url}/legal-customers/farms/{id}/"
        return self.client.get(url)

    @Authentication.is_authenticated
    def delete_farm(self, id):
        url = f"{self.api_base_url}/legal-customers/farms/{id}/"
        return self.client.delete(url)

    @Authentication.is_authenticated
    def add_farm(self, name, polygon):
        url = f"{self.api_base_url}/legal-customers/add-farm/"
        data = {
            "name": name,
            "polygon": polygon
        }
        return self.client.post(url, data=data)

    @Authentication.is_authenticated
    def process_farm(self, farm_id, start_date, end_date):
        url = f"{self.api_base_url}/legal-customers/process/"
        data = {
            "farm_id": farm_id,
            "start_date": start_date,
            "end_date": end_date,
        }
        return self.client.post(url, data=data)

    @Authentication.is_authenticated
    def get_farm_index(self, farm_id, filename, index):
        # 5
        url = f"{self.api_base_url}/legal-customers/index/{farm_id}/{filename}/{index}/"
        return self.client.get(url)

    @Authentication.is_authenticated
    def get_farm_index_image(self, farm_id, filename, index):
        # 6
        url = f"{self.api_base_url}/legal-customers/index-image/{farm_id}/{filename}/{index}/"
        return self.client.get(url)

    @Authentication.is_authenticated
    def get_farm_rgb_image(self, farm_id, filename):
        # 7
        url = f"{self.api_base_url}/legal-customers/rgb/{farm_id}/{filename}/"
        return self.client.get(url)

    @Authentication.is_authenticated
    def get_farm_time_series(self, farm_id, index, start_date, end_date):
        # 8
        url = f"{self.api_base_url}/legal-customers/time-series/{farm_id}/{index}/"
        params = {
            "start_date": start_date,
            "end_date": end_date

        }
        return self.client.get(url, params=params)



