import sys
import mokuai2
from mokuai2 import add

print('命令行参数如下:')
for i in sys.argv:
    print(i)

print('\n\nPython 路径为：', sys.path, '\n')

num = add(10,20)
print(num)

if __name__ == '__main__':
   print('程序自身在运行')
else:
   print('我来自另一模块')

print(dir(mokuai2))

s = 1/7
print(str(s))
print(repr(s))

for x in range(1,11):
    print(repr(x).rjust(2),repr(x*x).rjust(3),end='')
    print(repr(x*x*x).rjust(4))

for y in range(1,11):
    print('{0:2d} {1:3d} {2:4d}'.format(y,y*y,y*y*y))