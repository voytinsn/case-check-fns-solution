import json
from typing import Dict
from fns_api_client import FnsApiClient
import os
from dotenv import load_dotenv
from entities.negative_info import NegativeInfo
from models.clients_model import ClientsModel
from models.negative_info_model import NegativeInfoModel

load_dotenv()


def main():
    prepare_tables()
    # api_key = os.getenv("API_KEY")
    # base_url = os.getenv("API_URL")
    # api_client = FnsApiClient(base_url, api_key)

    # data: Dict = api_client.check(req=1027739471517)
    # negative_dict = data["items"][0]["ЮЛ"]["Негатив"]
    # negative_obj = NegativeInfo(**negative_dict)

    # return negative_obj
    return


    
def prepare_tables():
    """
    Подготовка таблиц в базе данных.
    """
    db_host = os.getenv("DB_HOST")
    db_port = int(os.getenv("DB_PORT"))
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_name = os.getenv("DB_NAME")

    negative_info_model = NegativeInfoModel(db_host, db_port, db_user, db_password, db_name)
    negative_info_model.create_table()

    clients_model = ClientsModel(db_host, db_port, db_user, db_password, db_name)
    clients_model.prepare_table()

if __name__ == "__main__":
    main()
