%global source0_hash 05a704e3c8f7792a17315080a21214a4448fd2452c1b0dd5226a3a55f90b58c3
Name: aircrack-ng
Version: 1.7
Release:        1%{?dist}
Summary:        Tools for auditing 802.11 (wireless) networks
License: GPL-2.0-or-later
URL: https://github.com/%{name}/%{name}
Source0:        https://github.com/%{name}/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Requires: util-linux%{?_isa}
Recommends: %{name}-doc
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  ethtool
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  hwloc-devel
BuildRequires:  libcmocka-devel
BuildRequires:  libnl3-devel
BuildRequires:  libpcap-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  pcre-devel
BuildRequires:  pkgconfig
BuildRequires:  sqlite-devel
BuildRequires:  util-linux
BuildRequires:  zlib-devel
# /oreon:deps
%description
aircrack-ng is a set of tools for auditing wireless networks. It's an
enhanced/reborn version of aircrack. It consists of airodump-ng (an 802.11
packet capture program), aireplay-ng (an 802.11 packet injection program),
aircrack (static WEP and WPA-PSK cracking), airdecap-ng (decrypts WEP/WPA
capture files), and some tools to handle capture files (merge, convert, etc.).

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description devel
%{summary}.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
BuildArch: noarch
%description doc
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
find . -type f -name "*.py" -exec sed -e 's@/usr/bin/env python@%{__python3}@g' -e 's@python2@python3@g' -i "{}" \;

%build

autoreconf -fiv
%configure \
    --with-experimental \
    --with-lto \
    --with-avx512 \
    --without-opt \
    --disable-static
%make_build
%install
%make_install
install -d -m 0755 %{buildroot}%{_datadir}/%{name}
find %{buildroot} -type f -name '*.la' -delete
%oreon_autofiles aircrack-ng-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles aircrack-ng-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n aircrack-ng-devel -f %{oreon_filedir}/aircrack-ng-devel.list
%files -n aircrack-ng-doc -f %{oreon_filedir}/aircrack-ng-doc.list

%changelog

%autochangelog
