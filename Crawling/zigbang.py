import requests
import pprint
import geohash2

keyword = "대치동"
url = "https://apis.zigbang.com/search?q={}".format(keyword)

req = requests.get(url)

# 실제 api 주소에서 json 형태로 리턴
_json = req.json()


if _json.get("code") == "200":
    data = _json.get("items")[0]
    _description = data.get("description")
    _id = data.get("id")
    _lat = data.get("lat")
    _lng = data.get("lng")
    _zoom = data.get("zoom")

    geohash = geohash2.encode(_lat, _lng, precision=5)

    url = "https://apis.zigbang.com/v2/items?deposit_gteq=0&domain=zigbang&geohash={}&rent_gteq=0&sales_type_in=전세%7C월세&service_type_eq=원룸".format(
        geohash)

    _req_items = requests.get(url).json()

    _items = _req_items.get("items")

    item_ids = []
    for item in _items:
        item_ids.append(item.get("item_id"))

    items = {"item_ids": item_ids[:100]}

    _results = requests.post(
        'https://apis.zigbang.com/v2/items/list', data=items).json()

    datas = _results.get("items")

    for d in datas:
        _address = "{} {}".format(d.get("address1"), d.get("address"))
        if d.get("address3") is not None:
            _address += " {}".format(d.get("address3"))

        building_floor = d.get("building_floor")
        floor = d.get("floor")
        thumbnail = d.get("images_thumbnail")
        item_id = d.get("item_id")
        reg_date = d.get("reg_date")
        sales_type = d.get("sales_type")
        service_type = d.get("service_type")
        size_m2 = d.get("size_m2")
        title = d.get("title")
        deposit = d.get("deposit")
        rent = d.get("rent")

        # pprint.pprint(d)
        print("*" * 100)
        print("{} [{}]".format(title, item_id))
        print("보증금/월세: {}/{}".format(deposit, rent))
        print("건물층/매물층: {}/{}".format(building_floor, floor))
        print("등록일자: {}".format(reg_date))
        print("서비스형태/매물형태: {}/{}".format(service_type, sales_type))
        print("사이즈: {}".format(size_m2))
