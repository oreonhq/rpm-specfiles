%global source0_hash a9d46a9c8f40e81f8a6df3ecc2c5a9a8e8da985876299108d92da547c013ba8c
Summary:        Intrusion Detection System
Name: suricata
Version: 8.0.7
Release:        1%{?dist}
License: GPL-2.0-only
URL: https://suricata.io/
Source0:        https://www.openinfosecfoundation.org/download/%{name}-%{version}.tar.gz
Source1: suricata.sysconfig
Source2: fedora.notes
Source3: suricata-tmpfiles.conf
Patch1: suricata-2.0.9-docs.patch
Patch2: suricata-4.1.1-service.patch
Patch3: suricata-5.0.4-geolite-path-fixup.patch
Patch4: suricata-6.0.3-log-path-fixup.patch
Requires: python3-pyyaml
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
ExcludeArch: ppc64le i686
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  file-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  hiredis-devel
BuildRequires:  jansson-devel
BuildRequires:  libcap-ng-devel
BuildRequires:  libevent-devel
BuildRequires:  libmaxminddb-devel
BuildRequires:  libnet-devel
BuildRequires:  libnetfilter_queue-devel
BuildRequires:  libnfnetlink-devel
BuildRequires:  libpcap-devel
BuildRequires:  libtool
BuildRequires:  libyaml-devel
BuildRequires:  lua-devel
BuildRequires:  lz4-devel
BuildRequires:  make
BuildRequires:  nspr-devel
BuildRequires:  nss-devel
BuildRequires:  nss-softokn-devel
BuildRequires:  pcre2-devel
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  python3-devel
BuildRequires:  python3-pyyaml
BuildRequires:  rust
BuildRequires:  systemd-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
The Suricata Engine is an Open Source Next Generation Intrusion
Detection and Prevention Engine. This engine is not intended to
just replace or emulate the existing tools in the industry, but
will bring new ideas and technologies to the field. This new Engine
supports Multi-threading, Automatic Protocol Detection (IP, TCP,
UDP, ICMP, HTTP, TLS, FTP and SMB! ), Gzip Decompression, Fast IP
Matching, and GeoIP identification.

%prep

%setup -q 
install -m 644 %{SOURCE2} doc/
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
sed -i 's/(datadir)/(sysconfdir)/' etc/Makefile.am
%ifarch x86_64
sed -i 's/-D__KERNEL__/-D__KERNEL__ -D__x86_64__/' ebpf/Makefile.am
%endif
find rust/ -name '*.rs' -type f -perm /111 -exec chmod -v -x '{}' '+'
autoreconf -fv --install

%build

export RUSTFLAGS="%build_rustflags"
%configure --enable-gccprotect --enable-pie --disable-gccmarch-native \
        --disable-coccinelle --enable-nfqueue --enable-af-packet \
        --with-libnspr-includes=/usr/include/nspr4 \
        --with-libnss-includes=/usr/include/nss3 \
        --enable-jansson --enable-geoip --enable-lua --enable-hiredis \
        --enable-rust  \
        --enable-python
%make_build
%install
make DESTDIR="%{buildroot}" "bindir=%{_sbindir}" install
mkdir -p %{buildroot}%{_sysconfdir}/%{name}/rules
install -m 640 rules/*.rules %{buildroot}%{_sysconfdir}/%{name}/rules
install -m 600 etc/*.config %{buildroot}%{_sysconfdir}/%{name}
install -m 600 threshold.config %{buildroot}%{_sysconfdir}/%{name}
install -m 600 suricata.yaml %{buildroot}%{_sysconfdir}/%{name}
mkdir -p %{buildroot}%{_unitdir}
install -m 0644 etc/%{name}.service %{buildroot}%{_unitdir}/
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
install -m 0755 %{SOURCE1} %{buildroot}%{_sysconfdir}/sysconfig/%{name}
mkdir -p %{buildroot}/%{_var}/log/%{name}
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
install -m 644 etc/%{name}.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
rm -rf %{buildroot}%{_includedir}
rm -rf %{buildroot}%{_libdir}/pkgconfig
mkdir -p %{buildroot}/%{_var}/lib/%{name}
mkdir -p %{buildroot}%{_tmpfilesdir}
install -m 0644 %{SOURCE3} %{buildroot}%{_tmpfilesdir}/%{name}.conf
mkdir -p %{buildroot}/run
install -d -m 0755 %{buildroot}/run/%{name}/
cp suricata-update/README.rst doc/suricata-update-README.rst
%oreon_autofiles main

%check

make check
%pre

%post

%systemd_post suricata.service
if [ -d %{_var}/log/%{name} ] ; then
	file=$(ls %{_var}/log/%{name}/* 2> /dev/null | wc -l)
	if [ -n "$files" ] && [ "$files" != "0" ] ; then
		chown -R suricata:suricata %{_var}/log/%{name}/ 2> /dev/null || :
	fi
fi
%preun

%systemd_preun suricata.service
%postun

%systemd_postun_with_restart suricata.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
