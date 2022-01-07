import requests

def get_info():
    response = requests.get(url='https://yobit.net/api/3/info')


    with open('info.txt', 'w') as file:
        file.write(response.text)

    return response.text


def get_ticker(coin1='btc', coin2='usd'):
    #response = requests.get(url='https://yobit.net/api/3/ticker/eth_btc-eth_btccc?ignore_invalid=1')
    response = requests.get(url=f'https://yobit.net/api/3/ticker/{coin1}_{coin2}?ignore_invalid=1')

    with open('ticker.txt', 'w') as file:
        file.write(response.text)

    return response.text


def get_depth(coin1='btc', coin2='usd', limit=150):
    response = requests.get(url=f'https://yobit.net/api/3/depth/{coin1}_{coin2}?limit={limit}&ignore_invalid=1')

    with open('depth.txt', 'w') as file:
        file.write(response.text)

    bids = response.json()[]



    return response.text


def main():
    # print(get_info())
    # print(get_ticker())
    # print(get_ticker(coin1='eth'))
    print(get_depth(coin1='eth'))




if __name__ == '__main__':
    main()