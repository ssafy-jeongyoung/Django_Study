from django.shortcuts import render
from io import BytesIO
import matplotlib.pyplot as plt
import base64
import pandas as pd

# Create your views here.
csv_path = 'weathers/data/austin_weather.csv'

def problem1(request):
    data_frame = pd.read_csv(csv_path)
    context = {
        'data_frame' : data_frame
    }
    return render(request, 'weathers/problem1.html', context)

def problem2(request):
    df = pd.read_csv(csv_path)

    df['Date'] = pd.to_datetime(df['Date'])
    # df['Month'] = df['Date'].dt.strftime('%Y-%m')

    # 다른 view 함수에서 plt를 이미 그린 상태에서
    # 다시 그리는 경우를 대비하여, 초기화를 진행
    plt.clf()
    plt.figure(figsize=(10, 6))
    plt.plot(df['Date'], df['TempHighF'])
    plt.plot(df['Date'], df['TempAvgF'])
    plt.plot(df['Date'], df['TempLowF'])
    plt.title('Temperature Variation')
    plt.xlabel('Date')
    plt.ylabel('Temperature(Fahrenheit)')
    plt.legend(('High Temperature', 'Average Temperature', 'Low Temperature'))
    # 비어있는 버퍼 생성
    buffer = BytesIO()

    # 버퍼에 그래프 저장
    plt.savefig(buffer, format='png')

    # 버퍼의 내용을 base64로 인코딩,                   //  사용할 수 있도록 디코딩
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace("\n", '')

    # 버퍼를 닫아줌
    buffer.close()

    # 이미지를 웹페이지에 표시하기 위해 URI 형식(주소 형식)으로 만들어진 문자열 생성
    context = {
        # chart_img : 저장된 이미지의 경로
        'chart_img' : f'data:image/png;base64,{image_base64}',
    }
    return render(request, 'weathers/problem2.html', context)

def problem3(request):
    df = pd.read_csv(csv_path)

    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.strftime('%Y-%m')
    temp_high = df.groupby('Month').mean('TempHighF')
    # temp_avg = df.groupby('Month').mean('TempAvgF')
    # temp_low = df.groupby('Month').mean('TempLowF')

    monthly_data = df.groupby('Month').agg({
        'TempHighF': 'mean',
        'TempAvgF': 'mean',
        'TempLowF': 'mean'
    }).reset_index()

    # 다른 view 함수에서 plt를 이미 그린 상태에서
    # 다시 그리는 경우를 대비하여, 초기화를 진행
    plt.clf()
    plt.figure(figsize=(10, 6))
    plt.plot(monthly_data['Month'], temp_high)
    # plt.plot(monthly_data['Month'], temp_avg)
    # plt.plot(monthly_data['Month'], temp_low)
    plt.title('Temperature Variation')
    plt.xlabel('Date')
    plt.xticks(range(0, len(monthly_data['Month']), 5))
    plt.ylabel('Temperature(Fahrenheit)')
    plt.legend(('High Temperature', 'Average Temperature', 'Low Temperature'))
    
    
    # 비어있는 버퍼 생성
    buffer = BytesIO()

    # 버퍼에 그래프 저장
    plt.savefig(buffer, format='png')

    # 버퍼의 내용을 base64로 인코딩,                   //  사용할 수 있도록 디코딩
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace("\n", '')

    # 버퍼를 닫아줌
    buffer.close()

    # 이미지를 웹페이지에 표시하기 위해 URI 형식(주소 형식)으로 만들어진 문자열 생성
    context = {
        # chart_img : 저장된 이미지의 경로
        'chart_img' : f'data:image/png;base64,{image_base64}',
    }
    return render(request, 'weathers/problem3.html', context)

def problem4(request):
    df = pd.read_csv(csv_path)
    df['Events'] = df['Events'].replace(r'^\s*$', 'No Events', regex=True)
    data = df['Events']

    rain = 0
    no_event = 0
    thunderstorm = 0
    fog = 0
    snow = 0

    for i in data:
        if 'No Events' in i:
            no_event += 1
            continue
        if 'Rain' in i:
            rain += 1
        if 'Thunderstorm' in i:
            thunderstorm += 1
        if 'Fog' in i:
            fog += 1
        if 'Snow' in i:
            snow += 1

    x= ['No Events','Rain','Thunderstorm','Fog','Snow']
    y= [no_event, rain, thunderstorm, fog, snow]
    # 이제 event_counts 딕셔너리에는 각 기상 현상의 발생 횟수가 저장됨
    plt.figure(figsize=(10, 6))
    plt.bar(x, y)
    plt.xlabel('Events')
    plt.ylabel('Counts')
    plt.title('Events Counts')
    plt.grid(True)

    # 비어있는 버퍼 생성
    buffer = BytesIO()

    # 버퍼에 그래프 저장
    plt.savefig(buffer, format='png')

    # 버퍼의 내용을 base64로 인코딩,                   //  사용할 수 있도록 디코딩
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace("\n", '')

    # 버퍼를 닫아줌
    buffer.close()

    # 이미지를 웹페이지에 표시하기 위해 URI 형식(주소 형식)으로 만들어진 문자열 생성
    context = {
        # chart_img : 저장된 이미지의 경로
        'chart_img' : f'data:image/png;base64,{image_base64}',
    }
    return render(request, 'weathers/problem4.html', context)
