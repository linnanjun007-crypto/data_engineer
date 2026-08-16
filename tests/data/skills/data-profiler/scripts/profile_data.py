"""Simple data profiler for integration testing."""

import argparse
import json


def main():
    parser = argparse.ArgumentParser(description="Profile data")
    parser.add_argument("--table", default="unknown", help="Table to profile")
    args = parser.parse_args()

    profile = {
        "status": "success",
        "table": args.table,
        "row_count": 1000,
        "null_percentage": 2.5,
        "unique_columns": ["id", "name"],
    }
    print(json.dumps(profile))


if __name__ == "__main__":
    main()
