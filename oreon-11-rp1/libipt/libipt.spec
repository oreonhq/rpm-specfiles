%global source0_hash f09a18fefba81d4fc2530d90858789e0c596f1b634e5777e6ccaf492966e9845
%global __cmake_in_source_build 1
Name: libipt
Version: 2.2
Release:        1%{?dist}
Summary:        Intel Processor Trace Decoder Library
License: BSD-3-Clause
URL: https://github.com/intel/libipt
Source0:        https://github.com/intel/libipt/archive/v%{version}.tar.gz#/libipt-%{version}.tar.gz
Patch1:        libipt-cmake40-compat.patch
ExclusiveArch: %{ix86} x86_64
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pandoc
# /oreon:deps
%description
The Intel Processor Trace (Intel PT) Decoder Library is Intel's reference
implementation for decoding Intel PT.  It can be used as a standalone library
or it can be partially or fully integrated into your tool.

%ldconfig_scriptlets 

%package devel
Summary: Header files and libraries for Intel Processor Trace Decoder Library
Requires: %{name}%{?_isa} = %{version}-%{release}
ExclusiveArch: %{ix86} x86_64
%description devel
The %{name}-devel package contains the header files and libraries needed to
develop programs that use the Intel Processor Trace (Intel PT) Decoder Library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n libipt-%{version}
%patch -P 1 -p1

%build

%cmake -DCMAKE_POLICY_VERSION_MINIMUM=3.5 -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DPTUNIT:BOOL=ON \
       -DMAN:BOOL=ON \
       -DDEVBUILD:BOOL=ON \
       .
%cmake_build
%install
%cmake_install
%global develdocs howto_libipt.md
(cd doc;cp -p %{develdocs} ..)
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

ctest -V %{?_smp_mflags}
%files -f %{oreon_filedir}/main.list
%files -n libipt-devel -f %{oreon_filedir}/libipt-devel.list

%changelog

%autochangelog
