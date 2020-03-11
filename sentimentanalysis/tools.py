def powcolumns(data, newcolumn='pow', *args):
    data[list(args)].multiply(data[newcolumn], axis="index")
    return data

def round(data, num=4):
        return data.round(num)