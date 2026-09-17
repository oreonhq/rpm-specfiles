%global source0_hash 31e40d30b5624352681a0eb4e155708679b0349e084913e419f5b3c2c668ac76

Name: libgbinder
Version: 1.1.43
Release: 2%{?dist}
Summary: Binder client library
License: BSD
URL: https://github.com/mer-hybris/libgbinder
Source0: %{url}/archive/refs/tags/%{version}.tar.gz

%global libglibutil_version 1.0.52

BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(libglibutil) >= %{libglibutil_version}
BuildRequires: pkgconfig
BuildRequires: make
BuildRequires: gcc
BuildRequires: bison flex
Requires: libglibutil >= %{libglibutil_version}

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

%autosetup -p1

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

%check
%{make_build} -C unit test

%files
%{_libdir}/%{name}.so.*
%license LICENSE

%files devel
%{_libdir}/pkgconfig/*.pc
%{_libdir}/%{name}.so
%{_includedir}/gbinder

# Tools
# Missing manpages: https://github.com/mer-hybris/libgbinder/issues/107
%package tools
Summary: Binder tools
Requires: %{name} >= %{version}

%description tools
Binder command line utilities

%files tools
%{_bindir}/binder-bridge
%{_bindir}/binder-list
%{_bindir}/binder-ping
%{_bindir}/binder-call

%changelog
%autochangelog
