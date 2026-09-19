%global source0_hash 966ee18c9e18587f8dcb7b2165c22b03d1e319d5a486f16b3c9423fd1546cf33

%global uuid    com.github.Latesil.%{name}

Name:           theme-switcher
Version:        2.0.4
Release:        25%{?dist}
Summary:        Switch dark/light GTK theme automatically during day/night

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/Latesil/theme-switcher
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# Default systemd user unit preset for < F32
# * https://fedoraproject.org/wiki/Changes/Systemd_presets_for_user_units
Source1:        99-default.preset

BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  intltool
%if 0%{?fedora}
BuildRequires:  libappstream-glib
%endif
BuildRequires:  meson >= 0.50.0
BuildRequires:  glib2-devel
BuildRequires:  python3-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(glib-2.0)

Requires:       gnome-terminal
Requires:       gtk3
Requires:       hicolor-icon-theme
Requires:       python3-gobject

%{?systemd_requires}

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

%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{uuid}

%if 0%{?fedora} < 32
install -Dpm0644 %{SOURCE1} -t %{buildroot}%{_prefix}/lib/systemd/user-preset/
%endif

%check
%if 0%{?fedora}
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
%endif
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%post
%systemd_user_post %{name}-auto.service

%preun
%systemd_user_preun %{name}-auto.service

%files -f %{uuid}.lang
%license LICENSE
%doc README.md CREDITS
%{_bindir}/%{name}-auto.py
%{_bindir}/%{name}-gui
%{_bindir}/%{name}-manual.py
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/icons/hicolor/symbolic/*/*.svg
%{_metainfodir}/*.xml
%{_userunitdir}/%{name}-auto.*
%{python3_sitelib}/Themeswitcher/

%if 0%{?fedora} < 32
%{_prefix}/lib/systemd/user-preset/99-default.preset
%endif

%changelog
%autochangelog
