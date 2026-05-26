%global debug_package   %{nil}

Name:           PEGTL
Version:        2.8.3
Release:        15%{?dist}
Summary:        Parsing Expression Grammar Template Library
License:        MIT
URL:            https://github.com/taocpp/%{name}
Source:        https://github.com/taocpp/PEGTL/archive/2.8.3/PEGTL-2.8.3.tar.gz

Patch:          PEGTL-compiler-warning.patch
# oreon url source checksums begin
%global source0_sha256 88b8e4ded6ea1f3f2223cc3e37072e2db1e123b90d36c309816341ae9d966723
%global source0_file PEGTL-2.8.3.tar.gz
# oreon url source checksums end

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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/PEGTL-2.8.3.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "88b8e4ded6ea1f3f2223cc3e37072e2db1e123b90d36c309816341ae9d966723" || { echo "oreon: Source0 SHA256 mismatch for PEGTL-2.8.3.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
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
