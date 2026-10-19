%global source0_hash fbd712903d61306ad00d5fa5029a9882630c7311ca487f48d2d76000956e8ff9
Name:		CharLS
Version:	2.4.4
Release:        1%{?dist}
Summary:        An optimized implementation of the JPEG-LS standard
License:	BSD-3-Clause
URL:		https://github.com/team-charls/charls
VCS:		git:%{url}.git
Source0:        https://github.com/team-charls/charls/archive/%{version}/%{name}-%{version}.tar.gz
Provides:       charls
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
# /oreon:deps
%description
An optimized implementation of the JPEG-LS standard for loss less and
near loss less image compression. JPEG-LS is a low-complexity standard that
matches JPEG 2000 compression ratios. In terms of speed, CharLS outperforms
open source and commercial JPEG LS implementations.

JPEG-LS (ISO-14495-1/ITU-T.87) is a standard derived from the Hewlett Packard
LOCO algorithm. JPEG LS has low complexity (meaning fast compression) and high
compression ratios, similar to JPEG 2000. JPEG-LS is more similar to the old
loss less JPEG than to JPEG 2000, but interestingly the two different techniques
result in vastly different performance characteristics.

%package devel
Summary:	Libraries and headers for CharLS
Requires:	%{name}%{?_isa} = %{version}-%{release}
Provides:       charls-devel
%description devel
CharLS Library Header Files and Link Libraries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir charls-%{version}
%oreon_prep
%build

%cmake -DBUILD_SHARED_LIBS:BOOL=ON \
	-DCMAKE_BUILD_TYPE:STRING="Release" \
	-DBUILD_TESTING=ON
%cmake_build
%install
%cmake_install
%oreon_autofiles CharLS-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n CharLS-devel -f %{oreon_filedir}/CharLS-devel.list

%changelog

%autochangelog
