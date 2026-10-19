%global source0_hash 727fbc2cfac5be7eef2ab9b797b951afd8f5261872c373a7c79c369b91f751bf
Name:           guake
Version:        3.10.1
Release:        1%{?dist}
Summary:        Drop-down terminal for GNOME
License:        GPL-2.0-or-later
URL:            http://guake-project.org/
Source0:        https://github.com/guake/guake/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
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
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  glib2
BuildRequires:  gnome-common
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3dist(pbr)
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
