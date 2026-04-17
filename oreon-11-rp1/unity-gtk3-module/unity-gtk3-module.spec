Name:           unity-gtk3-module
Version:        0.0.0+18.04.20171202
Release:        1%{?dist}
Summary:        GTK3 module for exporting old-style menus as GMenuModels

License:        LGPL-3.0-or-later
URL:            https://launchpad.net/unity-gtk-module
Source0:        http://old-releases.ubuntu.com/ubuntu/pool/universe/u/unity-gtk-module/unity-gtk-module_0.0.0+18.04.20171202.orig.tar.gz

BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  gtk3-devel
BuildRequires:  libX11-devel
BuildRequires:  pkgconfig
BuildRequires:  libtool
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext-devel
BuildRequires:  gtk-doc
BuildRequires:  systemd-rpm-macros

Requires:       gtk3%{?_isa}
Requires:       glib2%{?_isa}

%description
Unity GTK3 module exports GTK menu shells over DBus. It provides appmenu
integration used by desktop components such as Plasma workspace integrations.

%prep
mkdir -p %{name}-%{version}
tar -xzf %{SOURCE0} -C %{name}-%{version}
# GCC 15 is stricter about pointer types here
sed -i 's/icon = g_object_ref (pixbuf);/icon = G_ICON (g_object_ref (pixbuf));/g' \
  %{name}-%{version}/lib/unity-gtk-menu-item.c
sed -i 's/window_data->old_model = g_object_ref (old_menu_model);/window_data->old_model = G_MENU_MODEL (g_object_ref (old_menu_model));/g' \
  %{name}-%{version}/src/main.c

%build
cd %{name}-%{version}
# Ubuntu orig tarball ships configure.ac only
if test ! -x ./configure; then
  gtkdocize --copy --docdir docs || :
  autoreconf -fiv
fi
%configure --with-gtk=3 --with-gtk-module-dir=%{_libdir}/gtk-3.0/modules
%make_build

%install
cd %{name}-%{version}
%make_install

%post
%glib2_gsettings_schema_post

%postun
%glib2_gsettings_schema_postun

%files
%license COPYING.LESSER
%doc AUTHORS NEWS README
%{_libdir}/gtk-3.0/modules/libunity-gtk-module.so
%{_libdir}/libunity-gtk3-parser.so.*
%{_datadir}/glib-2.0/schemas/com.canonical.unity-gtk-module.gschema.xml
%{_datadir}/upstart/sessions/unity-gtk-module.conf
%{_userunitdir}/unity-gtk-module.service

%changelog
* Tue Apr 14 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.0.0+18.04.20171202-1
- Add unity-gtk3-module package for GTK3 appmenu module support
