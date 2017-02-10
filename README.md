# dapper-selinux-policy

##About
The Dapper SELinux Policy package contains custom SELinux modules for Dapper Linux, since grsecurity seems to tighten up the requirements for some programs. This repo contains fixes for firewalld and abrt-coredump-hook services.


##Building
To build this package, first install an RPM development chain:

```bash
$ sudo dnf install fedora-packager fedora-review

```

Next, setup rpmbuild directories with

```bash
$ rpmdev-setuptree
```
And place the file dapper-selinux-policy.spec in the SPECS directory, and rename the dapper-selinux-policy directory to dapper-selinux-policy-0.1 and compress it:
```bash
$ mv dapper-selinux-policy.spec ~/rpmbuild/SPECS/
$ mv dapper-selinux-policy dapper-selinux-policy-0.1
$ tar -czvf dapper-selinux-policy-0.1.tar.gz dapper-selinux-policy-0.1
$ mv dapper-selinux-policy-0.1.tar.gz ~/rpmbuild/SOURCES/
```

and finally, you can build RPMs and SRPMs with:
```bash
$ cd ~/rpmbuild/SPECS
$ rpmbuild -ba dapper-selinux-policy.spec
```


