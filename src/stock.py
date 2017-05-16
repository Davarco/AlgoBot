
class Stock(object):

    # Important data for bollinger bands
    mean_price = 0
    deviation = 0

    def __init__(self, data_list):
        print("Length: ", len(data_list))
        mean_price = calc_mean(data_list)
        deviation = calc_dev(data_list, mean_price)


def calc_mean(data_list):
    # Go through the dictionary and find avg
    total = 0
    for data in data_list:
        price = data['Close']
        total += float(price)
    avg = total/len(data_list)
    print("Average price: ", avg)
    return avg


def calc_dev(data_list, mean):
    # Go through the dictionary and add the squares of the prices
    total = 0
    for data in data_list:
        price = data['Close']
        total += float(price)**2
    deviation = (total/len(data_list)) - (mean**2 * len(data_list))
    print("Deviation: ", deviation)
    return deviation

