%global source0_hash 713d3e76b6c3073b122a9f5b6c025bc301a0436582f132caf782814363acf60f
%global source1_hash 44f1ae8e7073800a2c3a125a60a4b4d51584b23f6ab22a80dbdda4c4aba85c82

# rmpbuild parameters:
# --with docs: Build pre-generated documentation.

%global __cmake_in_source_build 1

Name: libipt
Version: 2.1.2
Release: 4%{?dist}
Summary: Intel Processor Trace Decoder Library
License: BSD-3-Clause
URL: https://github.com/intel/libipt
Source0:        https://github.com/intel/libipt/archive/v%{version}.tar.gz
Source1: doc-v%{version}.tar.xz
Patch1: libipt-cmake40-compat.patch
# c++ is required only for -DPTUNIT test "ptunit-cpp".
BuildRequires: gcc-c++ cmake
%if 0%{?_with_docs:1}
# pandoc is for -DMAN.
BuildRequires: pandoc
%endif
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
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%setup -q -n libipt-%{version}
%patch -P 1 -p1

%build
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DPTUNIT:BOOL=ON \
%if 0%{?_with_docs:1}
       -DMAN:BOOL=ON \
%endif
       -DDEVBUILD:BOOL=ON \
       .
%cmake_build

%install
%cmake_install
%global develdocs howto_libipt.md
(cd doc;cp -p %{develdocs} ..)

# If not building documentation, copy the pre-generated man pages
# to the appropriate place. Otherwise, tar up the generated
# documentation for use in subsequent builds.
%if 0%{?_with_docs:1}
(cd $RPM_BUILD_ROOT%{_mandir}/..; %__tar cJf %{SOURCE1} .)
%else
mkdir -p $RPM_BUILD_ROOT%{_mandir}
(cd $RPM_BUILD_ROOT%{_mandir}/..; %__tar xJf %{SOURCE1})
%endif

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
