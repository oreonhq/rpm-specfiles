%global source0_hash 1767fe155280361804cf1a62b2f77228bd764452668783050b6309cca888fb22

%{!?username:%global username	ip-sentinel}
%global service		ip-sentinel
%global homedir		%{_var}/lib/ip-sentinel

Summary:	Tool to prevent unauthorized usage of IP addresses
Name:		ip-sentinel
Version:	0.12
Release:	1934%{?dist}
License:	GPL-2.0-only
URL:		http://www.nongnu.org/ip-sentinel/
Source0:	http://savannah.nongnu.org/download/ip-sentinel/%{name}-%{version}.tar.bz2
Source1:	http://savannah.nongnu.org/download/ip-sentinel/%{name}-%{version}.tar.bz2.sig
Source2:	ip-sentinel.service
Patch0:		ip-sentinel-0.12-pidfile.patch
Patch1:		ip-sentinel-0.12-glibc.patch
Provides:	user(%username) = 1
Provides:	group(%username) = 1
BuildRequires:  gcc
BuildRequires:	which systemd
BuildRequires: make
Obsoletes: ip-sentinel-sysvinit < %{version}-%{release}
Provides: ip-sentinel-sysvinit = %{version}-%{release}
Obsoletes: ip-sentinel-minit < %{version}-%{release}
Provides: ip-sentinel-minit = %{version}-%{release}
Obsoletes: ip-sentinel-upstart < %{version}-%{release}
Provides: ip-sentinel-upstart = %{version}-%{release}
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
IP Sentinel is a tool that tries to prevent unauthorized usage of
IP addresses within an ethernet broadcast domain by answering ARP
requests. After receiving faked replies, requesting parties store
the MAC in their ARP tables and will send future packets to this
invalid MAC, rendering the IP unreachable.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p0 -b .pidfile
%patch -P1 -p0

# Create a sysusers.d config file
cat >ip-sentinel.sysusers.conf <<EOF
u ip-sentinel - 'IP sentinel user' %{homedir} -
EOF

%build
%configure --enable-release \
	   --with-initrddir=%{_initrddir} \
	   --with-username=%username \
           --disable-dietlibc
make %{?_smp_mflags} all

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install install-contrib
install -m750 -d $RPM_BUILD_ROOT%homedir
rm -rf $RPM_BUILD_ROOT%{_sysconfdir}/minit/
rm -rf $RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d/ip-sentinel

install -Dpm 755 %{SOURCE2} $RPM_BUILD_ROOT%{_unitdir}/ip-sentinel.service

install -m0644 -D ip-sentinel.sysusers.conf %{buildroot}%{_sysusersdir}/ip-sentinel.conf

%check
make check

%post
%systemd_post ip-sentinel.service

%preun
%systemd_preun ip-sentinel.service

%postun
%systemd_postun_with_restart ip-sentinel.service 

%triggerun -- ip-sentinel-sysvinit < 0.12-1909
# Save the current service runlevel info
# User must manually run systemd-sysv-convert --apply ip-sentinel
# to migrate them to systemd targets
/usr/bin/systemd-sysv-convert --save ip-sentinel >/dev/null 2>&1 ||:

# Run these because the SysV package being removed won't do them
/sbin/chkconfig --del ip-sentinel >/dev/null 2>&1 || :
/bin/systemctl try-restart ip-sentinel.service >/dev/null 2>&1 || :

%files
%doc AUTHORS COPYING ChangeLog NEWS README THANKS
%{_mandir}/*/*
%{_sbindir}/*
%{_unitdir}/ip-sentinel.service
%{_sysconfdir}/sysconfig/ip-sentinel
%attr(-,root,%username) %homedir
%{_sysusersdir}/ip-sentinel.conf

%changelog
%autochangelog
