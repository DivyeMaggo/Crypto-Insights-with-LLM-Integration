from dotenv import load_dotenv
import google.generativeai as genai
import json
import os
import http.client
import plotext as plt
from datetime import datetime

conn = http.client.HTTPSConnection("api.coincap.io")
payload = ''
headers = {}

def one_year_trend(user_input):
    final_request = "/v2/assets/"+user_input+"/history?interval=d1"
    conn.request("GET", final_request, payload, headers)
    res = conn.getresponse()
    data = res.read()
    trend_data = (json.loads(data.decode("utf-8"))['data'])
    #print(trend_data)
    usdPrice = []
    dates=[]
    for i in trend_data:
        usdPrice.append(i['priceUsd'])
        dates.append(i['date'])
    usdPrice = list(map(float, usdPrice))
    print('Minimum price has been : ',min(usdPrice),' USD')
    print('Maximum price has been : ',max(usdPrice),' USD')
    #print('type of date: ',dates)
    #print('type of price: ',usdPrice)
    dates = [datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%fZ').timestamp() for date in dates]
    plt.plot_size(60, 20)
    plt.plot(dates, usdPrice)
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.title(f"{user_input} Stock Prices Over Time")
    plt.show()


    


def summarize(crypto_data):
    print('\n')
    print('*********Summarizing********')
    load_dotenv()
    #using GEMINI to summarise the data
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content('Explain each keyword '+crypto_data+ 'Please respond in bullet points (individual sentences) but without using any bold formatting, asterisks, or special characters. In the end talk a little about the specific crypto currency.')
    print(response.text)
    print('*********End********')


def user_selected_crypto(user_input):
    final_request = "/v2/assets/"+user_input
    #print(final_request)
    conn.request("GET", final_request, payload, headers)
    res = conn.getresponse()
    data = res.read()
    crypto_data = (json.loads(data.decode("utf-8"))['data'])
    print(crypto_data)
    user_summary = input(' \n Do you want me to summarize this data for you? \n 1. Yes \n 2. No \n').lower()

    if(user_summary == '1' or user_summary == 'yes' or user_summary == 'Yes'):
        summarize(data.decode("utf-8"))
    else:
        print('All right, no summary!! \n')
    
    trend = input('Do you want to see the trend in crypto price in last one year? \n 1.Yes \n 2.No  \n').lower()
    if(trend == '1' or trend == 'yes' or trend == 'Yes'):
        one_year_trend(user_input)
    else:
        print('Okay, no trend!')



def top_10_crypto():
    conn.request("GET", "/v2/assets/", payload, headers)
    res = conn.getresponse()
    data = res.read()
    json_data = json.loads(data.decode('utf-8'))
    json_data = json_data['data']
    count = 0
    crypto_names =[]

    for i in json_data:
        if(count < 10):
            crypto_names.append(i['id'])
            print(f"{count+1}. {i['id']} \n")
        else:
            break
        count+=1
    return crypto_names