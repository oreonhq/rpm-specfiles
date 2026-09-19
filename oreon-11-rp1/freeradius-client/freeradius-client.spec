%global source0_hash eada2861b8f4928e3ac6b5bbfe11e92cd6cdcacfce40cae1085e77c1b6add0e9

Summary: RADIUS protocol client library
Name: freeradius-client
Version: 1.1.7
Release: 37%{?dist}
# For a breakdown of the licensing, see PACKAGE-LICENSING 
# Automatically converted from old format: BSD and MIT - review is highly recommended.
License: LicenseRef-Callaway-BSD AND LicenseRef-Callaway-MIT
URL: http://freeradius.org/freeradius-client/
Source0: ftp://ftp.freeradius.org/pub/freeradius/%{name}-%{version}.tar.gz
Source1: radiusclient.conf
Source2: PACKAGE-LICENSING
Source3: dictionary
Patch1: freeradius-client-1.1.7-size_t.patch
Patch2: freeradius-client-1.1.7-ipv6-attr-fix.patch
Patch3: freeradius-client-1.1.7-autoconf-c99.patch

BuildRequires: gcc
BuildRequires: make automake autoconf libtool
BuildRequires: nettle-devel >= 2.7.1
BuildRequires: libxcrypt-devel

%description
FreeRADIUS Client is a library for writing RADIUS Clients.
The library lets you develop a RADIUS-aware application in less than
50 lines of C code. 

%package devel
Summary: Development files for freeradius-client
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for freeradius-client.

%package utils
Summary: Utility programs for freeradius-client
Requires: %{name}%{?_isa} = %{version}-%{release}
# freeradius-client supersedes radiusclient-ng
Obsoletes: radiusclient-ng-utils

%description utils
FreeRADIUS Client is a framework and library for writing RADIUS Clients.
This package includes radius client test utilities such as,
radiusclient, radexample, radstatus, radembedded and radacct.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
rm -f lib/md5.c
sed -i -e 's|sys_lib_dlsearch_path_spec="[^"]\+|& %{_libdir}|g' configure

%patch -P1 -p1 -b .size_t
%patch -P2 -p1 -b .attr
%patch -P3 -p1 -b .autoconf-c99

%build

autoreconf -vi
%configure --disable-static --disable-rpath --with-nettle
make %{?_smp_mflags}

%install
cp -a %{SOURCE2} PACKAGE-LICENSING
make DESTDIR=%{buildroot} install
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_sbindir}/login.radius

mkdir -p %{buildroot}%{_datadir}/radiusclient
mv %{buildroot}%{_sysconfdir}/radiusclient/dictionary.* %{buildroot}%{_datadir}/radiusclient/
cp %{SOURCE1} %{buildroot}%{_sysconfdir}/radiusclient/
cp %{SOURCE3} %{buildroot}%{_sysconfdir}/radiusclient/
cp %{SOURCE3} %{buildroot}%{_datadir}/radiusclient/dictionary

%ldconfig_scriptlets

%files
%doc README.rst README.radexample BUGS doc/ChangeLog
%license COPYRIGHT PACKAGE-LICENSING

%dir %{_sysconfdir}/radiusclient
%config(noreplace) %{_sysconfdir}/radiusclient/issue
%config(noreplace) %{_sysconfdir}/radiusclient/port-id-map
%config(noreplace) %{_sysconfdir}/radiusclient/radiusclient.conf
%config(noreplace) %{_sysconfdir}/radiusclient/servers
%config(noreplace) %{_sysconfdir}/radiusclient/dictionary

%{_libdir}/libfreeradius-client.so.*

%dir %{_datadir}/radiusclient/
%{_datadir}/radiusclient/dictionary.ascend
%{_datadir}/radiusclient/dictionary.compat
%{_datadir}/radiusclient/dictionary.merit
%{_datadir}/radiusclient/dictionary.sip
%{_datadir}/radiusclient/dictionary

%files devel

%{_includedir}/freeradius-client.h
%{_libdir}/libfreeradius-client.so

%files utils

%{_sbindir}/radacct
%{_sbindir}/radiusclient
%{_sbindir}/radstatus
%{_sbindir}/radlogin
%{_sbindir}/radexample
%{_sbindir}/radembedded

%changelog
%autochangelog
