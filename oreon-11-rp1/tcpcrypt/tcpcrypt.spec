%global source0_hash 251213be8bfd0b9224f4d8d7a79fe1b8961a180f5a278f128376a66364a38ea3

%global _hardened_build 1
%global snapshot 0

Summary: Opportunistically encrypt TCP connections
Name: tcpcrypt
Version: 0.5
Release: 20%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
Url: http://tcpcrypt.org/
Source0: http://tcpcrypt.org//%{name}-%{version}.tar.gz
SOURCE1: tmpfiles-tcpcrypt.conf
SOURCE2: tcpcryptd.service
SOURCE3: tcpcryptd-firewall
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
BuildRequires: make
BuildRequires:  gcc
BuildRequires: openssl-devel libnetfilter_queue-devel libcap-devel
BuildRequires: libnetfilter_conntrack-devel libpcap-devel
BuildRequires: libtool autoconf automake
BuildRequires: systemd
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
Provides a protocol that attempts to encrypt (almost) all of your
network traffic. Unlike other security mechanisms, Tcpcrypt works out
of the box: it requires no configuration, no changes to applications,
and your network connections will continue to work even if the remote
end does not support

%package devel
Summary: Development package that includes the tcpcrypt header files
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The devel package contains the tcpcrypt library and the include files

%package libs
Summary: Libraries used by tcpcryptd server and tcpcrypt-aware applications

%description libs
Contains libraries used by tcpcryptd server and tcpcrypt-aware applications

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

# Create a sysusers.d config file
cat >tcpcrypt.sysusers.conf <<EOF
u tcpcryptd - 'tcpcrypt daemon account' /var/run/tcpcryptd -
EOF

%build
sh bootstrap.sh
%configure --disable-static --disable-rpath
%make_build

%install
%make_install
install -m 0755 %{SOURCE3} %{buildroot}/%{_bindir}
rm %{buildroot}%{_libdir}/*.la
mkdir -p %{buildroot}%{_sysconfdir}/tmpfiles.d/ %{buildroot}/run/tcpcryptd
install -D -m 0644 %{SOURCE1} %{buildroot}%{_tmpfilesdir}/tcpcrypt.conf
mkdir -p %{buildroot}%{_unitdir}
install -m 0755 %{SOURCE2} %{buildroot}/%{_unitdir}/tcpcryptd.service

install -m0644 -D tcpcrypt.sysusers.conf %{buildroot}%{_sysusersdir}/tcpcrypt.conf

%files libs
%doc README.markdown
%license LICENSE
%{_libdir}/libtcpcrypt.so.*

%files
%doc README.markdown
%license LICENSE
%{_bindir}/tcnetstat
%{_bindir}/tcpcryptd
%{_bindir}/tcpcryptd-firewall
%{_bindir}/tcs
%{_mandir}/man8/*
%attr(0644,root,root) %{_tmpfilesdir}/tcpcrypt.conf
%attr(0644,root,root) %{_unitdir}/tcpcryptd.service
%attr(0755,tcpcryptd,tcpcryptd) %dir /run/tcpcryptd
%{_sysusersdir}/tcpcrypt.conf

%files devel
%{_libdir}/libtcpcrypt.so
%dir %{_includedir}/tcpcrypt
%{_includedir}/tcpcrypt/*.h

%ldconfig_scriptlets libs

%post
%systemd_post tcpcryptd.service

%preun
%systemd_preun tcpcryptd.service

%postun
%systemd_postun_with_restart tcpcryptd.service

%changelog
%autochangelog
