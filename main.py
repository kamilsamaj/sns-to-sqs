from pprint import pprint

import boto3


def main():
    sns_client = boto3.client("sns", region_name="us-east-1")
    pprint(sns_client.list_topics())


if __name__ == '__main__':
    main()
