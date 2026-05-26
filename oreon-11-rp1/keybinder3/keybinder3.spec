Name:		keybinder3
Version:	0.3.2
Release:	22%{?dist}
Summary:	A library for registering global keyboard shortcuts
License:	MIT
URL:		https://github.com/kupferlauncher/keybinder
Source0:        https://github.com/kupferlauncher/keybinder/releases/download/keybinder-3.0-v0.3.2/keybinder-3.0-0.3.2.tar.gz
Patch0:        https://github.com/kupferlauncher/keybinder/pull/18.patch#/fix_gtkdoc.patch
# oreon url source checksums begin
%global source0_sha256 e6e3de4e1f3b201814a956ab8f16dfc8a262db1937ff1eee4d855365398c6020
%global source0_file keybinder-3.0-0.3.2.tar.gz
# oreon url source checksums end

BuildRequires:	pkgconfig(gtk+-3.0), gtk-doc, gobject-introspection-devel
BuildRequires: make

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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/keybinder-3.0-0.3.2.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "e6e3de4e1f3b201814a956ab8f16dfc8a262db1937ff1eee4d855365398c6020" || { echo "oreon: Source0 SHA256 mismatch for keybinder-3.0-0.3.2.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1 -n keybinder-3.0-%{version}

%build
%configure --enable-gtk-doc
%make_build

%install
%make_install

rm -rf %{buildroot}/%{_libdir}/libkeybinder-3.0.la

%ldconfig_scriptlets

%files
%license COPYING
%doc NEWS AUTHORS README
%{_libdir}/libkeybinder-3.0.so.*
%{_libdir}/girepository-1.0/Keybinder-3.0.typelib

%files devel
%dir %{_includedir}/keybinder-3.0/
%{_includedir}/keybinder-3.0/keybinder.h
%{_libdir}/pkgconfig/keybinder-3.0.pc
%{_libdir}/libkeybinder-3.0.so
%{_datadir}/gir-1.0/Keybinder-3.0.gir

%files doc
%dir %{_datadir}/gtk-doc/html/keybinder-3.0/
%{_datadir}/gtk-doc/html/keybinder-3.0/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.3.2-22
- Import
