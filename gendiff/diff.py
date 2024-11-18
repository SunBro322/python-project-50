
def check_diff(data1, data2):
    """ Сравнение двух словарей и получение нового с результатом """
    result = {}
    # sorted_data1 = dict(sorted(data1.items()))
    # sorted_data2 = dict(sorted(data2.items()))
    #
    # for k, v in sorted_data1.items():
    #     if k in sorted_data2:
    #         if v == sorted_data2[k]:
    #             result[k] = v
    #         else:
    #             result['- ' + k] = sorted_data1[k]
    #             result['+ ' + k] = sorted_data2[k]
    #     else:
    #         result['- ' + k] = sorted_data1[k]
    #
    # for k, v in sorted_data2.items():
    #     if k not in result:
    #         result['+ ' + k] = sorted_data2[k]
    #
    # return result

    keys = sorted(data1.keys() | data2.keys())
    for key in keys:
        if key in data1 and key not in data2:
            result[f'  - {key}'] = data1[key]
        elif key in data1 and key in data2 and data1[key] != data2[key]:
            result[f'  - {key}'] = data1[key]
            result[f'  + {key}'] = data2[key]
        elif key in data2 and key not in data1:
            result[f'  + {key}'] = data2[key]
        else:
            result[f'    {key}'] = data1[key]
    l = []
    for k, v in result.items():
        l.append(k + ': ' + str(v))
    r = '\n'.join(l)
    return f"{{\n{r}\n}}"
