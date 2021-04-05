from tapi_yandex_metrika import YandexMetrikaStats
import requests

METRIKA_TOKEN = "ТОКЕН"
COUNTER_ID = НОМЕР СЧЕТЧИКА

api = YandexMetrikaStats(access_token=METRIKA_TOKEN)


# Запрос визитов из ПС Яндекс
paramsSEOYandex = dict(
    ids=COUNTER_ID,
    metrics="ym:s:visits",
    date1="8daysAgo",
    date2="yesterday",
    dimensions="ym:s:lastSearchEngineRoot,ym:s:date",
    filters="ym:s:lastSearchEngineRoot=='Yandex'",
    sort="ym:s:date",
    limit=100
)
result = api.stats().get(params=paramsSEOYandex)

data = result().transform()

# Обработка данных ПС Yandex
dataSEOYandexLastFinish = data[1][2]
dataSEOYandexRealFinish = data[-1][2]
dataSEOYandexCompare = "%.0f%%" % (100 * (dataSEOYandexRealFinish-dataSEOYandexLastFinish)/dataSEOYandexLastFinish)

# Запрос визитов из ПС Google
paramsSEOGoogle = dict(
    ids=COUNTER_ID,
    metrics="ym:s:visits",
    date1="8daysAgo",
    date2="yesterday",
    dimensions="ym:s:lastSearchEngineRoot,ym:s:date",
    filters="ym:s:lastSearchEngineRoot=='Google'",
    sort="ym:s:date",
    limit=100
)
result2 = api.stats().get(params=paramsSEOGoogle)

data2 = result2().transform()


# Обработка данных ПС Google
dataSEOGoogleLastFinish = data2[1][2]
dataSEOGoogleRealFinish = data2[-1][2]
dataSEOGoogleCompare = "%.0f%%" % (100 * (dataSEOGoogleRealFinish-dataSEOGoogleLastFinish)/dataSEOGoogleLastFinish)

# Запрос визитов из Яндекс Директ
'''
paramsPaidYDirect = dict(
    ids=COUNTER_ID,
    metrics="ym:s:visits",
    date1="8daysAgo",
    date2="yesterday",
    dimensions="ym:s:lastAdvEngine,ym:s:date",
    filters="ym:s:lastAdvEngine=='yandex.direct'",
    sort="ym:s:date",
    limit=100
)
result3 = api.stats().get(params=paramsPaidYDirect)

data3 = result3().transform()

# Обработка данных Яндекс Директ
dataPaidYDirectLastFinish = data3[1][2]
dataPaidYDirectRealFinish = data3[-1][2]
dataPaidYDirectCompare = "%.0f%%" % (100 * (dataPaidYDirectRealFinish-dataPaidYDirectLastFinish)/dataPaidYDirectLastFinish)
'''
# Запрос визитов из Google Adwords
paramsPaidGAdwords = dict(
    ids=COUNTER_ID,
    metrics="ym:s:visits",
    date1="8daysAgo",
    date2="yesterday",
    dimensions="ym:s:lastAdvEngine,ym:s:date",
    filters="ym:s:lastAdvEngine=='google_adwords'",
    sort="ym:s:date",
    limit=100
)
result4 = api.stats().get(params=paramsPaidGAdwords)

data4 = result4().transform()

# Обработка данных Google Adwords
dataPaidGAdwordsLastFinish = data4[1][2]
dataPaidGAdwordsRealFinish = data4[-1][2]
dataPaidGAdwordsCompare = "%.0f%%" % (100 * (dataPaidGAdwordsRealFinish-dataPaidGAdwordsLastFinish)/dataPaidGAdwordsLastFinish)

# Запрос визитов из Google Adwords
paramsPaidYMarket= dict(
    ids=COUNTER_ID,
    metrics="ym:s:visits",
    date1="8daysAgo",
    date2="yesterday",
    dimensions="ym:s:lastAdvEngine,ym:s:date",
    filters="ym:s:lastAdvEngine=='market'",
    sort="ym:s:date",
    limit=100
)
result5 = api.stats().get(params=paramsPaidYMarket)

data5 = result5().transform()

