import configuration
import requests
import data

def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)

response = get_docs()

def get_logs():
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH)

response2 = get_logs()

def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

response3 = get_users_table()

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                        json=body,
                        headers=data.headers)

response4 = post_new_user(data.user_body)

def post_products_kits(products_ids):
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
                         json=products_ids,
                         headers=data.headers)

response5 = post_products_kits(data.product_ids)


print("-------------------")
print(response.status_code)
print(response.headers)
print("-------------------")
print(response2.status_code)
print(response2.headers)
print("-------------------")
print(response3.status_code)
print(response3.headers)
print("-------------------")
print(response4.status_code)
print(response4.json())
print("-------------------")
print(response5.status_code)
print(response5.json())
print("-------------------")