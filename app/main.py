import datetime


def outdated_products(products: list):
    return [product["name"] for product in products
            if product["expiration_date"] < datetime.date.today()]  #
