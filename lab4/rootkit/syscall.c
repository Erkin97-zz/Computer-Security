#include <linux/uaccess.h>
#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/init.h>
#include <asm/unistd.h>
#include <asm/page.h>
#include <asm/highmem.h>
#include <linux/mm.h>
#include <asm/tlbflush.h>
#include <linux/rwsem.h>

asmlinkage long (*orig_unlinkat)(int dfd, const char __user *filename, int flags);


asmlinkage long hacked_unlinkat(int dfd, const char __user *filename, int flags){
	return orig_unlinkat(dfd,filename,flags);
}



static int __init hook_init( void  ) {

    return 0;
}


void __exit hook_exit( void  ) {
	return;
}

module_init(hook_init);
module_exit(hook_exit);
MODULE_DESCRIPTION("module template");
MODULE_LICENSE("GPL");

