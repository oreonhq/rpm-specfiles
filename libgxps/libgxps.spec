Name:           libgxps
Version:        0.3.2
Release:        12%{?dist}
Summary:        GObject based library for handling and rendering XPS documents

License:        LGPL-2.1-or-later
URL:            https://wiki.gnome.org/Projects/libgxps
Source0:        https://ftp.gnome.org/pub/gnome/sources/%{name}/0.3/%{name}-%{version}.tar.xz

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  gtk3-devel
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  cairo-devel
BuildRequires:  libarchive-devel
BuildRequires:  freetype-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel
BuildRequires:  lcms2-devel

%description
libgxps is a GObject based library for handling and rendering XPS
documents.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        tools
Summary:        Command-line utility programs for manipulating XPS files
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    tools
The %{name}-tools contains command-line programs for manipulating XPS format
documents using the %{name} library.


%prep
%autosetup -p1


%build
%meson -Denable-gtk-doc=true -Denable-man=true
%meson_build


%install
%meson_install


%files
%doc AUTHORS MAINTAINERS NEWS README TODO
%license COPYING
%{_libdir}/*.so.2
%{_libdir}/*.so.2.*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/*.typelib


%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/*.gir
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/libgxps


%files tools
%{_bindir}/xpsto*
%{_mandir}/man1/xpsto*.1*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.3.2-12
- Prepare for Oreon 11 (RP1)