# Обработка данных Яндекс Маркет
dataPaidYMarketLastFinish = data5[1][2]
dataPaidYMarketRealFinish = data5[-1][2]
dataPaidYMarketCompare = "%.0f%%" % (100 * (dataPaidYMarketRealFinish-dataPaidYMarketLastFinish)/dataPaidYMarketLastFinish)

# Запрос визитов - прямые заходы
paramsDirectTraffic = dict(
    ids=COUNTER_ID,
    metrics="ym:s:visits",
    date1="8daysAgo",
    date2="yesterday",
    dimensions="ym:s:lastTrafficSource,ym:s:date",
    filters="ym:s:lastTrafficSource=='direct'",
    sort="ym:s:date",
    limit=100
)
result6 = api.stats().get(params=paramsDirectTraffic)

data6 = result6().transform()


#Выборка данных по прямым заходам
dataDirectTrafficLastFinish = data6[1][2]
dataDirectTrafficRealFinish = data6[-1][2]
dataDirectTrafficCompare = "%.0f%%" % (100 * (dataDirectTrafficRealFinish-dataDirectTrafficLastFinish)/dataDirectTrafficLastFinish)

paramsKeyword = dict(
    ids=COUNTER_ID,
    metrics="ym:s:visits",
    date1="8daysAgo",
    date2="yesterday",
    dimensions="ym:s:lastSearchPhrase,ym:s:date",
    filters="ym:s:lastSearchPhrase=='комус'",
    sort="ym:s:date",
    limit=100
)
result7 = api.stats().get(params=paramsKeyword)

data7 = result7().transform()


#Выборка данных по прямым заходам
dataKeywordLastFinish = data7[1][2]
dataKeywordRealFinish = data7[-1][2]
dataKeywordCompare = "%.0f%%" % (100 * (dataKeywordRealFinish-dataKeywordLastFinish)/dataKeywordLastFinish)

#Отправка в Telegram
tg_token = "ТОКЕН"

requests.get("https://api.telegram.org/bot{}/sendMessage".format(tg_token), params=dict(
   chat_id="ЧАТ_ID",
   parse_mode="html",
   text= #Трафик из поисковых систем
         "<b>Поисковые системы:</b>"
#Яндекс
         +"\n"
         +"\n"
         +"YANDEX"
         +"\n"
         +str(dataSEOYandexRealFinish)
         +" | "
         +str(dataSEOYandexLastFinish)
         +" | "
         +str(dataSEOYandexCompare)
# Google
         + "\n"
         + "GOOGLE"
         + "\n"
         + str(dataSEOGoogleRealFinish)
         + " | "
         + str(dataSEOGoogleLastFinish)
         + " | "
         + str(dataSEOGoogleCompare)
         +"\n"
         +"\n"
         +"<b>Рекламные системы:</b>"
#Яндекс Директ
'''
         +"\n"
         +"\n"
         +"YANDEX DIRECT"
         +"\n"
         +str(dataPaidYDirectRealFinish)
         +" | "
         +str(dataPaidYDirectLastFinish)
         +" | "
         +str(dataPaidYDirectCompare)
         +"\n"
'''
#Google Adwords
         +"GOOGLE ADWORDS"
         + "\n"
         + str(dataPaidGAdwordsRealFinish)
         + " | "
         + str  (dataPaidGAdwordsLastFinish)
         + " | "
         + str(dataPaidGAdwordsCompare)
         +"\n"
#Yandex Market
        +"YANDEX MARKET"
         + "\n"
         + str(dataPaidYMarketRealFinish)
         + " | "
         + str(dataPaidYMarketLastFinish)
         + " | "
         + str(dataPaidYMarketCompare)
         +"\n"
         +"\n"
         +"<b>Сезонные триггеры:</b>"
#Сезонные триггеры
         +"\n"
         +"\n"
#Прямые заходы
         +"ПРЯМЫЕ ЗАХОДЫ"
         +"\n"
         +str(dataDirectTrafficRealFinish)
         +" | "
         +str(dataDirectTrafficLastFinish)
         +" | "
         +str(dataDirectTrafficCompare)
         +"\n"
#Переходы по слову Комус
         +"ОРГАНИКА ПО СЛОВУ 'КОМУС'"
         +"\n"
         +str(dataKeywordRealFinish)
         +" | "
         +str(dataKeywordLastFinish)
         +" | "
         +str(dataKeywordCompare)
))
