%global source0_hash 78fc3711db14bf863040ae98f7bdca08f41623ebeaf7efaea7dd49a38b5f054c

# Tests fail to build with
# LLVM ERROR: Cannot select: intrinsic %%llvm.objc.clang.arc.use
# https://bugs.llvm.org/show_bug.cgi?id=49717
%bcond_with tests

%global toolchain clang

Name:           libobjc2
Version:        2.1
Release:        15%{?dist}
Summary:        GNUstep Objective-C runtime library
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            https://github.com/gnustep/libobjc2
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# Don't use CXXFLAGS when compiling eh_trampoline.cc
Patch0:         %{url}/commit/365e53632e8be41e49f21ee47a63e41be424a237.patch

BuildRequires:  sed
BuildRequires:  cmake
BuildRequires:  clang >= 7.0.1
BuildRequires:  libdispatch-devel >= 1.3
BuildRequires:  robin-map-devel

# libdispatch is not available on these architectures
ExcludeArch:    armv7hl i686 ppc64le s390x

%description
The GNUstep Objective-C runtime is designed as a drop-in replacement for the
GCC runtime. It supports both a legacy and a modern ABI, allowing code compiled
with old versions of GCC to be supported without requiring recompilation.
The modern ABI adds the following features:

* Non-fragile instance variables.
* Protocol uniquing.
* Object planes support.
* Declared property introspection.

Both ABIs support the following feature above and beyond the GCC runtime:

* The modern Objective-C runtime APIs, introduced with OS X 10.5.
* Blocks (closures).
* Low memory profile for platforms where memory usage is more important than
  speed.
* Synthesised property accessors.
* Efficient support for @synchronized()
* Type-dependent dispatch, eliminating stack corruption from mismatched
  selectors.
* Support for the associated reference APIs introduced with Mac OS X 10.6.
* Support for the automatic reference counting APIs introduced with Mac OS X
  10.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains development files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# replace bundled robin-map with the system one
mkdir -p third_party/robin-map/include
ln -s %{_includedir}/tsl third_party/robin-map/include/

# drop flag conflicting with FORTIFY_SOURCE
sed -e 's/-O0//g' -i CMakeLists.txt Test/CMakeLists.txt

%build
%cmake \
%if %{with tests}
%else
  -DTESTS=OFF \
%endif
  -DCMAKE_INSTALL_LIBDIR=%{_lib}

%cmake_build

%install
%cmake_install

# Workaround for https://github.com/gnustep/libobjc2/issues/199
mv %{buildroot}%{_includedir}/Block.h %{buildroot}%{_includedir}/Block-libobjc.h

%if %{with tests}
%check
%ctest
%endif

%files
%license COPYING
%doc README.md ANNOUNCE.%{version}
%{_libdir}/libobjc.so.*

%files devel
%{_includedir}/*.h
%{_includedir}/objc
%{_libdir}/libobjc.so
%{_libdir}/pkgconfig/libobjc.pc

%changelog
%autochangelog
