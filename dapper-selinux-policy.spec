Name:			dapper-selinux-policy
Version:		0.1
Release:		2
License:		GPLv3
Group:			System Environment/Base
Summary:		SELinux Policies for Dapper Linux
BuildArch:		noarch
URL:			https://github.com/dapperlinux/dapper-selinux-policy
Requires(post):	selinux-policy-base, selinux-policy-targeted, policycoreutils, policycoreutils-python libselinux-utils
BuildRequires:	selinux-policy selinux-policy-devel
 
Source0:		%{name}-%{version}.tar.gz
 
%description
Dapper Linux requires some custom SELinux configuration that migrates from further hardening provided by grsecurity. This package addresses these issues.
 
%prep
%setup -q
 
%build
make
 
%install
install -d %{buildroot}%{_datadir}/selinux/packages
install -m 0644 dapper-abrtinstallcc.pp.bz2 %{buildroot}%{_datadir}/selinux/packages
install -m 0644 dapper-firewalld.pp.bz2 %{buildroot}%{_datadir}/selinux/packages
install -m 0644 dapper-gdmsessionworker.pp.bz2 %{buildroot}%{_datadir}/selinux/packages
install -m 0644 dapper-spicevdagentd.pp.bz2 %{buildroot}%{_datadir}/selinux/packages
 
%post
# Load the modules
%{_sbindir}/semodule -n -s targeted -i %{_datadir}/selinux/packages/dapper-abrtinstallcc.pp.bz2
%{_sbindir}/semodule -n -s targeted -i %{_datadir}/selinux/packages/dapper-firewalld.pp.bz2
%{_sbindir}/semodule -n -s targeted -i %{_datadir}/selinux/packages/dapper-gdmsessionworker.pp.bz2
%{_sbindir}/semodule -n -s targeted -i %{_datadir}/selinux/packages/dapper-spicevdagentd.pp.bz2
# Reload SELinux policy
if %{_sbindir}/selinuxenabled ; then
    %{_sbindir}/load_policy
fi
 
 
%postun
# Remove modules
%{_sbindir}/semodule -n -r dapper-abrtinstallcc &amp;&gt; /dev/null || :
%{_sbindir}/semodule -n -r dapper-firewalld &amp;&gt; /dev/null || :
%{_sbindir}/semodule -n -r dapper-gdmsessionworker &amp;&gt; /dev/null || :
%{_sbindir}/semodule -n -r dapper-spicevdagentd &amp;&gt; /dev/null || :
# Reload SELinux policy
if %{_sbindir}/selinuxenabled ; then
	%{_sbindir}/load_policy
fi
 
%files
%defattr(-,root,root,0755)
%attr(0644,root,root) %{_datadir}/selinux/packages/*.pp.bz2
 
%changelog
* Fri Feb 17 2017 Matthew Ruffell <msr50@uclive.ac.nz>
- Addition of gdmsessionworker and spicevdagentd SELinux rules

* Fri Feb 10 2017 Matthew Ruffell <msr50@uclive.ac.nz>
- Addition of abrt-coredump-hook and firewalld SELinux rules
