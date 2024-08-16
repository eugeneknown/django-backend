from django.utils import timezone

# range
# [
#     {
#         'target': 'created_at',
#         'operator': 'range',
#         'value': ['2024-03-05', '2024-03-08 23:59:59'],
#     },
# ]

# return bool if request status code is 404
def status_error(request):
    return True if request.status_code == 404 else False

# format datetime from model 
# documentaion https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
def formatDateTime(date, format='%Y-%m-%d %H:%M:%S'):
    return date.strftime(format)


def dateTimeNow():
    return timezone.now()


def genericModelFilter(data):
    filter = {
        'filter': {
            'id__gte': '0',
        },
        'exclude': {
            'deleted_at__isnull': False,
        },
    }

    if data is not {}:
        for item in data: #array in data
            if item != 'filter' and item != 'exclude': break
            temp = dict()
            for _item in data[item]: # dict in array in data

                if _item['operator'] == 'range':
                    temp.update({_item['target']+'__range': _item['value']})

                if _item['operator'] == 'year':
                    temp.update({_item['target']+'__year': _item['value']})

                if _item['operator'] == 'month':
                    temp.update({_item['target']+'__month': _item['value']})

                if _item['operator'] == 'week':
                    temp.update({_item['target']+'__week': _item['value']})

                if _item['operator'] == 'day':
                    temp.update({_item['target']+'__day': _item['value']})


                if _item['operator'] == '=':
                    temp.update({_item['target']+'__exact': _item['value']})

                if _item['operator'] == '<>':
                    temp.update({_item['target']+'__isnull': _item['value']})

                if _item['operator'] == '>':
                    temp.update({_item['target']+'__gt': _item['value']})

                if _item['operator'] == '<':
                    temp.update({_item['target']+'__lt': _item['value']})

                if _item['operator'] == '>=':
                    temp.update({_item['target']+'__gte': _item['value']})

                if _item['operator'] == '<=':
                    temp.update({_item['target']+'__lte': _item['value']})

            filter[item] = temp

        if 'exclude' in data:
            filter['exclude'].update({ 'deleted_at__isnull': False })

    return(filter)


# def genericModelExclude(data):
#     exclude = dict()

#     if 'not' in data:
#         for item