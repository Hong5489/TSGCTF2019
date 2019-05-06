import zlib
f = open('easy_web/flag')
print zlib.decompress(f.read())