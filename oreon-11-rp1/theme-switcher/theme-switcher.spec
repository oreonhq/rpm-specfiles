%global source0_hash 966ee18c9e18587f8dcb7b2165c22b03d1e319d5a486f16b3c9423fd1546cf33
%global uuid    com.github.Latesil.%{name}
Name:           theme-switcher
Version:        2.0.4
Release:        1%{?dist}
Summary:        Switch dark/light GTK theme automatically during day/night
License:        GPL-3.0-or-later
URL:            https://github.com/Latesil/theme-switcher
Source0:        https://github.com/Latesil/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        99-default.preset
BuildArch:      noarch
Requires:       gnome-terminal
Requires:       gtk3
Requires:       hicolor-icon-theme
Requires:       python3-gobject
%{?systemd_requires}
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  glib2-devel
BuildRequires:  intltool
BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  python3-devel
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
A global automated switcher for dark/light GTK theme during day/night and more.

Theme-switcher automatically can switch your:

  - GTK theme
  - GNOME Terminal profiles
  - Wallpapers
  - More will come...

To read docs run:

  xdg-open %{_docdir}/%{name}/README.md

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%find_lang %{uuid}
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%post

%systemd_user_post %{name}-auto.service
%preun

%systemd_user_preun %{name}-auto.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
