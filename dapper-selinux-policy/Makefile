# Build Dapper Linux Specific SELinux Policy
# type "make" to build

all: dapper-abrtinstallcc.pp.bz2 dapper-firewalld.pp.bz2

dapper-abrtinstallcc.pp.bz2: dapper-abrtinstallcc.pp
	@echo Compressing $^ -\ dapper-abrtinstallcc.pp
	bzip2 -9 $^

dapper-firewalld.pp.bz2: dapper-firewalld.pp
	@echo Compressing $^ -\ dapper-firewalld.pp
	bzip2 -9 $^

dapper-abrtinstallcc.pp: dapper-abrtinstallcc.te
	checkmodule -M -m -o dapper-abrtinstallcc.mod dapper-abrtinstallcc.te
	semodule_package -o dapper-abrtinstallcc.pp -m dapper-abrtinstallcc.mod

dapper-firewalld.pp: dapper-firewalld.te
	checkmodule -M -m -o dapper-firewalld.mod dapper-firewalld.te
	semodule_package -o dapper-firewalld.pp -m dapper-firewalld.mod

clean:
	rm -f *~ *.tc *.pp *.pp.bz2 *.mod
	rm -rf tmp
