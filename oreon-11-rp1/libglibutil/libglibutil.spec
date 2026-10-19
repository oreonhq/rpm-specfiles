%global source0_hash f05586a0b5496ecf763a268a9f78ee71096b222aada0e78013befda5e999db63
Name: libglibutil
Version: 1.0.82
Release:        1%{?dist}
Summary:        Library of glib utilities
License: BSD
URL: https://github.com/sailfishos/libglibutil
Source0:        https://github.com/sailfishos/%{name}/archive/refs/tags/%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0)
# /oreon:deps
%description
Provides glib utility functions and macros

%package devel
Summary: Development library for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig
%description devel
This package contains the development library for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%make_build LIBDIR=%{_libdir} KEEP_SYMBOLS=1 release pkgconfig
%install
%{make_build} LIBDIR=%{_libdir} DESTDIR=%{buildroot} install-dev
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%{make_build} -C test test
%files -f %{oreon_filedir}/main.list
%files -n libglibutil-devel -f %{oreon_filedir}/libglibutil-devel.list

%changelog

%autochangelog
