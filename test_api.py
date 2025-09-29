import requests

base_url = "http://localhost:8000"
headers = {"X-API-Key": "secret-key"}

# Test lookup
response = requests.get(f"{base_url}/lookup?q=Jwara", headers=headers)
print("Lookup status:", response.status_code)
print("Lookup text:", response.text)
if response.status_code == 200:
    print("Lookup response:", response.json())
else:
    print("Lookup error")

# Test translate
response = requests.get(f"{base_url}/translate?code=NAMC-ASU.1.1", headers=headers)
print("Translate status:", response.status_code)
print("Translate text:", response.text)
if response.status_code == 200:
    print("Translate response:", response.json())
else:
    print("Translate error")

# Test codesystem
response = requests.get(f"{base_url}/codesystem/namaste", headers=headers)
print("CodeSystem response status:", response.status_code)
print("CodeSystem text:", response.text[:200])

# Test conceptmap
response = requests.get(f"{base_url}/conceptmap/namaste-to-icd11", headers=headers)
print("ConceptMap response status:", response.status_code)
print("ConceptMap text:", response.text[:200])
