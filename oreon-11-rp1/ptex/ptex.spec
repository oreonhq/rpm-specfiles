%global source0_hash 435c116ea5bbe6f0054f8227e204d255b2d91bf35786b007c77a894c729c1fbc
Name:           ptex
Version:        2.5.4
Release:        1%{?dist}
Summary:        Per-Face Texture Mapping for Production Rendering
License:        BSD-3-Clause
Url:            https://github.com/wdas/%{name}
Source0:        https://github.com/wdas/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  graphviz-devel
BuildRequires:  help2man
BuildRequires:  make
BuildRequires:  pkgconfig(libdeflate)
# /oreon:deps
%description
Ptex is a texture mapping system developed by 
Walt Disney Animation Studios for production-quality rendering.

%package devel
Summary: Development files for the Ptex library
Requires:       %{name} = %{version}
%description devel
Development files for Walt Disney Animation Studios Ptex library.

%package doc
Summary: Documentation files for the Ptex library
BuildArch:      noarch
%description doc
Documentation files for Walt Disney Animation Studios Ptex library.

%package libs
Summary:        Libraries for Ptex
%description libs
This package contains the library needed to run programs dynamically
linked with Ptex.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
echo %{version} > version
%cmake \
        -DCMAKE_CXX_STANDARD=17 \
        -DPTEX_BUILD_STATIC_LIBS=OFF 
%cmake_build
%install
%cmake_install
mv %{buildroot}%{_datadir}/pkgconfig %{buildroot}%{_libdir}
install -d '%{buildroot}%{_mandir}/man1'
for cmd in %{buildroot}%{_bindir}/*
do
  LD_LIBRARY_PATH='%{buildroot}%{_libdir}' \
      help2man \
      --no-info --no-discard-stderr --version-string='%{version}' \
      --output="%{buildroot}%{_mandir}/man1/$(basename "${cmd}").1" \
      "${cmd}"
done
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ifarch s390x
%ctest -- -R "halftest"
%else
%ctest
%endif
%files -f %{oreon_filedir}/main.list
%files -n ptex-devel -f %{oreon_filedir}/ptex-devel.list
%files -n ptex-doc -f %{oreon_filedir}/ptex-doc.list
%files -n ptex-libs -f %{oreon_filedir}/ptex-libs.list

%changelog

%autochangelog
