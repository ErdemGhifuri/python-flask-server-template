from helper.request import ApiRequest

class WebScraping:
  async def scrape():
    response = await ApiRequest.get('https://api.bukalapak.com/couriers/categories?access_token=bWHCCJgfTrAr1QyOUYCLdfbuZ55W032LZ6yQh5Ij5Ty-MQ')
    return response['data']