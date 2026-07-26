%global source0_hash ab4728157b68f84492512c7a451fe193924ae2aac3aa851de06eb3fd5acdc714

Name: libglibutil
Version: 1.0.80
Release: 2%{?dist}
Summary: Library of glib utilities
License: BSD
URL: https://github.com/sailfishos/libglibutil
Source0: %{url}/archive/refs/tags/%{version}.tar.gz

BuildRequires: pkgconfig
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: make gcc

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

%check
%{make_build} -C test test

%files
%license LICENSE
%{_libdir}/%{name}.so.*

%files devel
%{_libdir}/pkgconfig/*.pc
%{_libdir}/%{name}.so
%{_includedir}/gutil

%changelog
%autochangelog
