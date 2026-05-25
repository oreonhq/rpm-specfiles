Name:		keybinder3
Version:	0.3.2
Release:	22%{?dist}
Summary:	A library for registering global keyboard shortcuts
License:	MIT
URL:		https://github.com/kupferlauncher/keybinder
Source0:	%{url}/releases/download/keybinder-3.0-v%{version}/keybinder-3.0-%{version}.tar.gz
Patch0:     %{url}/pull/18.patch#/fix_gtkdoc.patch

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
