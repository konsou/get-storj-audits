import requests

ADDRESS = "192.168.42.3:14000"


def main():
    print(f"AUDIT STATS FOR {ADDRESS}")

    response = requests.get(f"http://{ADDRESS}/api/sno")
    satellites = response.json()['satellites']

    for satellite in satellites:
        response = requests.get(f"http://{ADDRESS}/api/sno/satellite/{satellite['id']}")
        response_parsed = response.json()

        print(f"{satellite['url']}: Audits {response_parsed['audit']['successCount']} / {response_parsed['audit']['totalCount']} (success / total) ")


if __name__ == '__main__':
    main()
