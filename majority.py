'''definition and test of majority algorithm from class.'''

def majority(data, tieBreaker=None):
    '''Return majority element of sequence data, OR
    tieBreaker if  exactly half of the elements in data are tieBreaker, OR
    None otherwise.  Examples:

    >>> d = [1, 3, 1, 1, 1, 3, 3, 1, 3, 3]
    >>> print(majority(d))
    None
    >>> d.append(3)
    >>> majority(d)
    3
    >>> majority('a'*25 + 'b'*49 + 'a'*25)
    'a'
    >>> s = 'aabbbc'*1000000 #length 6 million
    >>> print(majority(s))
    None
    >>> majority(s+'bdbb')
    'b'
    '''      
    n = len(data)
    if n == 0:
        return tieBreaker
##    input("Continue from: {}, {}".format(data,tieBreaker))
    pairs = [] # empty list
    if n % 2 == 1:
        tieBreaker = data[-1] # last element in Python sequence
    for i in range(0, n-1, 2): # for(i = 0; i < n-1; i+=2)
        if data[i] == data[i+1]:
            pairs.append(data[i])
    major = majority(pairs, tieBreaker)
    if major is None:
        return None
    nMajor = data.count(major) # handy method does the obvious
    if 2*nMajor > n or (2*nMajor == n and major == tieBreaker):
        return major
    return None # candidate did not pan out

if __name__ == '__main__':
    import doctest
    print('testing...')
    doctest.testmod(verbose=True)

##print(majority('abbcb'*5))
##d = [1, 3, 1, 1, 1, 3, 3, 1, 3, 3]
##print(majority(d))
##d.append(3)
##print(majority(d))
##print(majority('a'*25 + 'b'*49 + 'a'*25))
##s = 'aabbbc'*10 #length 6 million
##print(majority(s))
##print(majority(s+'bdbb'))

