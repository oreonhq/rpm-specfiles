%global source0_hash 6b51f3efd6b8500c92f3c5d25e158f813d3be078c31c9b480c7ea791b6725e5e

%undefine __cmake_in_source_build
# https://github.com/georgmartius/vid.stab/commit/05829db776069b7478dd2d90b6e0081668a41abc
%global commit 05829db776069b7478dd2d90b6e0081668a41abc
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20230603

Name:           vid.stab
Version:        1.1.1
Release:        %autorelease
Summary:        Video stabilize library for fmpeg, mlt or transcode
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://public.hronopik.de/vid.stab
Source0:        https://github.com/georgmartius/vid.stab/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  orc-devel
Requires:       glibc
Provides:	%{name}-libs = %{version}-%{release}
Obsoletes:	%{name}-libs < %{version}-%{release}

%description
Vidstab is a video stabilization library which can be plugged-in with Ffmpeg
and Transcode.

%package devel
Summary:        Development files for vid.stab
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the development files (library and header files).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{name}-%{commit}
# remove SSE2 flags
sed -i 's|-DUSE_SSE2 -msse2||' tests/CMakeLists.txt
# fxi warning _FORTIFY_SOURCE requires compiling with optimization (-O)
sed -i 's|-Wall -O0|-Wall -O|' tests/CMakeLists.txt
# use macros EXIT_SUCCESS and EXIT_FAILURE instead for portability reasons.
sed -i 's|return units_failed==0;|return units_failed>0;|' tests/testframework.c

%build
# TODO: Please submit an issue to upstream (rhbz#2381628)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake
%cmake_build

# build the tests program
pushd tests
%cmake
%cmake_build
popd

%install
%cmake_install

%check
LD_LIBRARY_PATH=%{buildroot}%{_libdir} tests/tests || :

%ldconfig_scriptlets -n %{name}

%files
%doc README.md
%license LICENSE
%{_libdir}/libvidstab.so.*

%files devel
%{_includedir}/vid.stab/
%{_libdir}/libvidstab.so
%{_libdir}/pkgconfig/vidstab.pc

%changelog
%autochangelog
