import requests
import os
from get_price import get_min
from datetime import datetime, timedelta, timezone

notice_telegram_url = "telegram_bot_address"
min_limit = 0.001
msg = '[OCCE] '


def push_telegram(msg):
    url = notice_telegram_url + msg
    requests.get(url=url)


if __name__ == '__main__':
    response = get_min()
    if 'telegram_bot' in os.environ:
        notice_telegram_url = str(os.getenv('telegram_bot'))
    tz_utc_8 = timezone(timedelta(hours=8))
    now = datetime.now(tz_utc_8)
    msg += str(now.strftime('%Y-%m-%d %H:%M:%S')) + '\n'

    if response == 'wrong':
        msg += 'There is no such exchange pair.\n' \
               'Maybe it is not available this time on https://www.occe.io\n' \
               'Please change to another pair.'
        push_telegram(msg)
    elif response == 'empty':
        msg += 'This time no active orders.\n' \
               'Please wait.' \
               'Check on https://www.occe.io'
        # push_telegram(msg)
    else:
        if float(response) >= min_limit:
            msg += 'It is %.8f now!!!\n' % float(response)
            msg += 'Check on https://www.occe.io/exchange/sugar_uah'
            push_telegram(msg)
