from flask import Flask
from flask import jsonify
from collections import defaultdict,Counter
from flask import request
from newsapi.newsapi_exception import NewsAPIException
from newsapi.newsapi_client import NewsApiClient

application = Flask(__name__)

@application.route('/alldata')
def alldatafunc():
    freq = {}
    fq = []
    resultfin = []
    cnnup = defaultdict(list)
    foxup = defaultdict(list)
    renderup = defaultdict(list)
    newsapi = NewsApiClient(api_key="d11761b89fdb4599b1497bf951690000")
    cnn = newsapi.get_top_headlines(sources="CNN",page_size=20)
    fox = newsapi.get_top_headlines(sources="FOX-News",page_size=20)
    render = newsapi.get_top_headlines(page_size=100)
    
    
    for i in cnn['articles']:
        if i['title'] is None or i['title'] == "" or i['title'] == "null" or i['author'] is None or i['author'] == ""  or i['author'] == "null" or i['description'] is None or i['description'] == "" or i['description'] == "null" or i['source'] is None or i['source'] == "" or i['source'] == "null"  or i['url'] is None or i['url'] == ""  or i['url'] == "null" or i['urlToImage'] is None or i['urlToImage'] == "" or i['urlToImage'] == "null" :
            pass
        else:
            cnnup['articles'].append(i)
    
    
    for i in fox['articles']:
        if i['title'] is None or i['title'] == "" or i['title'] == "null" or i['author'] is None or i['author'] == ""  or i['author'] == "null" or i['description'] is None or i['description'] == "" or i['description'] == "null" or i['source'] is None or i['source'] == "" or i['source'] == "null"  or i['url'] is None or i['url'] == ""  or i['url'] == "null" or i['urlToImage'] is None or i['urlToImage'] == "" or i['urlToImage'] == "null" :
            pass
        else:
            foxup['articles'].append(i)

    for i in render['articles']:
        if i['title'] is None or i['title'] == "" or i['title'] == "null" or i['author'] is None or i['author'] == ""  or i['author'] == "null" or i['description'] is None or i['description'] == "" or i['description'] == "null" or i['source'] is None or i['source'] == "" or i['source'] == "null"  or i['url'] is None or i['url'] == ""  or i['url'] == "null" or i['urlToImage'] is None or i['urlToImage'] == "" or i['urlToImage'] == "null" :
            pass
        else:
            renderup['articles'].append(i)

    for i in render['articles']:
        fq.append(i['title'])
    fq1 = dict(Counter(" ".join(fq).lower().split()))
   

   
    stop_words=['a', "a's", 'able', 'about', 'above', 'according', 'accordingly', 'across', 'actually', 'after', 'afterwards', 'again', 'against', "ain't", 'all', 'allow', 'allows', 'almost', 'alone', 'along', 'already', 'also', 'although', 'always', 'am', 'among', 'amongst', 'an', 'and', 'another', 'any', 'anybody', 'anyhow', 'anyone', 'anything', 'anyway', 'anyways', 'anywhere', 'apart', 'appear', 'appreciate', 'appropriate', 'are', "aren't", 'around', 'as', 'aside', 'ask', 'asking', 'associated', 'at', 'available', 'away', 'awfully', 'b', 'be', 'became', 'because', 'become', 'becomes', 'becoming', 'been', 'before', 'beforehand', 'behind', 'being', 'believe', 'below', 'beside', 'besides', 'best', 'better', 'between', 'beyond', 'both', 'brief', 'but', 'by', 'c', "c'mon", "c's", 'came', 'can', "can't", 'cannot', 'cant', 'cause', 'causes', 'certain', 'certainly', 'changes', 'clearly', 'co', 'com', 'come', 'comes', 'concerning', 'consequently', 'consider', 'considering', 'contain', 'containing', 'contains', 'corresponding', 'could', "couldn't", 'course', 'currently', 'd', 'definitely', 'described', 'despite', 'did', "didn't", 'different', 'do', 'does', "doesn't", 'doing', "don't", 'done', 'down', 'downwards', 'during', 'e', 'each', 'edu', 'eg', 'eight', 'either', 'else', 'elsewhere', 'enough', 'entirely', 'especially', 'et', 'etc', 'even', 'ever', 'every', 'everybody', 'everyone', 'everything', 'everywhere', 'ex', 'exactly', 'example', 'except', 'f', 'far', 'few', 'fifth', 'first', 'five', 'followed', 'following', 'follows', 'for', 'former', 'formerly', 'forth', 'four', 'from', 'further', 'furthermore', 'g', 'get', 'gets', 'getting', 'given', 'gives', 'go', 'goes', 'going', 'gone', 'got', 'gotten', 'greetings', 'h', 'had', "hadn't", 'happens', 'hardly', 'has', "hasn't", 'have', "haven't", 'having', 'he', "he's", 'hello', 'help', 'hence', 'her', 'here', "here's", 'hereafter', 'hereby', 'herein', 'hereupon', 'hers', 'herself', 'hi', 'him', 'himself', 'his', 'hither', 'hopefully', 'how', 'howbeit', 'however', 'i', "i'd", "i'll", "i'm", "i've", 'ie', 'if', 'ignored', 'immediate', 'in', 'inasmuch', 'inc', 'indeed', 'indicate', 'indicated', 'indicates', 'inner', 'insofar', 'instead', 'into', 'inward', 'is', "isn't", 'it', "it'd", "it'll", "it's", 'its', 'itself', 'j', 'just', 'k', 'keep', 'keeps', 'kept', 'know', 'knows', 'known', 'l', 'last', 'lately', 'later', 'latter', 'latterly', 'least', 'less', 'lest', 'let', "let's", 'like', 'liked', 'likely', 'little', 'look', 'looking', 'looks', 'ltd', 'm', 'mainly', 'many', 'may', 'maybe', 'me', 'mean', 'meanwhile', 'merely', 'might', 'more', 'moreover', 'most', 'mostly', 'much', 'must', 'my', 'myself', 'n', 'name', 'namely', 'nd', 'near', 'nearly', 'necessary', 'need', 'needs', 'neither', 'never', 'nevertheless', 'new', 'next', 'nine', 'no', 'nobody', 'non', 'none', 'noone', 'nor', 'normally', 'not', 'nothing', 'novel', 'now', 'nowhere', 'o', 'obviously', 'of', 'off', 'often', 'oh', 'ok', 'okay', 'old', 'on', 'once', 'one', 'ones', 'only', 'onto', 'or', 'other', 'others', 'otherwise', 'ought', 'our', 'ours', 'ourselves', 'out', 'outside', 'over', 'overall', 'own', 'p', 'particular', 'particularly', 'per', 'perhaps', 'placed', 'please', 'plus', 'possible', 'presumably', 'probably', 'provides', 'q', 'que', 'quite', 'qv', 'r', 'rather', 'rd', 're', 'really', 'reasonably', 'regarding', 'regardless', 'regards', 'relatively', 'respectively', 'right', 's', 'said', 'same', 'saw', 'say', 'saying', 'says', 'second', 'secondly', 'see', 'seeing', 'seem', 'seemed', 'seeming', 'seems', 'seen', 'self', 'selves', 'sensible', 'sent', 'serious', 'seriously', 'seven', 'several', 'shall', 'she', 'should', "shouldn't", 'since', 'six', 'so', 'some', 'somebody', 'somehow', 'someone', 'something', 'sometime', 'sometimes', 'somewhat', 'somewhere', 'soon', 'sorry', 'specified', 'specify', 'specifying', 'still', 'sub', 'such', 'sup', 'sure', 't', "t's", 'take', 'taken', 'tell', 'tends', 'th', 'than', 'thank', 'thanks', 'thanx', 'that', "that's", 'thats', 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'thence', 'there', "there's", 'thereafter', 'thereby', 'therefore', 'therein', 'theres', 'thereupon', 'these', 'they', "they'd", "they'll", "they're", "they've", 'think', 'third', 'this', 'thorough', 'thoroughly', 'those', 'though', 'three', 'through', 'throughout', 'thru', 'thus', 'to', 'together', 'too', 'took', 'toward', 'towards', 'tried', 'tries', 'truly', 'try', 'trying', 'twice', 'two', 'u', 'un', 'under', 'unfortunately', 'unless', 'unlikely', 'until', 'unto', 'up', 'upon', 'us', 'use', 'used', 'useful', 'uses', 'using', 'usually', 'uucp', 'v', 'value', 'various', 'very', 'via', 'viz', 'vs', 'w', 'want', 'wants', 'was', "wasn't", 'way', 'we', "we'd", "we'll", "we're", "we've", 'welcome', 'well', 'went', 'were', "weren't", 'what', "what's", 'whatever', 'when', 'whence', 'whenever', 'where', "where's", 'whereafter', 'whereas', 'whereby', 'wherein', 'whereupon', 'wherever', 'whether', 'which', 'while', 'whither', 'who', "who's", 'whoever', 'whole', 'whom', 'whose', 'why', 'will', 'willing', 'wish', 'with', 'within', 'without', "won't", 'wonder', 'would', 'would', "wouldn't", 'x', 'y', 'yes', 'yet', 'you', "you'd", "you'll", "you're", "you've", 'your', 'yours', 'yourself', 'yourselves', 'z', 'zero']
    
    stop_char = ['-','!','@','#','$','%','^','&','*','|','+','-']
    
    for i,v in fq1.items():
        if i not in stop_words:
            if i not in stop_char:
                freq[i] = int(v)

    result = dict(sorted(freq.items() , key=lambda t : t[1] , reverse=True))
    flag = 0
    for key,val in result.items():
        flag += 1
        resultfin.append({"word": key, "size": val})
        if flag == 30:
            break

    
    masterdic = {}
    masterdic["cnnnews"] = cnnup
    masterdic["foxnews"] = foxup
    masterdic["rendernews"] = renderup
    masterdic["wordcloud"] = resultfin
    
    return jsonify(masterdic)

