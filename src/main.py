#!/usr/bin/python3

import requests
import sys

from prettytable import PrettyTable


def main():
    if len(sys.argv) < 2:
        print(f"Address not specified.")
        sys.exit()

    address = sys.argv[1]

    print(f"AUDIT STATS FOR {address}")

    response = requests.get(f"http://{address}/api/sno")
    satellites = response.json()['satellites']

    table = PrettyTable(["Satellite", "Succesful audits", "Total audits"])

    for satellite in satellites:
        response = requests.get(f"http://{address}/api/sno/satellite/{satellite['id']}")
        response_parsed = response.json()

        table.add_row([satellite['url'], response_parsed['audit']['successCount'],
                       response_parsed['audit']['totalCount']])

        # print(f"{satellite['url']}: Audits {response_parsed['audit']['successCount']} / "
        #       f"{response_parsed['audit']['totalCount']} (success / total) ")

    table.align["Satellite"] = 'l'
    table.align["Succesful audits"] = 'r'
    table.align["Total audits"] = 'r'

    print(table)


if __name__ == '__main__':
    main()
