%global source0_hash f035ca0e1b5d37b78e358f07a25b05c5cdaf2c85c4b31cf29f6be17f288a349e
Name:          ccrtp
Summary:        Common C++ class framework for RTP/RTCP
Version:       2.1.2
Release:        19%{?dist}
License:       GPL-2.0-or-later AND GPL-2.0-or-later WITH mif-exception
URL:           http://www.gnu.org/software/commoncpp/
Source0:        http://ftp.gnu.org/pub/gnu/ccrtp/ccrtp-%{version}.tar.gz
# oreon:deps
BuildRequires:  commoncpp2-devel
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libgcrypt-devel
BuildRequires:  make
BuildRequires:  ucommon-devel
# /oreon:deps
%description
ccRTP is a generic, extensible and efficient C++ framework for
developing applications based on the Real-Time Transport Protocol
(RTP) from the IETF. It is based on Common C++ and provides a full
RTP/RTCP stack for sending and receiving of realtime data by the use
of send and receive packet queues. ccRTP supports unicast,
multi-unicast and multicast, manages multiple sources, handles RTCP
automatically, supports different threading models and is generic as
for underlying network and transport protocols.

%package devel
Summary: Header files and libraries for %{name} development
License: GPL-2.0-or-later AND GPL-2.0-or-later WITH mif-exception AND LGPL-2.0-or-later AND LGPL-2.1-or-later
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig, commoncpp2-devel
%description devel
The %{name}-devel package contains the header files and libraries needed
to develop programs that use the %{name} library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
chmod 644 src/ccrtp/rtp.h

%build

%configure --disable-static
%make_build
%install
%make_install
rm -f %{buildroot}%{_infodir}/dir
find %{buildroot} -name '*.la' -exec rm -f {} \;
%oreon_autofiles ccrtp-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n ccrtp-devel -f %{oreon_filedir}/ccrtp-devel.list

%changelog

%autochangelog
