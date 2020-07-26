import argparse
import datetime
import pytz

parser = argparse.ArgumentParser()
parser.add_argument("mode", type=int)
args = parser.parse_args()

today_date = datetime.date.today()
now_datetime = datetime.datetime.now(tz=pytz.timezone("Asia/Yerevan"))


if args.mode == 1:
    print(today_date.strftime("%Y.%m.%d"))
elif args.mode == 2:
    print(now_datetime.strftime("%Y.%m.%d %H:%M:%S"))
elif args.mode == 3:
    print(now_datetime.strftime("%a %b %d %Y %H:%M:%S GMT%z"))
else:
    print("Something went wrong!")