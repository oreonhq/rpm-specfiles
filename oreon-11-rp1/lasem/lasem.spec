%global source0_hash none

%global apiver 0.6

Name:           lasem
Version:        0.6.0
Release:        4%{?dist}
Summary:        A library for rendering SVG and Mathml, implementing a DOM like API

License:        LGPL-2.1-or-later
URL:            https://lasemproject.github.io/lasem/
Source0:        https://github.com/LasemProject/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
# dropped as in 0.6.0 the different translatable strings have changed
# will attempt to contact the translator
#Patch0:      000-add-ka.patch

BuildRequires:  gcc
BuildRequires:  intltool
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(pango)
BuildRequires:  meson
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gi-docgen
Requires:       lyx-fonts
Provides:       bundled(itex2mml) = 1.6.1

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
%autosetup

%build
%meson -Ddocumentation=enabled

%meson_build

%install
%meson_install
find $RPM_BUILD_ROOT%{_libdir} -type f -name '*.la' -delete -print

#docs are installed using %%doc
rm -rf $RPM_BUILD_ROOT%{_prefix}/doc

%find_lang %{name}-%{apiver}

%ldconfig_scriptlets

%check
# disabled until failure can be resolved upstream
#%%meson_test

%files -f %{name}-%{apiver}.lang
%doc NEWS.md README.md
%license COPYING itex2mml/COPYING.itex2MML
%{_libdir}/girepository-1.0/Lasem-%{apiver}.typelib
%{_libdir}/lib%{name}-%{apiver}.so.*

%files devel
%{_includedir}/%{name}-%{apiver}
%{_libdir}/lib%{name}-%{apiver}.so
%{_libdir}/pkgconfig/%{name}-%{apiver}.pc
%{_datadir}/gir-1.0/Lasem-%{apiver}.gir
%{_docdir}/%{name}-%{apiver}

%files render
%{_bindir}/%{name}-render-%{apiver}
%{_mandir}/man1/%{name}-render-%{apiver}.1*

%changelog
%autochangelog
