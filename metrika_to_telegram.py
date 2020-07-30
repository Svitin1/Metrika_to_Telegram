from tapi_yandex_metrika import YandexMetrikaStats
import requests

METRIKA_TOKEN = "ВАШ ТОКЕН"
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
dataSEOYandexLast = data[1]
dataSEOYandexLastFinish = dataSEOYandexLast[2]
dataSEOYandexReal = data[-1]
dataSEOYandexRealFinish = dataSEOYandexReal[2]
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
dataSEOGoogleLast = data2[1]
dataSEOGoogleLastFinish = dataSEOGoogleLast[2]
dataSEOGoogleReal = data2[-1]
dataSEOGoogleRealFinish = dataSEOGoogleReal[2]
dataSEOGoogleCompare = "%.0f%%" % (100 * (dataSEOGoogleRealFinish-dataSEOGoogleLastFinish)/dataSEOGoogleLastFinish)

# Запрос визитов из Яндекс Директ
paramsPaidYDirect = dict(
    ids=COUNTER_ID,
    metrics="ym:s:visits",
    date1="8daysAgo",
    date2="yesterday",
    dimensions="ym:s:lastAdvEngine,ym:s:date",
    filters="ym:s:lastAdvEngine=='ya_direct'",
    sort="ym:s:date",
    limit=100
)
result3 = api.stats().get(params=paramsPaidYDirect)

data3 = result3().transform()

# Обработка данных Яндекс Директ
dataPaidYDirectLast = data3[1]
dataPaidYDirectLastFinish = dataPaidYDirectLast[2]
dataPaidYDirectReal = data3[-1]
dataPaidYDirectRealFinish = dataPaidYDirectReal[2]
dataPaidYDirectCompare = "%.0f%%" % (100 * (dataPaidYDirectRealFinish-dataPaidYDirectLastFinish)/dataPaidYDirectLastFinish)

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
dataPaidGAdwordsLast = data4[1]
dataPaidGAdwordsLastFinish = dataPaidGAdwordsLast[2]
dataPaidGAdwordsReal = data4[-1]
dataPaidGAdwordsRealFinish = dataPaidGAdwordsReal[2]
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
dataPaidYMarketLast = data5[1]
dataPaidYMarketLastFinish = dataPaidYMarketLast[2]
dataPaidYMarketReal = data5[-1]
dataPaidYMarketRealFinish = dataPaidYMarketReal[2]
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
dataDirectTrafficLast = data6[1]
dataDirectTrafficLastFinish = dataDirectTrafficLast[2]
dataDirectTrafficReal = data6[-1]
dataDirectTrafficRealFinish = dataDirectTrafficReal[2]
dataDirectTrafficCompare = "%.0f%%" % (100 * (dataDirectTrafficRealFinish-dataDirectTrafficLastFinish)/dataDirectTrafficLastFinish)

paramsKeyword = dict(
    ids=COUNTER_ID,
    metrics="ym:s:visits",
    date1="8daysAgo",
    date2="yesterday",
    dimensions="ym:s:lastSearchPhrase,ym:s:date",
    filters="ym:s:lastSearchPhrase=='ВАШ КЕЙВОРД'",
    sort="ym:s:date",
    limit=100
)
result7 = api.stats().get(params=paramsKeyword)

data7 = result7().transform()


#Выборка данных по прямым заходам
dataKeywordLast = data7[1]
dataKeywordLastFinish = dataKeywordLast[2]
dataKeywordReal = data7[-1]
dataKeywordRealFinish = dataKeywordReal[2]
dataKeywordCompare = "%.0f%%" % (100 * (dataKeywordRealFinish-dataKeywordLastFinish)/dataKeywordLastFinish)

#Отправка в Telegram
tg_token = "ВАШ ТОКЕН ТЕЛЕГРАМ"

requests.get("https://api.telegram.org/bot{}/sendMessage".format(tg_token), params=dict(
   chat_id="ЧАТ ID",
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
#Переходы по слову 
         +"ОРГАНИКА ПО СЛОВУ ''"
         +"\n"
         +str(dataKeywordRealFinish)
         +" | "
         +str(dataKeywordLastFinish)
         +" | "
         +str(dataKeywordCompare)
))

