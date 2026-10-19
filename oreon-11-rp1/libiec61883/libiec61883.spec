%global source0_hash 594dbdd4e391d8a4df740db573681b288eee0366e443e5d465febbefd24a5a32
Summary:        Streaming library for IEEE1394
Name:           libiec61883
Version:        1.2.0
Release:        1%{?dist}
License:        LGPL-2.1-or-later AND GPL-2.0-or-later
Source0:        http://www.kernel.org/pub/linux/libs/ieee1394/%{name}-%{version}.tar.gz
URL:            https://ieee1394.docs.kernel.org/en/latest/#libiec61883
ExcludeArch:    s390 s390x
Patch0:         libiec61883-1.2.0-installtests.patch
Patch1:         libiec61883-channel-allocation-without-local-node-rw.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libraw1394-devel
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
The libiec61883 library provides an higher level API for streaming DV,
MPEG-2 and audio over IEEE1394.  Based on the libraw1394 isochronous
functionality, this library acts as a filter that accepts DV-frames,
MPEG-2 frames or audio samples from the application and breaks these
down to isochronous packets, which are transmitted using libraw1394.

%package devel
Summary:        Development files for libiec61883
Requires:       %{name} = %{version}-%{release}
%description devel
Development files needed to build applications against libiec61883

%package utils
Summary:        Utilities for use with libiec61883
Requires:       %{name} = %{version}-%{release}
%description utils
Utilities that make use of iec61883

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -vif
%configure --disable-static
%make_build
%install
%make_install
find %{buildroot} -name '*.la' -delete
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libiec61883-devel -f %{oreon_filedir}/libiec61883-devel.list
%files -n libiec61883-utils -f %{oreon_filedir}/libiec61883-utils.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.0-1
- Prepare for Oreon 11 (RP1)
