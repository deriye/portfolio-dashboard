import requests

assets = { }

while True:

    option = input('Add List Delete Quit')

    if option == 'Add':
        asset = input('enter yoyr stock: ')
        year = input('year')
        month = input('month')
        date = input('date')
        added_asset = f'https://api.polygon.io/v1/open-close/{asset}/{year}-{month}-{date}?adjusted=true&apiKey=wEH_XaiJhHkSCCXkvU3P7XmY3yhe7igY'
        today = f'https://api.polygon.io/v1/open-close/{asset}/2021-07-02?adjusted=true&apiKey=wEH_XaiJhHkSCCXkvU3P7XmY3yhe7igY'
        data_bought = requests.get(added_asset).json()
        data_today = requests.get(today).json()
        data_bought_close = data_bought['close']
        data_today_close = data_today['close']


        procent_return = (data_today_close-data_bought_close)/data_bought_close*100
        assets[asset] = [data_today_close, procent_return]
        print(assets)
    elif option == 'List':
        print(assets)
    elif option == 'Delete':
        delete = input('What do you want to delete?: ')
        assets.pop(delete)
    elif option == 'Quit':
        break
    else:
        print('Please try again...')







