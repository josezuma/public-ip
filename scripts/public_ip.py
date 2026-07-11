#!/usr/bin/env python3
"""CLI: public-ip"""
import sys, json, argparse
from datetime import datetime
def main():
    parser = argparse.ArgumentParser(description="Public Ip")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    r = {"tool": "public-ip", "v": "1.0.0", "author": "Jose Zuma"}
    print(json.dumps(r, indent=2) if args.json else f"{name} v1.0.0")
if __name__ == "__main__": main()
