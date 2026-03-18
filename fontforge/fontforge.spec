%global gettext_package FontForge

Name:           fontforge
Version:        20251009
Release:        2%{?dist}
Summary:        Outline and bitmap font editor

License:        GPL-3.0-or-later
URL:            http://fontforge.github.io/
Source0:        https://github.com/fontforge/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

Requires:       xdg-utils
Requires:       (autotrace or potrace)
Requires:       hicolor-icon-theme

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel
BuildRequires:  libpng-devel
BuildRequires:  giflib-devel
BuildRequires:  libxml2-devel
BuildRequires:  freetype-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libXt-devel
BuildRequires:  xorg-x11-proto-devel
BuildRequires:  gettext
BuildRequires:  pango-devel
BuildRequires:  cairo-devel
BuildRequires:  libspiro-devel
BuildRequires:  python3-devel
BuildRequires:  readline-devel
BuildRequires:  libappstream-glib
BuildRequires:  woff2-devel
# F25 build is failing add following to fix
BuildRequires:  shared-mime-info
# F33 onward need now
BuildRequires:  gtk3-devel
BuildRequires:  python3-sphinx
BuildRequires: make
# 20151009 version requires below
BuildRequires: gtkmm3.0-devel

%py_provides python3-fontforge
%py_provides python3-psMat

%description
FontForge (former PfaEdit) is a font editor for outline and bitmap
fonts. It supports a range of font formats, including PostScript
(ASCII and binary Type 1, some Type 3 and Type 0), TrueType, OpenType
(Type2) and CID-keyed fonts.

%package devel
Summary: Development files for fontforge
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-doc = %{version}-%{release}

%description devel
This package includes the library files you will need to compile
applications against fontforge.

%package doc
Summary: Documentation files for %{name}
BuildArch: noarch

%description doc
This package contains documentation files for %{name}.


%prep
%autosetup

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%cmake -DCMAKE_BUILD_TYPE=Release \
          -DENABLE_WOFF2=ON \
          -DPYHOOK_INSTALL_DIR=%{python3_sitearch}
%cmake_build

%install
%cmake_install

desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications            \
  --add-category X-Fedora                                  \
  desktop/org.fontforge.FontForge.desktop

# remove unneeded .la and .a files
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
find $RPM_BUILD_ROOT -name '*.a' -exec rm -f {} ';'

rm -f %{buildroot}%{_datadir}/doc/fontforge/{.buildinfo,.nojekyll}
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml

# Find translations
%find_lang %{gettext_package}

%check
%ctest

%files -f %{gettext_package}.lang
%doc AUTHORS
%license LICENSE COPYING.gplv3
%{_bindir}/*
%{_libdir}/lib*.so.*
%{_datadir}/applications/*FontForge.desktop
%{_datadir}/fontforge
%{_datadir}/icons/hicolor/*/apps/org.fontforge.FontForge*
%{_mandir}/man1/*.1*
%{_datadir}/mime/packages/fontforge.xml
%{_metainfodir}/org.fontforge.FontForge.appdata.xml
%{python3_sitearch}/fontforge.so
%{python3_sitearch}/psMat.so

%files devel
%{_libdir}/lib*.so

%files doc
%doc %{_pkgdocdir}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 20251009-2
- Prepare for Oreon 11 (RP1)
