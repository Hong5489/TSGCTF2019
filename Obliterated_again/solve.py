import zlib
f = open('easy_web/problem/flag')
print zlib.decompress(f.read())