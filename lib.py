import requests
import concurrent.futures

subreddits = []

def scrape_data():
    """
    This function will return nothing but scrape all the data from reddit
    and cache it up for the program.
    """
    response_data = []
    
    # read the file reddit file and add that in global list
    with open("reddits.txt", "r") as r_file:
        for line in r_file:
            red_ = line.strip()
            subreddits.append(red_)
            print("Added subreddit", red_)

    def get_urls():             # helper
        urls = []
        for i in subreddits:
            u = "https://www.reddit.com/r/{}/top.json".format(i)
            urls.append(u)

        print(urls)
        return urls

    def load_url(url, timeout): # helper
        return requests.get(url, timeout = timeout, headers={"User-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1"})

    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        future_to_url = {executor.submit(load_url, url, 10): url for url in get_urls()}

        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
#                data = future.result().json()
#                print(data)     # debug
                response_data.append(future.result().json())
                
            except Exception as exc:
                print(exc)
            else:
                print("ok")

    return response_data        # list of json response


if __name__ == "__main__":
    print ("Lib has been directly invoked")

    json_l = scrape_data()

    for i in json_l:
        print(i["data"]["children"][0]["data"]["title"]) # target only 0th element #expect 3 titles

else:
    print ("lib has been imported!")
