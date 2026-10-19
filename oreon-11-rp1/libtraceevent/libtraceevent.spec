%global source0_hash e6d82cb2392d04866203387fa092692e4282ccc36c8235dc129afd1ceba12684
Name: libtraceevent
Version: 1.9.0
Release:        1%{?dist}
License: LGPL-2.1-only AND LGPL-2.1-or-later AND GPL-2.0-only AND GPL-2.0-or-later
Summary:        Library to parse raw trace event formats
URL: https://git.kernel.org/pub/scm/libs/libtrace/libtraceevent.git/
Source0:        https://git.kernel.org/pub/scm/libs/libtrace/libtraceevent.git/snapshot/libtraceevent-%{version}.tar.gz
%global __provides_exclude_from ^%{_libdir}/traceevent/plugins
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  gcc
BuildRequires:  xmlto
# /oreon:deps
%description
libtraceevent is a library to parse raw trace event formats.

%package devel
Summary: Development headers of %{name}
Requires: %{name}%{_isa} = %{version}-%{release}
%description devel
Development headers of %{name}-libs

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build

MANPAGE_DOCBOOK_XSL=`rpm -ql docbook-style-xsl | grep manpages/docbook.xsl`
make -O -j1 V=1 VERBOSE=1 CFLAGS="%{build_cflags}" LDFLAGS="%{build_ldflags}" prefix=%{_prefix} libdir=%{_libdir} MANPAGE_XSL=%{MANPAGE_DOCBOOK_XSL} all doc
%install
%make_install prefix=%{_prefix} libdir=%{_libdir} install doc-install
rm -rf %{buildroot}/%{_libdir}/libtraceevent.a
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libtraceevent-devel -f %{oreon_filedir}/libtraceevent-devel.list

%changelog

%autochangelog
