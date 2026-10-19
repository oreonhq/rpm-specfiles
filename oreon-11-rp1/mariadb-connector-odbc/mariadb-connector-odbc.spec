%global source0_hash 5062f491f7189ba32352a9834777886dfbc64a107bb0e2e50921dd6ae2bd18ad
%bcond debug 0
Name:           mariadb-connector-odbc
Version:        3.2.9
Release:        1%{?dist}
Summary:        The MariaDB Native Client library (ODBC driver)
License:        LGPL-2.1-or-later
Source0:        https://archive.mariadb.org/connector-odbc-%{version}/%{name}-%{version}-src.tar.gz
Url:            https://mariadb.org/en/
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  unixODBC-devel
# /oreon:deps
%description
MariaDB Connector/ODBC is a standardized, LGPL licensed database driver using
the industry standard Open Database Connectivity (ODBC) API. It supports ODBC
Standard 3.5, can be used as a drop-in replacement for MySQL Connector/ODBC,
and it supports both Unicode and ANSI modes.

%package        devel
Summary:        Development files for the %{name}
Requires:       %{name} = %{version}-%{release}
%description    devel
Header files for %{name} that make developing projects with
this connector easier.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{name}-%{version}-src

sed -i -e "s|/usr/include/mariadb|$(pkg-config --variable=includedir libmariadb)|" CMakeLists.txt

%build

%cmake \
       -DCMAKE_BUILD_TYPE="%{?with_debug:Debug}%{!?with_debug:RelWithDebInfo}" \
       -DMARIADB_LINK_DYNAMIC="$(pkg-config --variable=libdir libmariadb)/libmariadb.so" \
       \
       -DINSTALL_LAYOUT=%{!?flatpak:RPM}%{?flatpak:DEFAULT} \
       -DINSTALL_LIBDIR="%{_lib}" \
       -DINSTALL_LIB_SUFFIX="%{_lib}" \
       -DINSTALL_DOCDIR="%{_defaultdocdir}/%{name}" \
       -DINSTALL_LICENSEDIR="%{_defaultlicensedir}/%{name}" \
       \
       -DCMAKE_C_FLAGS_DEBUG="-O0 -g" \
       -DCMAKE_CXX_FLAGS_DEBUG="-O0 -g" \
       \
       -DCMAKE_SKIP_RPATH=YES \
       -DCMAKE_SKIP_INSTALL_RPATH=YES
cmake -B %_vpath_builddir -N -LAH
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n mariadb-connector-odbc-devel -f %{oreon_filedir}/mariadb-connector-odbc-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.2.8-2
- Import
