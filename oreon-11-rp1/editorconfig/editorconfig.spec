%global source0_hash 9d8b420b56a969ea3cf784861c72d26fa0e158fa1494d732df2c8a1480d36a5c
%bcond system_uthash %[0%{?fedora} || 0%{?epel}]
%global _smp_mflags -j1
%global srcname editorconfig-core-c
%global common_description %{expand:
EditorConfig makes it easy to maintain the correct coding style when
switching between different text editors and between different projects.
The EditorConfig project maintains a file format and plugins for various
text editors which allow this file format to be read and used by those
editors.}
Name:           editorconfig
Summary:        Parser for EditorConfig files written in C
Version:        0.12.11
Release:        1%{?dist}
License:        BSD-2-Clause AND BSD-3-Clause AND BSD-1-Clause
URL:            https://github.com/editorconfig/editorconfig-core-c
Source0:        https://github.com/editorconfig/editorconfig-core-c/archive/refs/tags/v0.12.11.tar.gz#/editorconfig-core-c-0.12.11.tar.gz
%if %{with system_uthash}
%endif
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  pcre2-devel
BuildRequires:  uthash-static
# /oreon:deps
%description %common_description

%package        libs
Summary:        Parser library for EditorConfig files (shared library)
Provides:       bundled(inih) = 0^20110627git328c3d4
%if %{without system_uthash}
Provides:       bundled(uthash) = 2.3.0
%endif
%description    libs %common_description

This package contains the shared library.

%package        devel
Summary:        Parser library for EditorConfig files (development files)
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       cmake
%description    devel %common_description

This package contains the files needed for development.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{srcname}-%{version} -p1
%if %{with system_uthash}
# Unbundle uthash
rm -vf src/lib/utarray.h
%endif

%build

%cmake
%cmake_build
%install
%cmake_install
rm %{buildroot}/%{_libdir}/libeditorconfig_static.a
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n editorconfig-libs -f %{oreon_filedir}/editorconfig-libs.list
%files -n editorconfig-devel -f %{oreon_filedir}/editorconfig-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.12.10-1
- Prepare for Oreon 11 (RP1)
