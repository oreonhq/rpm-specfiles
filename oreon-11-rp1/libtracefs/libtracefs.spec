%global source0_hash a9cd9cbae81b7fff71b3f72d2b819e49cec0402529e5f252e1d9319a62a356cb
Name: libtracefs
Version: 1.8.3
Release:        1%{?dist}
License: LGPL-2.1-or-later AND GPL-2.0-or-later AND GPL-2.0-only
Summary:        Library for access kernel tracefs
URL: https://git.kernel.org/pub/scm/libs/libtrace/libtracefs.git/
Source0:        https://git.kernel.org/pub/scm/libs/libtrace/libtracefs.git/snapshot/libtracefs-%{version}.tar.gz
Conflicts: trace-cmd < 2.9.1-6
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(libtraceevent)
BuildRequires:  xmlto
# /oreon:deps
%description
libtracefs is a library for accessing kernel tracefs

%package devel
Summary: Development headers of %{name}
Requires: %{name}%{_isa} = %{version}-%{release}
%description devel
Development headers of %{name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build

%set_build_flags
make -O -j1 V=1 VERBOSE=1 prefix=%{_prefix} libdir=%{_libdir} all doc
%install
%make_install prefix=%{_prefix} libdir=%{_libdir} install_doc
rm -rf %{buildroot}/%{_libdir}/libtracefs.a
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libtracefs-devel -f %{oreon_filedir}/libtracefs-devel.list

%changelog

%autochangelog
