# VirusTotal-Scan
Automate retrieving sha256 file hash using certutil, then input the hash to VirusTotal and return the scan results.

**Prerequisites:**
```python
py -m pip install requests
```
Enter your own VirusTotal API key in the ``"x-apikey"`` field under ``def runScan(url)``
![image](https://user-images.githubusercontent.com/103214796/164131213-be8f292d-6477-4f56-89aa-f483dc73b91f.png)
