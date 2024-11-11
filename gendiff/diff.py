
def check_diff(data1, data2):
    """ Сравнение двух словарей и получение нового с результатом """
    result = {}
    sorted_data1 = dict(sorted(data1.items()))
    sorted_data2 = dict(sorted(data2.items()))

    for k, v in sorted_data1.items():
        if k in sorted_data2:
            if v == sorted_data2[k]:
                result[k] = v
            else:
                result['- ' + k] = sorted_data1[k]
                result['+ ' + k] = sorted_data2[k]
        else:
            result['- ' + k] = sorted_data1[k]

    for k, v in sorted_data2.items():
        if k not in result:
            result['+ ' + k] = sorted_data2[k]

    return result
