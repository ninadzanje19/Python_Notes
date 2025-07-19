########################################################################################################################
#                                               Tools
########################################################################################################################

"""Duck Duck Go search"""
from langchain_community.tools import DuckDuckGoSearchRun

search = DuckDuckGoSearchRun()

response_tools = search.invoke("Tell me about Langchain")
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
"""Serp Search"""
from langchain_community.utilities import SerpAPIWrapper
from constants import serp_api_key


params = {
    "engine": "google",
    "gl": "in",
    "hl": "en",
}
serp_search = SerpAPIWrapper(serpapi_api_key=serp_api_key,params=params)
#response_tools = serp_search.run("Tell me about Langchain")

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
"""Serper Search (Paid)"""
from constants import serper_api_key
import os
os.environ["SERPER_API_KEY"] = serper_api_key
from langchain_community.utilities import GoogleSerperAPIWrapper

serper_search = GoogleSerperAPIWrapper()
#response_tools = serper_search.run("Tell me about Langchain")

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
"""Brave Search"""
from langchain_community.tools import BraveSearch
from constants import brave_api_key

tool = BraveSearch.from_api_key(api_key=brave_api_key, search_kwargs={"count": 3})
#response_tools = tool.run("Tell me about Langchain")

#Checkout various tools at https://python.langchain.com/docs/integrations/tools/
