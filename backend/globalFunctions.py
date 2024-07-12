# range
# [
#     {
#         'target': 'created_at',
#         'operator': 'range',
#         'value': ['2024-03-05', '2024-03-08 23:59:59'],
#     },
# ]


def genericModelFilter(data):
    filter = {
        'filter': [{
            'id__gte': '0',
        }],
        'exclude': [{
            'deleted_at__isnull': False,
        }],
    }

    if data is not {}:
        for item in data:
            array = []
            for _item in data[item]:
                if item != 'filter' and 'exclude': break
                temp = dict()

                if _item['operator'] == 'range':
                    temp[_item['target']+'__range'] = _item['value']

                if _item['operator'] == 'year':
                    temp[_item['target']+'__year'] = _item['value']

                if _item['operator'] == 'month':
                    temp[_item['target']+'__month'] = _item['value']

                if _item['operator'] == 'week':
                    temp[_item['target']+'__week'] = _item['value']

                if _item['operator'] == 'day':
                    temp[_item['target']+'__day'] = _item['value']


                if _item['operator'] == '=':
                    temp[_item['target']+'__exact'] = _item['value']

                if _item['operator'] == '>':
                    temp[_item['target']+'__gt'] = _item['value']

                if _item['operator'] == '<':
                    temp[_item['target']+'__lt'] = _item['value']

                if _item['operator'] == '>=':
                    temp[_item['target']+'__gte'] = _item['value']

                if _item['operator'] == '<=':
                    temp[_item['target']+'__lte'] = _item['value']


                if item == 'exclude': temp['deleted_at__isnull'] = False

                array.append(temp)


            filter[item] = array

    return(filter)


# def genericModelExclude(data):
#     exclude = dict()

#     if 'not' in data:
#         for item