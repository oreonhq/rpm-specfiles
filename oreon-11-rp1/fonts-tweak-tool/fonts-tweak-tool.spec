Name: fonts-tweak-tool
Version: 0.4.8
Release: 11%{?dist}
Summary: Tool for customizing fonts per language

License: LGPL-3.0-or-later
URL: https://gitlab.com/tagoh/%{name}/
Source0: https://gitlab.com/api/v4/projects/tagoh%2F%{name}packages/generic/%{name}/%{version}/%{name}-%{version}.tar.bz2

BuildRequires: desktop-file-utils
BuildRequires: intltool
BuildRequires: python3-devel
BuildRequires: gobject-introspection-devel pkgconfig(glib-2.0)
BuildRequires: make
Requires: libeasyfc-gobject >= 0.14.1
Requires: python3-gobject
Requires: gtk3
Requires: hicolor-icon-theme

%description
fonts-tweak-tool is a GUI tool for customizing fonts per language on desktops
using fontconfig.

%prep
%autosetup -p1
autoreconf --install

%build
%configure --disable-static PYTHON=%{__python3}
%make_build

%install
%make_install

desktop-file-install --dir=%{buildroot}%{_datadir}/applications --remove-only-show-in="GNOME;Unity;" fonts-tweak-tool.desktop

rm -f %{buildroot}%{_libdir}/lib*.so
%__brp_remove_la_files
rm -f %{buildroot}%{_datadir}/gir-*/FontsTweak-*.gir

%find_lang %{name}

%ldconfig_scriptlets

%files -f %{name}.lang
%doc README AUTHORS NEWS
%license COPYING
%{_bindir}/%{name}
%{python3_sitearch}/fontstweak
%{_datadir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_libdir}/libfontstweak-resources.so.0*
%{_libdir}/girepository-*/FontsTweak-*.typelib


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.4.8-11
- Import
