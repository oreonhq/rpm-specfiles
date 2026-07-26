%global source0_hash f1404ca250f02e37a118aa00cf0ec2cbe11896e060c6d369c6761baea7d55a2c

# Stubby has its own package now
%bcond_with stubby
#%%global extraver rc1
%global upstream_version %{version}%{?extraver:-%{extraver}}
%global stubby_version 0.4.2

%undefine __cmake_in_source_build

Summary: Modern asynchronous API to the DNS
Name: getdns
Version: 1.7.3
Release: 10%{?extraver:.%{extraver}}%{?dist}
License: BSD-3-Clause
Url: http://www.getdnsapi.net
Source: http://www.getdnsapi.net/dist/%{name}-%{upstream_version}.tar.gz
Source1: http://www.getdnsapi.net/dist/%{name}-%{upstream_version}.tar.gz.asc
Source2: http://keys.gnupg.net/pks/lookup?op=get&search=0xE5F8F8212F77A498#/willem.nlnetlabs.nl
BuildRequires:  gcc
BuildRequires: libidn2-devel unbound-devel doxygen libevent-devel
BuildRequires: pkgconfig openssl-devel libyaml-devel
BuildRequires: systemd-rpm-macros
BuildRequires: libuv-devel libev-devel check-devel
BuildRequires: cmake
BuildRequires: gnupg2
Requires: unbound-libs

%if %{with stubby}
Source2: stubby.service
%endif

#Patch0:

%description
getdns is a modern asynchronous DNS API. It implements DNS entry points
from a design developed and vetted by application developers, in an API
specification edited by Paul Hoffman. With the development of this API,
we intend to offer application developers a modernized and flexible way
to access DNS security (DNSSEC) and other powerful new DNS features; a
particular hope is to inspire application developers towards innovative
security solutions in their applications.

%package devel
Summary: Development package that includes getdns header files
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The devel package contains the getdns library and the include files and
some example C code.

%package utils
Summary: getdns utilities
Requires: %{name}%{?_isa} = %{version}-%{release}

%description utils
The %{name}-utils package contains utilities using getdns library,
getdns_query and getdns_query_mon utilities. They can be used to analyze
responses from DNS servers over UDP, TCP and TLS, including support for
DNS security.

getdns_query can be used for fetching details of DNS responses in json format.
getdns_query_mon is great for automated monitoring of DNS server replies.

%if %{with stubby}
%package stubby
Summary: DNS Privacy Daemon - Stubby
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: stubby%{?_isa} = stubby-%{stubby_version}

%description stubby 
Stubby is an application that acts as a local DNS Privacy stub resolver (using DNS-over-TLS). Stubby encrypts DNS queries sent from a client machine (desktop or laptop) to a DNS Privacy resolver increasing end user privacy. Stubby is in the early stages of development but is suitable for technical/advanced users. A more generally user-friendly version is on the way!
%end
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{?gpgverify:%gpgverify -k 2 -s 1 -d 0}
%autosetup -p1 -n %{name}-%{upstream_version}

# Create a sysusers.d config file
cat >getdns.sysusers.conf <<EOF
u stubby - 'stubby DNS daemon account' %{_sysconfdir}/stubby -
EOF

%build
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo -DENABLE_STATIC=OFF \
  -DPATH_TRUST_ANCHOR_FILE=%{_sharedstatedir}/unbound/root.key \
%if %{with stubby}
  -DBUILD_STUBBY=ON \
%endif

%cmake_build

%check
# make test needs a network connection - so disabled per default
# make test

%install
%cmake_install

%if %{with stubby}
mkdir -p %{buildroot}%{_unitdir}
install -m 644 %{SOURCE2} %{buildroot}%{_unitdir}/stubby.service
install -d -m 0750 %{buildroot}%{_localstatedir}/cache/stubby
install -d -m 0755 %{buildroot}%{_sysconfdir}/stubby
install -d %__cmake_builddir/stubby/stubby.yml %{buildroot}%{_sysconfdir}/stubby/stubby.yml
rm -rf %{buildroot}%{_docdir}/stubby
%endif

rm -rf %{buildroot}%{_libdir}/*.la
rm -rf %{buildroot}%{_docdir}/%{name}

install -m0644 -D getdns.sysusers.conf %{buildroot}%{_sysusersdir}/getdns.conf

%files
%{_libdir}/libgetdns*so.10*
%doc README.md NEWS AUTHORS ChangeLog
%license LICENSE

%files utils
%{_bindir}/getdns_query
%{_bindir}/getdns_server_mon

%if %{with stubby}
%files stubby
%{_bindir}/stubby
%{_mandir}/*/stubby.1*
%dir %attr(0755,root,root) %{_sysconfdir}/stubby
%config(noreplace) %{_sysconfdir}/stubby/stubby.yml
%attr(0644,root,root) %{_unitdir}/stubby.service
%dir %attr(0750,stubby,stubby) %{_localstatedir}/cache/stubby
%doc stubby/README.md stubby/AUTHORS stubby/NEWS stubby/ChangeLog
%endif
%{_sysusersdir}/getdns.conf

%files devel
%{_libdir}/libgetdns*.so
%{_includedir}/getdns/
%{_libdir}/pkgconfig/*.pc
%{_mandir}/*/*.3*
%doc spec

%post
%{?ldconfig}

%postun
%{?ldconfig}
%end

%if %{with stubby}

%post stubby
%systemd_post stubby.service

%preun stubby
%systemd_preun stubby.service

%postun stubby
%systemd_postun_with_restart stubby.service
%end
%endif

%changelog
%autochangelog
