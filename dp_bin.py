"""
Valid packing set.
$V=\{u| \sum{s_i*u_i}\le W}

"""


def get_sizes(a):
    """Returns number of sizes in array.
    If there are multiples of the same size it will increment the counts of the size.
    
    Arguments:
        a {[type]} -- [description]
    """

    sizes, counts = [], []
    for e in a:
        if e in sizes:
            i = sizes.index(e)
            counts[i] += 1
        else:
            # element is not there.
            sizes.append(e)
            # 1 item of that size
            counts.append(1)
    return sizes, counts

def valid(sizes, counts, W):
