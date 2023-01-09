<div align="center">

<a href="https://satplat.com/" target="_blank"> <img src="https://user-images.githubusercontent.com/29748439/211309040-f338a8c8-2617-455d-bcae-0727eceb622a.png" width=300 /> </a>

</div>

<h1 align="center">Python SatPlat Api Client</h1>
<h3 align="center">a simple module to integrate with SatPlat satellite image api service</h3>

# Overview
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [References](#references)
- [Swagger](#swagger)

# Installation
This module is a pip package to let you integrate with satplat api service provider. in order to use this module you have to install it by pip command or through setup.

```bash
pip install satplat_api
```
Import package into your project by:

```bash
from satplat_api.api import SatPlatAPI
```
in order to use the module please consider looking at examples and documentations.

# Usage
In order to integrate with this service provider you need to first have an account and token. so first of all create an account with the url provided below:
<https://dashboard.satplat.com/#/login>


For easy implementations i have provided two simple examples, one for creating authenticating and getting access key and one for simple example to get current data from a location

```python
# importing satplat module
from satplat_api.api import SatPlatAPI

# creating an instance client
client = SatPlatAPI()

# setting up access token
client.set_access_token(access_token="<YOUR_TOKEN>")

```

now that you have access token with unlimited time access then there is no need for authenticating, you can just set the access_token and proceed with other requests.


```python
#importing satplat module
from satplat_api.api import SatPlatAPI

# creating an instance client
client = SatPlatAPI()

# setting the access token for headers in client object
client.set_access_token(access_token="<YOUR_TOKEN>")

# to get farms list 
pprint(client.get_farms_list())

```

# References

- <a href="./docs/satplat-api-document.pdf">document</a>


# Swagger
i even did create a custom swagger for testing purposes

<div align="center">
<img src="https://user-images.githubusercontent.com/29748439/211308445-95044159-842d-4e13-ba1d-a345e84785da.png"/>
</div>
