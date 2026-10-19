%global source0_hash 89548cefd5b86d5819278bd5dc6e098a1b7031a28da82c580ca535fedbe94a8c
%global commit0 36a66881fceface8732daf413b68a9e06626b31f
%global date 20250117
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
Name:       c-icap-modules
Version:    0.5.7
Release:        1%{?dist}
Summary:        Services for the c-icap server
License:    LGPL-2.0-or-later
URL:        http://c-icap.sourceforge.net/
Source0:        https://github.com/c-icap/%{name}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
Requires:   c-icap >= %{version}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bzip2-devel
BuildRequires:  c-icap-devel
BuildRequires:  clamav-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libatomic
BuildRequires:  libtool
BuildRequires:  lmdb-devel
BuildRequires:  make
# /oreon:deps
%description
C-icap is an implementation of an ICAP server. It can be used with HTTP proxies
that support the ICAP protocol to implement content adaptation and filtering
services. Most of the commercial HTTP proxies must support the ICAP protocol,
the open source Squid 3.x proxy server supports it too.

Currently the following services have been implemented for the c-icap server:
  - virus_scan, an antivirus ICAP service
  - url_check, an URL blacklist/whitelist icap service
  - srv_content_filtering, a score based content filtering icap service

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n c-icap-modules-%{commit0}

# See RECONF
echo "master-%{shortcommit0}" > VERSION.m4
autoreconf -vif

%build

%configure \
  --disable-static \
  --enable-shared \
  --enable-virus_scan-profiles \
  --with-clamav \
  --with-lmdb
%make_build
%install
mkdir -p %{buildroot}%{_sysconfdir}/c-icap
%make_install
rm -f %{buildroot}%{_libdir}/c_icap/*.la
rm -f %{buildroot}%{_sysconfdir}/c-icap/*.default
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
