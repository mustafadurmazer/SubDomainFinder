import requests

target_input = "google.com/"


with open("subdomainlist.txt.txt","r") as subdomainlist:
    for word in subdomainlist:
        word = word.strip()
        #strip fonksiyonu ile istenilen metindeki boşluklar virgüller noktalar veya istenmeyen harfler temizlenebilir.
        url = "https://" + word + "." + target_input
        try:
            response = requests.get(url)
        except requests.exceptions.ConnectionError:
            print("Not Found Sundomain:",{url})
