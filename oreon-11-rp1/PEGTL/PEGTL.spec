# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 88b8e4ded6ea1f3f2223cc3e37072e2db1e123b90d36c309816341ae9d966723
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

%global debug_package   %{nil}

Name:           PEGTL
Version:        2.8.3
Release:        15%{?dist}
Summary:        Parsing Expression Grammar Template Library
License:        MIT
URL:            https://github.com/taocpp/%{name}
Source:        https://github.com/taocpp/PEGTL/archive/2.8.3/PEGTL-2.8.3.tar.gz

Patch:          PEGTL-compiler-warning.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
# Faster than make, with no disadvantages
BuildRequires:  ninja-build

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
%oreon_verify_sources
%autosetup -p1

%build
# Default cmake path is /usr/share/pegtl/cmake. This is OK, but we prefer
# /usr/share/cmake/pegtl to reduce clutter in /usr/share.
%cmake \
    -DPEGTL_INSTALL_INCLUDE_DIR:PATH='%{_includedir}' \
    -DPEGTL_INSTALL_DOC_DIR:PATH='%{_pkgdocdir}' \
    -DPEGTL_INSTALL_CMAKE_DIR:PATH='%{_datadir}/cmake/pegtl' \
    -GNinja
%cmake_build

%install
%cmake_install
# The default installation of documentation is useless: it just installs the
# LICENSE file where we do not want it. Remove its handiwork and deal with
# documentation manually.
rm -rv %{buildroot}%{_pkgdocdir}

%check
%ctest

%files devel
%doc README.md doc/
%license LICENSE
%{_includedir}/tao/pegtl.hpp
%{_includedir}/tao/pegtl/
%{_datadir}/cmake/pegtl/

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.8.3-15
- Prepare for Oreon 11 (RP1)
