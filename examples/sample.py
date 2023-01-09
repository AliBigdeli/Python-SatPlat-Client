from satplat_api.api import SatPlatAPI
from pprint import pprint
import os


client = SatPlatAPI()
client.set_access_token(
    access_token=os.environ['ACCESS_TOKEN'])
# pprint(client.get_farms_list())
farm = client.get_farm_detail("ff83c4d2-6ecb-4f6f-8862-e414244658d1")
process = client.process_farm(
    farm["id"],
    "2023-01-01",
    "2023-01-30"
)
print(process)
# 5
pprint(client.get_farm_index(
    farm["id"],
    process[-1]["file_name"],
    client.FileType.NDVI.value
))
# 6
pprint(client.get_farm_index_image(
    farm["id"],
    process[-1]["file_name"],
    client.FileType.NDVI.value
))
# 7
pprint(client.get_farm_rgb_image(
    farm["id"],
    process[0]["file_name"]
))
# 8
pprint(client.get_farm_time_series(
    farm["id"],
    client.FileType.NDVI.value,
    start_date="2022-11-01",
    end_date="2022-12-01"
))
