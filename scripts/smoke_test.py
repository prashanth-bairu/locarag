import requests


if __name__ == "__main__":
    print(requests.get("http://127.0.0.1:8000/health", timeout=5).json())
