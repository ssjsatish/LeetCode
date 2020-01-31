def build_max_heap():

def max_heapify(a):


def heapsort(a):
    build_max_heap(a)
    for i in range(len(a),2):
        a[1],a[i] = a[i],a[1]
        