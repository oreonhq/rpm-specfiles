%global source0_hash ed1517146e6cf66ddedaddd372eb8045e9345a011e68d89a2887af7a87165ebc
Name: libgbinder
Version: 1.1.52
Release:        1%{?dist}
Summary:        Binder client library
License: BSD
URL: https://github.com/mer-hybris/libgbinder
Source0:        https://github.com/mer-hybris/%{name}/archive/refs/tags/%{version}.tar.gz
%global libglibutil_version 1.0.52
Requires: libglibutil >= %{libglibutil_version}
# oreon:deps
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libglibutil)
# /oreon:deps
%description
GLib-style interface to binder (Android IPC mechanism)

Key features:
1. Integration with GLib event loop
2. Detection of 32 vs 64 bit kernel at runtime
3. Asynchronous transactions that don't block the event thread
4. Stable service manager and low-level transaction APIs

Android keeps changing both low-level RPC and service manager
protocols from version to version. To counter that, libgbinder
implements configirable backends for different variants of those,
and yet keeping its own API unchanged.

%package devel
Summary: Development library for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
This package contains the development library for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%{make_build} LIBDIR=%{_libdir} KEEP_SYMBOLS=1 release pkgconfig
%{make_build} -C test/binder-bridge KEEP_SYMBOLS=1 release
%{make_build} -C test/binder-list KEEP_SYMBOLS=1 release
%{make_build} -C test/binder-ping KEEP_SYMBOLS=1 release
%{make_build} -C test/binder-call KEEP_SYMBOLS=1 release
%install
%{make_build} LIBDIR=%{_libdir} DESTDIR=%{buildroot} install-dev
%{make_build} -C test/binder-bridge DESTDIR=%{buildroot} install
%{make_build} -C test/binder-list DESTDIR=%{buildroot} install
%{make_build} -C test/binder-ping DESTDIR=%{buildroot} install
%{make_build} -C test/binder-call DESTDIR=%{buildroot} install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%check

%{make_build} -C unit test
%package tools
Summary: Binder tools
Requires: %{name} >= %{version}
%description tools
Binder command line utilities

%files -f %{oreon_filedir}/main.list
%files -n libgbinder-devel -f %{oreon_filedir}/libgbinder-devel.list
%files -n libgbinder-tools -f %{oreon_filedir}/libgbinder-tools.list

%changelog

%autochangelog
