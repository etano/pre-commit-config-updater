import argparse
import logging
import urllib.request


log = logging.getLogger(__name__)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--config",
        action="append",
        help="| separated config source and destination",
        required=True,
        destination="configs",
    )
    args = parser.parse_args(argv)

    # download most recent configuration files
    configs = [c.split("|") for c in args.config]
    for src, dst in configs:
        log.info(f"downloading {dst} from {src}")
        urllib.request.urlretrieve(src, dst)

    return 0


if __name__ == "__main__":
    exit(main())
