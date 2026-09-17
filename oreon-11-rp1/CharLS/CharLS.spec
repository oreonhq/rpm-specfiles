%global source0_hash bbf67d51446a98eb8fc98c9c6de49a2605c709d3a14ba39f09a09f8e57527099

Name:		CharLS
Version:	2.4.3
Release:	%autorelease
Summary:	An optimized implementation of the JPEG-LS standard
License:	BSD-3-Clause
URL:		https://github.com/team-charls/charls
VCS:		git:%{url}.git
Source0:	%{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	gcc
BuildRequires:	gcc-c++
Provides:       charls

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

%autosetup -n charls-%{version}

%build
%cmake -DBUILD_SHARED_LIBS:BOOL=ON \
	-DCMAKE_BUILD_TYPE:STRING="Release" \
	-DBUILD_TESTING=ON
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE.md
%doc CHANGELOG.md README.md SECURITY.md
%{_libdir}/libcharls.so.2*

%files devel
%{_includedir}/charls/
%{_libdir}/cmake/charls/
%{_libdir}/libcharls.so
%{_libdir}/pkgconfig/charls.pc

%changelog
%autochangelog
