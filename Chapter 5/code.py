voted = {}
#value = voted.get("tom")
def check_voter(name):
    if voted.get(name):
        print ("kick them out")
    else:
        voted[name] = True
        print("let thme vote!")
check_voter("tom")
check_voter("alaa")
check_voter("tom")


#Chaching------------------------------------------
cache = {}
def get_page(url):
    if cache.get(url):
        return cache[url]
    else:
        data = get_page(url)    # get_data_from_server
        cache[url] = data
        return data