from os import system

# Success code for linux terminal is equal to 0.

from cride.circles.models import Circle


def get_installation():
    request_install = system("pip install requests")
    tssplit_install = system("pip install tssplit")

    return request_install, tssplit_install


def create_circles_from_csv_file(url):

    request_, tssplit_ = get_installation()

    if not request_ or not tssplit_:
        import requests
        from tssplit import tssplit

        response = requests.get(url)

        if response.status_code == 200:

            datas_raw = response.text
            tssplit('"aaaa","bbbb","ccc,ddd"', quote='"', delimiter=',')
            datas_list = [tssplit(data, quote='"', delimiter=',') for data in datas_raw.split('\n')]
            for data in datas_list[1:]:
                print(data)
                Circle.objects.update_or_create(
                    name=data[0],
                    slug=data[1],
                    defaults={
                        'is_public': bool(data[2]),
                        'verified': bool(data[3]),
                        'members_limit': int(data[4]) if data[4].isnumeric() else 0,
                    },
                )
            else:
                print('ERROR: connection.')

    else:
        print('ERROR: problem on installation "requests" and "tssplit" packages.')
