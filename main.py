import requests
from bs4 import BeautifulSoup

def main():
    url = "https://www.wildberries.ru/catalog"
    response = requests.get(url)
    print(response.status_code)
    # print(response.text)

    soup = BeautifulSoup(response.text, "html.parser")
    spoon = soup.find_all("a", class_='product-card_link j-card-link j-open-full-product-card')
    print(spoon)

   # soup = BeautifulSoup(response.text, "html.parser")
   # part = soup.find("div", class_="text-container")
    # with open("page.txt", "a", encoding="UTF-8") as file:
    #     file.write(part.text)
     #    file.write("".join([i.text for i in spoon]))

if __name__ == '__main__':
    main()
