import requests
from requests import Response
from pydantic import BaseModel, Field, root_validator


class Info(BaseModel):
    sna: str
    sarea: str
    mday: str
    ar: str
    act: bool
    updateTime: str
    total: int
    rent_bikes: int = Field(alias="available_rent_bikes")
    lat: float = Field(alias="latitude")
    lng: float = Field(alias="longitude")
    return_bikes: int = Field(alias="available_return_bikes")

    @root_validator(pre=True)
    def convert_act_to_str(cls, values):
        values['act'] = "營業中" if values['act'] else "維護中"
        return values

    @root_validator(pre=True)
    def clean_sna(cls, values):
        values['sna'] = values['sna'].split("_")[-1]
        return values


def __download_json():
    url = "https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json"

    try:
        res: Response = requests.get(url)
        res.raise_for_status()  # 確保請求成功
    except requests.exceptions.RequestException as e:
        raise Exception(f"連線失敗: {e}")
    else:
        all_data: list[dict] = res.json()
        return all_data


def load_data() -> list[Info]:
    try:
        all_data: list[dict] = __download_json()
    except Exception as error:
        print(error)
        return [] 

    try:
        youbike_data = [Info(**item) for item in all_data]
    except Exception as e:
        print(f"資料格式錯誤: {e}")
        return []

    return youbike_data
