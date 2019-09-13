from TikTokApi import TikTokapi



def getTrending(results):
    api = TikTokapi("browsermob-proxy/bin/browsermob-proxy")
    trending = api.trending(results)

    return len(trending)



def test_trending():
    assert getTrending(5) == 5
    assert getTrending(10) == 10
    assert getTrending(20) == 20