import requests

base_url = "http://127.0.0.1:5000"

def get_random_number(min_value=0, max_value=100):
    url = f"{base_url}/random_number"
    payload = {"min": min_value, "max": max_value}
    response = requests.post(url, json=payload)
    
    if response.status_code != 200:
        raise Exception("Failed to get random number")
    else:
        return response.json()["random_number"]
    
def calculate(num1, num2, operation):
    url = f"{base_url}/calculate"
    payload = {"num1": num1, "num2": num2, "operation": operation}
    response = requests.post(url, json=payload)
    
    if response.status_code != 200:
        raise Exception("Failed to calculate")
    else:
        return response.json()["result"]
    
if __name__ == "__main__":
    print(get_random_number())
    print(calculate(5, 3, "add"))
    print(calculate(5, 3, "subtract"))
    print(calculate(5, 3, "multiply"))
    print(calculate(5, 3, "divide"))
    
    respond = requests.put(f"{base_url}/user/1", json={"name": "John Doe", "age": 30})
    
    print(respond.json()["message"])
    
    respond = requests.get(f"{base_url}/user/1")
    
    print(respond.json()["name"], respond.json()["age"])