%global source0_hash b18f4b04f3171d245bb915d59bf0f9268160579f7ff1cc7454e045ee8943f8a3

%global _hardened_build	1

# version revision
%global revision	11259

Name:		yadifa
Version:	2.6.7
Release:	5%{?dist}
Summary:	Lightweight authoritative Name Server with DNSSEC capabilities

License:	BSD-3-Clause
URL:		http://www.yadifa.eu
Source0:	http://cdn.yadifa.eu/sites/default/files/releases/%{name}-%{version}-%{revision}.tar.gz
Source1:	yadifad.service
Source3:	yadifa.logrotate

BuildRequires:	gcc
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	openssl-devel
BuildRequires:	openssl-devel-engine
BuildRequires:	sed

Requires:	logrotate
Requires:	yadifa-libs = %{version}-%{release}

Requires(post):		systemd
Requires(preun):	systemd
Requires(postun):	systemd
BuildRequires:		systemd

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

# adjust build options
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

# adjust additional key options
sed -i 's|^include "keys.conf"|#include "keys.conf"|' etc/yadifad.conf.example
sed -i '/^<\/key>/a \ \n<key>\n \ name \ abroad-admin-key\n \ algorithm \ hmac-md5\n \ secret \ AbroadAdminTSIGKey==\n<\/key>' \
    etc/yadifad.conf.example

%make_build

%install
%make_install

# config
for conf in yadifad yakeyrolld; do
install -Dpm 0644 etc/${conf}.conf \
    %{buildroot}%{_sysconfdir}/${conf}.conf
done

mkdir -p %{buildroot}%{_localstatedir}/log/yadifa
mkdir -p %{buildroot}%{_localstatedir}/log/yakeyrolld
rm -f %{buildroot}%{_libdir}/*.la
rm -rf %{buildroot}%{_defaultdocdir}/yadifa

# bash completion
for comp in yadifa yadifad; do
install -Dpm 0644 etc/${comp}.bash_completion \
    %{buildroot}%{_datadir}/bash-completion/completions/${comp}
done

install -Dpm 0644 %{SOURCE1} %{buildroot}%{_unitdir}/yadifad.service

install -Dpm 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/logrotate.d/yadifa

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

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%doc etc/*.conf.example
%config(noreplace) %{_sysconfdir}/yadifad.conf
%config(noreplace) %{_sysconfdir}/yakeyrolld.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/yadifa
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/yadifad
%{_unitdir}/yadifad.service
%{_localstatedir}/zones
%{_localstatedir}/log/yadifa
%{_localstatedir}/log/yakeyrolld
%{_sbindir}/yadifad
%{_sbindir}/yakeyrolld
%{_mandir}/man5/yadifa.*.5*
%{_mandir}/man5/yadifad.*.5*
%{_mandir}/man8/yadifad.8*
%{_mandir}/man5/yakeyrolld.*.5*
%{_mandir}/man8/yakeyrolld.8*

%files libs
%{_libdir}/libdnscore.so.7*
%{_libdir}/libdnsdb.so.7*
%{_libdir}/libdnslg.so.7*

%files tools
%license COPYING
%doc AUTHORS
%{_bindir}/yadifa
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/yadifa
%{_mandir}/man8/yadifa.8*

%files devel
%{_includedir}/dnscore
%{_includedir}/dnsdb
%{_includedir}/dnslg
%{_libdir}/libdnscore.so
%{_libdir}/libdnsdb.so
%{_libdir}/libdnslg.so

%changelog
%autochangelog
