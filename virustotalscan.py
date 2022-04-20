import subprocess
import requests

def getFilehash(userinput):
    result = subprocess.check_output(f'certutil.exe -hashfile "{userinput}" sha256', universal_newlines=True)
    query = result.split()[5]
    print(query)
    getURL(query)

def getURL(query):
    url = f"https://www.virustotal.com/api/v3/search?query={query}"
    runScan(url)

def runScan(url):
    headers = {
    "Accept": "application/json",
    "x-apikey": "enter your own VirusTotal API key within the quotes here"
    }

    response = requests.request("GET", url, headers=headers)

    print(response.text)
    input('Press enter to exit')
    exit()

question = input('Do you need to retrieve the file hash? Type yes or no: ').lower()
if question == 'yes':
    userinput = input('Give me a file path to retrieve its hash: ')
    getFilehash(userinput)

elif question == 'no':
    query = input('Give me a hash or URL to scan with VirusTotal: ')
    getURL(query)
    input('Press enter to exit')
    exit()
