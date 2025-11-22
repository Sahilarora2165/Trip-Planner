import json # to convert python dictionaries into json format
import os # to access env variables
import requests # to send http requests -> here for talking with SERPER API
from langchain.tools import tool

class SearchTools():

    # '@' - Decorator that tells python how a function works. Here it works as an AI tool.
    @tool("Search the Internet")
    def search_internet(query):

        # Docstring
        """
        useful to search the internet about a
        given topic and return relevant results.
        """

        # Request to Serper AI
        top_result_to_return = 4 # top 4 results to show
        url = f"https://google.serper.dev/search" # Endpoint where we send our search request
        payload = json.dumps({"q": query}) # converts into json format for api.
        # extra info sent with the request - api key , and in json format
        headers = {
            'X-API-KEY': os.environ['SERPER_API_KEY'],
            'Content-Type': 'application/json',
        }

        # Raw data we get from the search result and storing them in response variable.
        response = requests.request("POST", url, headers=headers, data=payload)

        # This process the search result returned by the SERPER.
        if 'organic' not in response.json():  # Organic - Normal , non paid search results/website
            return "Sorry , I couldn't find anything about that, there could be an error with your serper api key."
        else:
            results = response.json()['organic'] # Converts the raw form of response in json and gets the value where key is organic.
            string = []
            for result in results[:top_result_to_return]:
                try:
                    string.append('\n'.join([
                        f"Title: {result['title']}", f"Link: {result['link']}",
                        f"Snippet: {result['snippet']}", "\n-----------------"
                    ]))
                except KeyError:
                    continue

            return '\n'.join(string)

