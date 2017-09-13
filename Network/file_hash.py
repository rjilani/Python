import hashlib

# print hashlib.algorithms_available
# print hashlib.algorithms_guaranteed

BLOCKSIZE = 65536
hasher = hashlib.sha1()
# hasher = hashlib.md5()
with open('./test.csv', 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(BLOCKSIZE)
print(hasher.hexdigest())
