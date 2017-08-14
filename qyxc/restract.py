
__author__ = 'WY'

import re
from scrapy.selector import Selector


#在html中提取信息并返回

def restractHeaderInfoForOneDay(headText):
    #提取每一天的头部信息
    info = dict()
    day_index_p = re.compile('<h2>(.*)</h2>')
    date_p = re.compile('<h3>(\w*)<span')
    line_p = re.compile('<a href.*?>(.*?)</a>')#非贪婪形式
    info['date'] = date_p.findall(headText)[0]
    info['day_index'] = day_index_p.findall(headText)[0]
    pos = line_p.findall(headText)
    pos = [filter_text2(filter_text2(x,'&nbsp;'),'\xa0') for x in pos]
    info['line'] = pos
    return info

def filter_text2(text,flag):
    if text.find(flag) is -1:
        return text
    else:
        return text.replace(flag,' ')

'''
@:parameter text 要匹配的文本
@:parameter regex 正则表达式
@:parameter func 对匹配结果处理的函数

@:return the result as a list
'''

def restract(regex, text, func=None ):
    pattern = re.compile(regex,re.S)
    r = pattern.findall(text)
    if func is None:
        return r
    else:
        if callable(func):
            func(r)
        else:
            raise Exception('参数三不可被调用')

def showResult(list):
    for i, item in enumerate(list):
        print(i,item)


def restractPoiArticle(poiText):
    #种类为景点的article
    info = dict()
    posNameWithSpanRe = '<h5 class="ellipsis".*?<(?:a|span) title="(.*?)"'
    scoreRe = '>(...)分' #得分
    peopleNumRe = '(\d*)人点评'
    bangNameRe = u'right.*\"(.*)榜'
    rankRe = '第(\d*)位'
    posInfoRe = 'planview-content-poi-user.*</em>(.*?)</div>'
    posName = restract(posNameWithSpanRe, poiText)
    score = restract(scoreRe,poiText)
    peopleNum = restract(peopleNumRe,poiText)
    rankName = restract(bangNameRe,poiText)
    rank = restract(rankRe,poiText)
    posInfo = restract(posInfoRe,poiText)
    if len(posName) is not 0:
        info['posName'] = filter_text2(filter_text2(posName[0],'&nbsp;'),'\xa0')
    else:
        info['posName'] = ''

    if len(score) is not 0:
        info['score'] = score[0]
    else:
        info['score'] = ''

    if len(peopleNum) is not 0:
        info['peopleNumOfCom'] = peopleNum[0]
    else:
        info['peopleNumOfCom'] = ''

    if len(rankName) is not 0:
        info['rankName'] = rankName[0].replace('>','')
    else:
        info['rankName'] = ''

    if len(rank) is not 0:
        info['rank'] = rank[0]
    else:
        info['rank'] = ''

    if len(posInfo) is not 0:
        info['posInfo'] = posInfo[0].strip()
    else:
        info['posInfo'] = ''

    if poiText.find('自定义') is not -1:
        info['type'] = '自定义'

    return info

def restractTrafficeArticle(trafficText):
    #提取traffic信息
    info = dict()
    artrifficRe = '<dd>.*?<span class="ellipsis" title="(.*?)">.*?</span>\s*?(?:<time>\s*(\S*?)\s*</time>)?\s*?</dd>'#提取当天航线信息，飞机和时间
    trifficSuggRe = '<span>(距离.*?)</span>'#建议 距离：1957KM，98%的用户选择了飞机，平均用时3小时。
    info['traffic'] = restract(artrifficRe,trafficText)
    info['sugg'] = restract(trifficSuggRe,trafficText)
    return info

def restractHotelArticle(hotelText):
    info = dict()
    hotelNameRe = '<(a|span) title=\"(.*?)\"'
    scoreRe = '用户评分(.*?)分'
    priceRe = '<b class="\w*">(\d*)</b>'
    addressRe = '<li class="place">(.*?)</li>'
    aroundPoiRe = '<b>(.*?)</b>'      #附近景点
    resonOfRecommendRe = '<li class="ellipsis" title="(.*?)">'#推荐理由
    info['hotelName'] = restract(hotelNameRe,hotelText)[0]
    score = restract(scoreRe,hotelText)
    price = restract(priceRe,hotelText)
    addressTemp = restract(addressRe, hotelText)
    info['score'] = score[0] if len(score) is not 0 else ''
    info['price'] = price[0] if len(price) is not 0 else ''
    info['address'] = restract('<a.*?>(.*?)</a>',addressTemp[0]) if len(addressTemp) is not 0 else []
    info['arounfPoi'] = restract(aroundPoiRe,hotelText)
    info['resonOfRecommend'] = restract(resonOfRecommendRe,hotelText)
    if hotelText.find('自定义住宿') is not -1:
        info['type'] = '自定义住宿'
    return info

def getArtileAsListForOneDay(dayText):
    infoList = []
    articleRe = '<article.*?</article>'#当前Day的所有article
    articleTexts = restract(articleRe, dayText)
    articleInfo = dict()
    for articleText in articleTexts:
        if articleText.find('class="hotel clearfix"') is not -1:
            articleInfo = restractHotelArticle(hotelText=articleText)
        elif articleText.find('class="poi clearfix"') is not -1:
            articleInfo = restractPoiArticle(poiText=articleText)
        elif articleText.find('class="traffic clearfix"') is not -1:
            articleInfo = restractTrafficeArticle(trafficText=articleText)
        infoList.append(articleInfo)
    return infoList

def getDistinceAsListForOneDay(dayText):
    infoList = []
    sepRe = '<div class="sep".*?</div>'#提取Day块的所有行走方式Div
    sepDisRe = '<span>(.*)</span>'
    li = restract(sepRe,dayText)
    for item in li:
        pattern = re.compile(sepDisRe,re.S)
        infoList.append(pattern.findall(item)[0])
    return infoList

def getHeaderAsDict(dayText):
    headerRe = '<header>.*?</header>'
    headerText = restract(headerRe,dayText)[0]
    return restractHeaderInfoForOneDay(headerText)
#提取每一天的信息
def restractDayInfo(dayText):
    infoList = []
    headerInfoDict = getHeaderAsDict(dayText)
    articleList = getArtileAsListForOneDay(dayText)
    distinceList = getDistinceAsListForOneDay(dayText)
    infoList.append(headerInfoDict)
    if len(articleList) is 0:
        infoList.append('当日暂无行程安排')
        return infoList
    for index, distinceinfo in enumerate(distinceList):
        infoList.append(articleList[index])
        infoList.append(distinceinfo)
    infoList.append(articleList[-1])
    return infoList

class Restractor(object):
    @staticmethod
    def restractXCInfo(response):
        infoList = []
        select = Selector(response)
        daysText = select.xpath("//div[@class='day']").extract()
        for dayText in  daysText:
            dayInfoList = restractDayInfo(dayText)
            infoList.append(dayInfoList)
        return infoList


