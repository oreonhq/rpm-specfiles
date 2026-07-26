%global source0_hash 314b4793e0902fbf1fdb7fb659af37a3c1306ed1aad5d1c84de6c931b351d359

Summary:        Implementation of an E-component of Network Intrusion Detection System
Name:           libnids
Version:        1.24
Release:        35%{?dist}
License:        GPL-2.0-or-later
URL:            https://libnids.sourceforge.net/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz.asc
Source2:        gpgkey-67E00C8AE6DEE3486468F6C6E20D29536F5C037F.gpg
Patch0:         libnids-1.24-inline.patch
Patch1:         libnids-configure-c99.patch
BuildRequires:  gnupg2
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  libnet-devel
BuildRequires:  glib2-devel
BuildRequires:  libpcap-devel
BuildRequires:  pkgconfig

%description
Libnids is an implementation of an E-component of Network Intrusion
Detection System. It emulates the IP stack of Linux 2.x and offers
IP defragmentation, TCP stream assembly and TCP port scan detection.

Using libnids, one has got a convenient access to data carried by a
TCP stream, no matter how artfully obscured by an attacker.

%package devel
Summary:        Development files for libnids
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package package includes header files and libraries necessary
for developing programs which use the libnids library. It contains
the API documentation of the library, too.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%if 0%{?fedora} > 41 || 0%{?rhel} > 10
export CFLAGS="$CFLAGS -std=gnu17"
%endif

%configure --enable-shared
%make_build

%install
%make_install install_prefix=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/libnids.a

%ldconfig_scriptlets

%files
%license COPYING
%doc CHANGES CREDITS MISC README
%{_libdir}/libnids.so.*

%files devel
%doc doc/* samples/
%{_libdir}/libnids.so
%{_includedir}/nids.h
%{_mandir}/man3/libnids.3*

%changelog
%autochangelog
