%global source0_hash 78becb1861f102057f7cac26c90bde2f4ef5027680c0d2758a7c2700b51dd73d
Name: piper
Version: 0.8
Release:        14%{?dist}
License: GPL-2.0-or-later AND LGPL-2.1-or-later
URL: https://github.com/libratbag/%{name}
Summary:        GTK application to configure gaming mice
Source0:        https://github.com/libratbag/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch: noarch
Requires: gtk3
Requires: hicolor-icon-theme
Requires: libratbag-ratbagd >= 0.14
Requires: python3-cairo
Requires: python3-evdev
Requires: python3-gobject
Requires: python3-lxml
%{?python_provide:%python_provide python3-%{name}}
# oreon:deps
BuildRequires:  appstream
BuildRequires:  desktop-file-utils
BuildRequires:  gettext-devel
BuildRequires:  git-core
BuildRequires:  gtk-update-icon-cache
BuildRequires:  libappstream-glib
BuildRequires:  libratbag-ratbagd
BuildRequires:  meson
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  python3-cairo
BuildRequires:  python3-devel
BuildRequires:  python3-evdev
BuildRequires:  python3-flake8
BuildRequires:  python3-gobject
BuildRequires:  python3-lxml
# /oreon:deps
%description
Piper is a GTK+ application to configure gaming mice, using libratbag
via ratbagd.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -S git
sed -e '/meson_install.sh/d' -i meson.build

# Workaround to https://bugzilla.redhat.com/show_bug.cgi?id=2100362

%build

%meson
%meson_build
%check

%meson_test
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%install
%meson_install
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
