import argparse
from jobs.logic import run_job


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--catalog", required=True)
    parser.add_argument("--source", required=True)
    parser.add_argument("--limit", type=int, default=10)

    args = parser.parse_args()

    run_job(
        catalog=args.catalog,
        source=args.source,
        limit=args.limit
    )
