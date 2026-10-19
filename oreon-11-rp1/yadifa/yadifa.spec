%global source0_hash b18f4b04f3171d245bb915d59bf0f9268160579f7ff1cc7454e045ee8943f8a3
%global _hardened_build	1
%global revision	11259
Name:		yadifa
Version:	3.0.3
Release:        1%{?dist}
Summary:        Lightweight authoritative Name Server with DNSSEC capabilities
License:	BSD-3-Clause
URL:		http://www.yadifa.eu
Source0:        http://cdn.%{name}.eu/sites/default/files/releases/%{name}-%{version}-%{revision}.tar.gz
Source1:	yadifad.service
Source3:	yadifa.logrotate
Requires:	logrotate
Requires:	yadifa-libs = %{version}-%{release}
Requires(post):		systemd
Requires(preun):	systemd
Requires(postun):	systemd
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  openssl-devel-engine
BuildRequires:  sed
BuildRequires:  systemd
# /oreon:deps
%description
YADIFA is a name server implementation developed from scratch by .eu.
It is portable across multiple operating systems and supports DNSSEC,
TSIG, DNS notify, DNS update, IPv6.

%package libs
Summary:	Libraries used by the YADIFA packages
%description libs
Contains libraries used by YADIFA DNS server

%package tools
Summary:	Remote management client for YADIFA DNS server
%description tools
Contains utility for YADIFA DNS server remote management

%package devel
Summary:	Header files and libraries needed for YADIFA development
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description devel
The yadifa-devel package contains header files and libraries
required for development with YADIFA DNS server

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}-%{revision}

%build

export CPPFLAGS="%{optflags} -DNDEBUG -g"
export LDFLAGS="$LDFLAGS -lssl -lcrypto"
%configure \
    --with-tools \
    --enable-rrl \
    --enable-nsid \
    --enable-ctrl \
    --enable-systemd-resolved-avoidance \
    --enable-shared \
    --disable-static
sed -i 's|-mtune=native||g' \
    {.,bin/yadifa,lib/dnscore,lib/dnsdb,lib/dnslg,sbin/yadifad,sbin/yakeyrolld}/Makefile
sed -i 's|= -fno-ident|=|g' \
    {.,bin/yadifa,lib/dnscore,lib/dnsdb,lib/dnslg,sbin/yadifad,sbin/yakeyrolld}/Makefile
sed -i 's|= -ansi|=|g' \
    {.,bin/yadifa,lib/dnscore,lib/dnsdb,lib/dnslg,sbin/yadifad,sbin/yakeyrolld}/Makefile
sed -i 's|= -pedantic|=|g' \
    {.,bin/yadifa,lib/dnscore,lib/dnsdb,lib/dnslg,sbin/yadifad,sbin/yakeyrolld}/Makefile
sed -i '/^YRCFLAGS = -DNDEBUG $(CCOPTIMISATIONFLAGS) -DCMR/d' \
    {.,bin/yadifa,lib/dnscore,lib/dnsdb,lib/dnslg,sbin/yadifad,sbin/yakeyrolld}/Makefile
sed -i '/^YPCFLAGS = -DNDEBUG $(CCOPTIMISATIONFLAGS) -pg -DCMP/d' \
    {.,bin/yadifa,lib/dnscore,lib/dnsdb,lib/dnslg,sbin/yadifad,sbin/yakeyrolld}/Makefile
sed -i '/^YDCFLAGS = -DDEBUG $(DEBUGFLAGS) -DCMD/d' \
    {.,bin/yadifa,lib/dnscore,lib/dnsdb,lib/dnslg,sbin/yadifad,sbin/yakeyrolld}/Makefile
sed -i 's|^include "keys.conf"|#include "keys.conf"|' etc/yadifad.conf.example
sed -i '/^<\/key>/a \ \n<key>\n \ name \ abroad-admin-key\n \ algorithm \ hmac-md5\n \ secret \ AbroadAdminTSIGKey==\n<\/key>' \
    etc/yadifad.conf.example
%make_build
%install
%make_install
for conf in yadifad yakeyrolld; do
install -Dpm 0644 etc/${conf}.conf \
    %{buildroot}%{_sysconfdir}/${conf}.conf
done
mkdir -p %{buildroot}%{_localstatedir}/log/yadifa
mkdir -p %{buildroot}%{_localstatedir}/log/yakeyrolld
rm -f %{buildroot}%{_libdir}/*.la
rm -rf %{buildroot}%{_defaultdocdir}/yadifa
for comp in yadifa yadifad; do
install -Dpm 0644 etc/${comp}.bash_completion \
    %{buildroot}%{_datadir}/bash-completion/completions/${comp}
done
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_unitdir}/yadifad.service
install -Dpm 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/logrotate.d/yadifa
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%post

%systemd_post yadifad.service
exit 0
%preun

%systemd_preun yadifad.service
exit 0
%postun

%systemd_postun_with_restart yadifad.service
exit 0
%ldconfig_scriptlets libs
%files -f %{oreon_filedir}/main.list
%files -n yadifa-libs -f %{oreon_filedir}/yadifa-libs.list
%files -n yadifa-tools -f %{oreon_filedir}/yadifa-tools.list
%files -n yadifa-devel -f %{oreon_filedir}/yadifa-devel.list

%changelog

%autochangelog
