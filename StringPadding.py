from pprint import pprint as pp

# https://pyformat.info/#string_pad_align
pp('"aaa".zfill(10)={}'.format("aaa".zfill(10)))
pp('"aaa".rjust(10)={}'.format("aaa".rjust(10)))
#pp("'{:_<10}'.format('test')={}".format('{:_<10}'.format('test')))
#pp("'{:<10}'.format('test')={}".format('{:<10}'.format('test')))
# pp("'{:*>10}'.format('test')={}".format('{:*>10}'.format('test')))
# pp("'{:*>}'.format('test')={}".format('{:*>}'.format('test')))
# pp("'{:*^10}'.format('test')={}".format('{:*^10}'.format('test')))
# pp("'{:*^10}'.format('test1')={}".format('{:*^10}'.format('test1')))
