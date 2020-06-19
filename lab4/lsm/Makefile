.phony: rebuild-kernel

all: count prevent rebuild-kernel
	sudo chown vagrant /dev/thook

count:
	gcc count.c -o count
	sudo chown vagrant /dev/thook
prevent:
	gcc prevent.c -o prevent
	sudo chown vagrant /dev/thook

first-build-kernel:
	rm -f *.deb && \
		tar -xf linux-source-3.16.tgz && \
		cd linux-source-3.16 && \
		cp ../config.i386_none_686-pae ./.config && \
		make ARCH=i386 oldconfig && \
		make -j`nproc` deb-pkg && \
		cd .. && \
		sudo dpkg -i *.deb && \
	touch /home/vagrant/secret

rebuild-kernel:
	rm -f *.deb && \
		cd linux-source-3.16 && \
		cp ../config.i386_none_686-pae ./.config && \
		make ARCH=i386 oldconfig && \
		make ARCH=i386 -j`nproc` && \
		sudo make ARCH=i386 install && \
	touch /home/vagrant/secret


clean:
	cd linux-source-3.16 && make clean
	rm -rf *.deb
	rm -f *.changes
	rm prevent count


reboot:
	sudo shutdown -r now
