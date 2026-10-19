%global source0_hash 0fe55b672cbeaa4dc047b7658f0a5d6aae0d94a5ee25727d25df43f148fc8709
%global debug_package   %{nil}
Name:           PEGTL
Version:        4.0.2
Release:        1%{?dist}
Summary:        Parsing Expression Grammar Template Library
License:        BSL-1.0
URL:            https://github.com/taocpp/%{name}
Source0:        https://github.com/taocpp/PEGTL/archive/refs/tags/4.0.2.tar.gz#/PEGTL-2.8.3.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
# /oreon:deps
%description
The Parsing Expression Grammar Template Library (PEGTL) is a zero-dependency
C++11 header-only library for creating parsers according to a Parsing
Expression Grammar (PEG).

%package devel
Summary:        Development files for %{name}
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name} = %{version}-%{release}
Requires:       libstdc++-devel
%description devel
The %{name}-devel package contains C++ header files for developing
applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake \
    -DPEGTL_INSTALL_INCLUDE_DIR:PATH='%{_includedir}' \
    -DPEGTL_INSTALL_DOC_DIR:PATH='%{_pkgdocdir}' \
    -DPEGTL_INSTALL_CMAKE_DIR:PATH='%{_datadir}/cmake/pegtl' \
    -GNinja
%cmake_build
%install
%cmake_install
rm -rv %{buildroot}%{_pkgdocdir}
%oreon_autofiles PEGTL-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n PEGTL-devel -f %{oreon_filedir}/PEGTL-devel.list

%changelog

%autochangelog
