%global source0_hash 5ead2276b42a534ac40437ce53b2231320b985539dc325453d93874be8d92869
%bcond_with tests
%global toolchain clang
Name:           libobjc2
Version:        2.3
Release:        1%{?dist}
Summary:        GNUstep Objective-C runtime library
License:        GPL-2.0-only
URL:            https://github.com/gnustep/libobjc2
Source0:        https://github.com/gnustep/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         %{url}/commit/365e53632e8be41e49f21ee47a63e41be424a237.patch
ExcludeArch:    armv7hl i686 ppc64le s390x
# oreon:deps
BuildRequires:  clang
BuildRequires:  cmake
BuildRequires:  libdispatch-devel
BuildRequires:  robin-map-devel
BuildRequires:  sed
# /oreon:deps
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
mv %{buildroot}%{_includedir}/Block.h %{buildroot}%{_includedir}/Block-libobjc.h
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with tests}
%check

%ctest
%endif
%files -f %{oreon_filedir}/main.list
%files -n libobjc2-devel -f %{oreon_filedir}/libobjc2-devel.list

%changelog

%autochangelog
