In the first example, we made our custom "hello" kernel module.
We compiled this module using the MakeFile and make command
Later inserted the module. When we run 
```
lsmod | grep hello
```

```
vagrant@debian-8:~/lkm$ lsmod | grep hello
hello                  12418  0 
```

we can see that it's loaded. and if we run command which prints kernel logs

```
dmesg
```

`[14794.111725] Hello` we this one.

Later remove the module and we can see the  `[15257.051896] Bye`

These are custom logs which was written in the `hello.c`

```c++
module_init(hello_init);
module_exit(hello_exit);
```