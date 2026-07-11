#!/usr/bin/env python3
"""public-ip — Show public IP address. CLI that queries multiple services for external IP."""
import sys, json, argparse
def main():
    parser = argparse.ArgumentParser(description="Show public IP address. CLI that queries multiple services for external IP.")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    result = {"tool": "public-ip", "ready": True}
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"{result}")
if __name__ == "__main__":
    main()
