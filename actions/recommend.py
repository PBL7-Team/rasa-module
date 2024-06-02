import requests
import re

import unicodedata

def convert_vietnamese_number_to_int(num_str):
    if num_str.isdigit():
        return int(num_str)
    
    num_str = unicodedata.normalize('NFD', num_str)
    num_str = ''.join([c for c in num_str if unicodedata.category(c) != 'Mn']).lower()

    vietnamese_numbers = {
        "mot": 1, "nhat": 1, "hai": 2, "ba": 3, "bon": 4, "nam": 5,
        "sau": 6, "bay": 7, "tam": 8, "chin": 9, "muoi": 10,
        "muoi mot": 11, "muoi hai": 12, "muoi ba": 13, "muoi bon": 14, "muoi lam": 15,
        "muoi sau": 16, "muoi bay": 17, "muoi tam": 18, "muoi chin": 19, "hai muoi": 20
    }

    return vietnamese_numbers.get(num_str, None)


def recommend_place(message,num):
    url = "http://flask-app.southeastasia.cloudapp.azure.com:8080/recommend"
    
    params = {'message': message}
    headers = {'API-Key': 'PBL_7_Traveling'}
    
    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        recommendations = data.get('message', [])
        if recommendations:
            if num:
                num = convert_vietnamese_number_to_int(num)
                if num:
                    return "\n".join(recommendations[:num])
                else:
                    return "Không thể chuyển đổi số"
            else:
                return "\n".join(recommendations)
        else:
            return "Không tìm thấy địa điểm phù hợp"
    else:
        print(f"Failed to get recommendations: {response.status_code}")
    
    # if isinstance(num, str):
    #     num = convert_vietnamese_number_to_int(num)
    
print(recommend_place('Hãy giới thiệu cho tôi địa điểm ăn chơi về đêm ở Đà Nẵng','5'))

    