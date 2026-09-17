%global source0_hash 47228f0c07dfb2fbf51e35eb60f12c22113ef6923a0e23fcae3b2a4efee5ed29

Name: libmbim
Version: 1.32.0
Release: 3%{?dist}
Summary: Support library for the Mobile Broadband Interface Model protocol
License: LGPL-2.1-or-later
URL: https://gitlab.freedesktop.org/mobile-broadband/libmbim/
Source:        https://gitlab.freedesktop.org/mobile-broadband/libmbim/-/archive/%{version}/%{name}-%{version}.tar.bz2

BuildRequires: meson >= 0.53
BuildRequires: gcc
BuildRequires: glib2-devel >= 2.56
BuildRequires: gobject-introspection-devel
BuildRequires: gtk-doc
BuildRequires: pkgconfig
BuildRequires: python3
BuildRequires: help2man


%description
This package contains the libraries that make it easier to use MBIM
functionality from applications that use glib.


%package devel
Summary: Header files for adding MBIM support to applications that use glib
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: glib2-devel%{?_isa}
Requires: pkgconfig

%description devel
This package contains the header and pkg-config files for developing
applications using MBIM functionality from applications that use glib.

%package utils
Summary: Utilities to use the MBIM protocol from the command line
Requires: %{name}%{?_isa} = %{version}-%{release}
License: GPL-2.0-or-later

%description utils
This package contains the utilities that make it easier to use MBIM
functionality from the command line.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1


%build
# Let's avoid BuildRequiring bash-completion because it changes behavior
# of shell, at least until the .pc file gets into the -devel subpackage.
# We'll just install the bash-completion file ourselves.
%meson -Dgtk_doc=true -Dbash_completion=false
%meson_build


%install
%meson_install
find %{buildroot}%{_datadir}/gtk-doc |xargs touch --reference meson.build
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
cp -a src/mbimcli/mbimcli %{buildroot}%{_datadir}/bash-completion/completions/


%check
%meson_test


%ldconfig_scriptlets


%files
%license LICENSES/LGPL-2.1-or-later.txt
%doc NEWS AUTHORS README.md
%{_libdir}/libmbim-glib.so.4*
%{_libdir}/girepository-1.0/Mbim-1.0.typelib


%files devel
%{_includedir}/libmbim-glib/
%{_libdir}/pkgconfig/mbim-glib.pc
%{_libdir}/libmbim-glib.so
%{_datadir}/gtk-doc/html/libmbim-glib/
%{_datadir}/gir-1.0/Mbim-1.0.gir


%files utils
%license LICENSES/GPL-2.0-or-later.txt
%{_bindir}/mbimcli
%{_bindir}/mbim-network
%{_datadir}/bash-completion
%{_libexecdir}/mbim-proxy
%{_mandir}/man1/mbim*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.32.0-3
- Prepare for Oreon 11 (RP1)