@application.route('/')
def indexpage():
    return application.send_static_file("index.html")

@application.route('/entertainment')
def category1():
    page1 = request.args.get('data')
    obj1 = getresource(page1)
    return obj1 

@application.route('/general')
def category2():
    page2 = request.args.get('data')
    obj2 = getresource(page2)
    return obj2 

@application.route('/business')
def category3():
    page3 = request.args.get('data')
    obj3 = getresource(page3)
    return obj3 

@application.route('/sports')
def category4():
    page4 = request.args.get('data')
    obj4 = getresource(page4)
    return obj4 

@application.route('/health')
def category5():
    page5 = request.args.get('data')
    obj5 = getresource(page5)
    return obj5 

@application.route('/science')
def category6():
    page6 = request.args.get('data')
    obj6 = getresource(page6)
    return obj6 

@application.route('/technology')
def category7():
    page7 = request.args.get('data')
    obj7 = getresource(page7)
    return obj7 

@application.route('/all')
def category8():
    diccc = {}
    newsapi = NewsApiClient(api_key="d11761b89fdb4599b1497bf951690000")
    sources = newsapi.get_sources(language="en",country="us")
    return jsonify(sources)


def getresource(searchfor):
    dicc = {}
    newsapi = NewsApiClient(api_key="d11761b89fdb4599b1497bf951690000")
    sources = newsapi.get_sources(category= searchfor,language="en",country="us")
    return jsonify(sources)

