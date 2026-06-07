%global source0_hash 713d3e76b6c3073b122a9f5b6c025bc301a0436582f132caf782814363acf60f

%global __cmake_in_source_build 1

Name: libipt
Version: 2.1.2
Release: 4%{?dist}
Summary: Intel Processor Trace Decoder Library
License: BSD-3-Clause
URL: https://github.com/intel/libipt
Source0:        https://github.com/intel/libipt/archive/v%{version}.tar.gz#/libipt-2.1.2.tar.gz
Patch1:        libipt-cmake40-compat.patch
BuildRequires: gcc-c++ cmake pandoc
BuildRequires: make
ExclusiveArch: %{ix86} x86_64

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

%check
ctest -V %{?_smp_mflags}

%files
%doc README
%license LICENSE
%{_libdir}/%{name}.so.*

%files devel
%doc %{develdocs}
%{_includedir}/*
%{_libdir}/%{name}.so
%{_mandir}/*/*.gz

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.1.2-4
- Import
