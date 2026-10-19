%global source0_hash 991a23debf7e2c5683516d7a90eca112a9c985252e984d0e3410691d7e1159ea
%global apiver 0.6
Name:           lasem
Version:        0.6.0
Release:        4%{?dist}
Summary:        A library for rendering SVG and Mathml, implementing a DOM like API
License:        LGPL-2.1-or-later
URL:            https://lasemproject.github.io/lasem/
Source0:        https://github.com/LasemProject/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
Requires:       lyx-fonts
Provides:       bundled(itex2mml) = 1.6.1
# oreon:deps
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gi-docgen
BuildRequires:  intltool
BuildRequires:  meson
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(pango)
# /oreon:deps
%description
Lasem is a library for rendering SVG and Mathml, implementing a DOM like API.
It's based on GObject and use Pango and Cairo for the rendering.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        render
Summary:        Simple MathML converter
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    render
Simple application, which is able to convert a Mathml, a latex math or a SVG
file to either a PNG, PDF or SVG image.

%prep
%oreon_prep
%build

%meson -Ddocumentation=enabled
%meson_build
%install
%meson_install
find $RPM_BUILD_ROOT%{_libdir} -type f -name '*.la' -delete -print
rm -rf $RPM_BUILD_ROOT%{_prefix}/doc
%find_lang %{name}-%{apiver}
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%files -f %{oreon_filedir}/main.list
%files -n lasem-devel -f %{oreon_filedir}/lasem-devel.list
%files -n lasem-render -f %{oreon_filedir}/lasem-render.list

%changelog

%autochangelog
