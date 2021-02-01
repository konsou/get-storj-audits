#!/usr/bin/python3
import requests
import sys


def main():
    if len(sys.argv) < 2:
        print(f"Address not specified.")
        sys.exit()

    address = sys.argv[1]

    print(f"AUDIT STATS FOR {address}")

    response = requests.get(f"http://{address}/api/sno")
    satellites = response.json()['satellites']

    for satellite in satellites:
        response = requests.get(f"http://{address}/api/sno/satellite/{satellite['id']}")
        response_parsed = response.json()

        print(f"{satellite['url']}: Audits {response_parsed['audit']['successCount']} / "
              f"{response_parsed['audit']['totalCount']} (success / total) ")


if __name__ == '__main__':
    main()
