from elasticsearch import Elasticsearch

es = Elasticsearch()


def post_tweets(index, doc_type, body):
    es.index(index=index, doc_type=doc_type, body=body)


def filter_tweets(text, lst):
    ltext = text.lower()
    a = 0
    for words in lst:
        lwords = words.lower()
        result = ltext.__contains__(lwords)
        if result:
            a = 1
            return a
    # print ("filter tweets down't see the tokem" + text)
    return a
