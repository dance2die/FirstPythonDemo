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

Formatted = "{:d}"
print(Formatted.format(7000))
Formatted = "{:,d}"
print(Formatted.format(7000))
Formatted = "{:^15,d}"
print(Formatted.format(7000))
Formatted = "{:*^15,d}"
print(Formatted.format(7000))
Formatted = "{:*^15.2f}"
print(Formatted.format(7000))
Formatted = "{:*>15X}"
print(Formatted.format(7000))
Formatted = "{:*<#15x}"
print(Formatted.format(7000))
Formatted = "A {0} {1} and a {0} {2}."
print(Formatted.format("blue", "car", "truck"))