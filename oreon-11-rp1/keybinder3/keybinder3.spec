%global source0_hash e6e3de4e1f3b201814a956ab8f16dfc8a262db1937ff1eee4d855365398c6020
Name:		keybinder3
Version:	0.3.2
Release:        1%{?dist}
Summary:        A library for registering global keyboard shortcuts
License:	MIT
URL:		https://github.com/kupferlauncher/keybinder
Source0:        https://github.com/kupferlauncher/keybinder/releases/download/keybinder-3.0-v0.3.2/keybinder-3.0-0.3.2.tar.gz#/keybinder3-0.3.2.tar.gz
Patch0:        https://github.com/kupferlauncher/keybinder/pull/18.patch#/fix_gtkdoc.patch
# oreon:deps
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  make
BuildRequires:  pkgconfig(gtk+-3.0)
# /oreon:deps
%description
Keybinder is a library for registering global keyboard shortcuts. 
Keybinder works with GTK-based applications using the X Window System.

The library contains:
- A C library, libkeybinder
- Gobject-Introspection bindings

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
This package contains the development files for %{name}.

%package doc
Summary: Documentation for %{name}
BuildArch: noarch
Requires: %{name} = %{version}-%{release}
Requires: devhelp
%description doc
This package contains documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir keybinder-3.0-%{version}
%oreon_prep
%build

%configure --enable-gtk-doc
%make_build
%install
%make_install
rm -rf %{buildroot}/%{_libdir}/libkeybinder-3.0.la
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n keybinder3-devel -f %{oreon_filedir}/keybinder3-devel.list
%files -n keybinder3-doc -f %{oreon_filedir}/keybinder3-doc.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.3.2-22
- Import
