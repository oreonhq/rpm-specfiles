%global source0_hash 6f8d01602ca26f654d7e7d1aebd8cf60e25e7c97d649d18360ebf01111df9f3d

Name:           guake
Version:        3.7.0
Release:        26%{?dist}
Summary:        Drop-down terminal for GNOME

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://guake-project.org/
Source0:        https://github.com/guake/guake/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  %{py3_dist pbr}
BuildRequires:  gettext
BuildRequires:  gnome-common
BuildRequires:  make
BuildRequires:  glib2
BuildRequires:  desktop-file-utils

Requires:       python3 >= 3.5
Requires:       python3-cairo
Requires:       python3-dbus
Requires:       python3-gobject
Requires:       python3-pyxdg
Requires:       %{py3_dist pbr}
Requires:       keybinder3
Requires:       libwnck3
Requires:       libnotify
Requires:       vte291 >= 0.42

Recommends:     libutempter

%description
Guake is a dropdown terminal made for the GNOME desktop environment. Guake's
style of window is based on an FPS game, and one of its goals is to be easy to
reach.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

sed -i -e 's|PREFIX?=/usr/local|PREFIX?=/usr|' Makefile
sed -i -e 's|update-desktop-database|true|' Makefile

%build
%make_build

%install
PBR_VERSION=%{version} %make_install prefix=%{_prefix}

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}-prefs.desktop

rm %{buildroot}%{_datadir}/glib-2.0/schemas/gschemas.compiled

%find_lang %{name}

%files -f %{name}.lang
%doc README.rst NEWS.rst
%license COPYING
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}*egg-info/
%{_bindir}/%{name}
%{_bindir}/%{name}-toggle
%{_datadir}/applications/%{name}-prefs.desktop
%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/org.guake.gschema.xml
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}/

%changelog
%autochangelog
