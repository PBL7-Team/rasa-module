import requests
import re
from bs4 import BeautifulSoup

def fetch_wikipedia_content(search_term):
    url = f"https://vi.wikipedia.org/w/index.php?search={search_term}&ns0=1"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        for vcard in soup.find_all(class_="vcard"):
            vcard.decompose()
        content_div = soup.find('div', id='mw-content-text')
        if content_div:
            all_text = content_div.get_text(separator=' ')
            all_text_with_spaces = ' '.join(all_text.split())
            return all_text_with_spaces
        else:
            return "Không tìm thấy nội dung trong div với id = mw-content-text."
    else:
        return f"Lỗi khi gửi yêu cầu: {response.status_code}"

def cut_content_before_edit_source(content):
    edit_source_index = content.find("[ sửa | sửa mã nguồn ]")
    if edit_source_index == -1:
        return content
    cut_content = content[:content.rfind(".", 0, edit_source_index) + 1]
    return cut_content

def clean_text(text):
    cleaned_text = re.sub(r'([a-zA-ZÀ-ỹ])([!-/:-@\[-`{-~])', r'\1 \2', text)
    cleaned_text = re.sub(r'\[\d+\]', '', cleaned_text)
    return cleaned_text

def fix_punctuation(text):
    text = re.sub(r'\s+([.,;!?])', r'\1', text)
    return text

def search_wikipedia(search_term):
    content = fetch_wikipedia_content(search_term)
    cut_content = cut_content_before_edit_source(content)
    cleaned_content = clean_text(cut_content)
    cleaned_content = fix_punctuation(cleaned_content)
    return cleaned_content

# def search_wikipedia(search_term):
#     url = "http://flask-app.southeastasia.cloudapp.azure.com:8080/search"
    
#     params = {'query': search_term}
#     headers = {'API-Key': 'PBL_7_Traveling'}
    
#     response = requests.get(url, params=params, headers=headers)

#     if response.status_code == 200:
#         data = response.json()
#         print(data)
#     else:
#         print(f"Failed to get recommendations: {response.status_code}")