@application.route('/getsearchresult')
def getsearchresult():
    searchup = defaultdict(list)
    newsapi = NewsApiClient(api_key="d11761b89fdb4599b1497bf951690000")
    keyword_ = request.args.get('keyword')
    print("keyword",keyword_)
    from_ = request.args.get('from')
    print("keyword",from_)
    to_ = request.args.get('todate')
    print("keyword",to_)
    source_ = request.args.get('source')
    print("keyword",source_)

    if source_ == "all":
        try:
            final_result = newsapi.get_everything(q = keyword_ ,from_param = from_ ,to= to_,language="en",page_size=30,sources="",sort_by="publishedAt")
        except NewsAPIException as error:
            return str(error) 
    else:
        try:
            final_result = newsapi.get_everything(q = keyword_ ,from_param = from_ ,to= to_,sources=source_,language="en",page_size=30,sort_by="publishedAt")
        except NewsAPIException as error:

            return str(error)
   
        
        

    data = final_result["articles"]
    for i in data:
        if i['title'] is None or i['title'] == "" or i['title'] == "null" or i['author'] is None or i['author'] == "" or i['author'] == "null" or i['description'] is None or i['description'] == "" or i['description'] == "null" or i['source'] is None or i['source'] == "" or i['source'] == "null" or i['url'] is None or i['url'] == "" or i['url'] == "null" or i['urlToImage'] is None or i['urlToImage'] == "" or i['urlToImage'] == "null" or i['publishedAt'] is None or i['publishedAt'] == "" or i['publishedAt'] == "null":
            pass
        else:
            searchup['articles'].append(i) 

    return jsonify(searchup)

        
if __name__ == "__main__":
    application.run(debug=True)