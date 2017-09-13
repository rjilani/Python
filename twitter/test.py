from twitter.util.configreader import ConfigReader

# config = ConfigParser.ConfigParser()
# print config.read('./config/config.ini')
#
# print config.sections()
#
# print config.get('Default','access_token')
#
# config.read('./config/globals.ini')
#
# a = config.get('Default','tags_to_watch').split()
#
# for i in a:
#     print i


# def filter_tweets(text,lst):
#     ltext = text.lower()
#     a = 0
#     for words in lst:
#         lwords = words.lower()
#         result = ltext.__contains__(lwords)
#         if result == True:
#             a = 1
#             return a
#     return a
#
#
# def filter_tweetssss(text,lst):
#     ltext = text.lower()
#     a = 0
#     for words in lst:
#         lwords = words.lower()
#         result = ltext.__contains__(lwords)
#         if result:
#             a = 1
#             return a
#     # print ("filter tweets down't see the tokem" + text)
#     return a
#
# a = filter_tweetssss("rashid my ",['java', 'python', 'javascript', 'ruby', 'docker', 'aws',
#                'azure', 'C#', 'C++', 'Angularjs', 'bigdata', 'Machine Learning', 'Scala', 'PHP'])
#
# print a

# configreader = ConfigReader('./config/globals.ini', 'TechnologyTweets')
#
# print configreader.index_type
# print configreader.access_token_secret
# print configreader.consumer_key

