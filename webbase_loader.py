from langchain_community.document_loaders import WebBaseLoader
url = 'https://www.flipkart.com/apple-macbook-air-m2-16-gb-256-gb-ssd-macos-sequoia-mc7x4hn-a/p/itmdc5308fa78421?pid=COMH64PY76CJKBYU&lid=LSTCOMH64PY76CJKBYUM2PGKJ&marketplace=FLIPKART&cmpid=content_computer_23013654687_g_8965229628_gmc_pla&tgi=sem,1,G,11214002,g,search,,774151532861,,,,c,,,,,,,&entryMethod=23013654687&&cmpid=content_23013654687_gmc_pla&gad_source=1&gad_campaignid=23013654687&gbraid=0AAAAADxRY5_Fc2nm_ZykWNCWyb6kaCpeh&gclid=Cj0KCQiA5I_NBhDVARIsAOrqIsZLm-stPFz3A7agOSsZzy6VOqeC_c6BlbAhgWZGP3Qtm3JSjub3rd8aAm7XEALw_wcB'
loader = WebBaseLoader(url)
docs = loader.load()
print(docs)