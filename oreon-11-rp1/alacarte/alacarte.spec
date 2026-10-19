%global source0_hash 3f4eb9370a9cd97547ec2f182d091f59315eea5ed335cc8243d4df2354862d52
%global app_id  org.gnome.alacarte
Name:           alacarte
Version:        3.58.0
Release:        1%{?dist}
Summary:        Menu editor for the GNOME desktop
License:        LGPL-2.0-or-later
URL:            https://gitlab.gnome.org/GNOME/alacarte
Source0:        https://download.gnome.org/sources/alacarte/3.58/%{name}-%{version}.tar.xz
BuildArch:      noarch
Requires:       gnome-menus >= 3.5.3
Requires:       gtk3
Requires:       python3-gobject
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-style-xsl
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  pkgconfig(libgnome-menu-3.0)
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  python3-devel
# /oreon:deps
%description
Alacarte is a graphical menu editor that lets you edit, add, and delete
menu entries. It follows the freedesktop.org menu specification and
should work with any desktop environment that uses this specification.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
autoreconf -i -f

%build

%configure
%make_build
%install
%make_install
desktop-file-install \
  --delete-original \
  --add-only-show-in=GNOME \
  --remove-not-show-in=KDE \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{app_id}.metainfo.xml
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
