# Purpose:
#   Serve as a main entry point for the tool.
#
# Author:
#   Noah Juopperi<juopperi@osdl.org>

from services.fetcher import fetch_all
from output.excel import build_excel
from data.channels import CHANNELS

def main():
    print("running audit...\n")

    results = fetch_all(CHANNELS)

    print("building report...")
    build_excel(results)

    print("done!")

if __name__ == "__main__":
    main()