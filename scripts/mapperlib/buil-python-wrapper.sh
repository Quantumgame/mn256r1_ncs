swig -python pyflags.i
gcc -fPIC -c biasusb.c pyflags_wrap.c -I/usr/include/python2.7
ld -shared biasusb.o pyflags_wrap.o -o _biasusb_wrap.so
