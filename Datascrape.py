import requests
# lira id: TRY
# CAD
# url = requests.get(f"https://free.currconv.com/api/v7/currencies?apiKey=1dcbd2d6cb964b6e7d5c")
#https://free.currconv.com/api/v7/convert?q=USD_CAD&compact=ultra&apiKey=1dcbd2d6cb964b6e7d5c

def get_value(curr1: str, curr2: str) -> float:
    user_input = curr1
    converted = curr2
    if user_input != "" and converted != "":
        if user_input != "Select" and converted != "Select":
            url = requests.get(f'https://free.currconv.com/api/v7/convert?q={user_input}_{converted}&compact=ultra&apiKey=1dcbd2d6cb964b6e7d5c')
            return url.json()[f"{user_input}_{converted}"]
    return 1


