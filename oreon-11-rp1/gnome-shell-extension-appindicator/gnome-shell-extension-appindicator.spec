%global source0_hash 3f692824e54c2192d984a24e1685722d1c88787e24dba662aecabe0b7f9e2bbc

%global forgeurl https://github.com/ubuntu/gnome-shell-extension-appindicator
%global uuid appindicatorsupport@rgcjonas.gmail.com

Name: gnome-shell-extension-appindicator
Version: 66
%forgemeta
Release: %autorelease
Summary: AppIndicator/KStatusNotifierItem support for GNOME Shell
BuildArch: noarch

License: GPL-2.0-only
URL: %{forgeurl}
Source0: %{forgesource}

BuildRequires: gettext
BuildRequires: glib2
BuildRequires: jq
BuildRequires: meson

Requires: gnome-shell >= 3.14.0
Requires: libappindicator-gtk3

# gnome-shell-extension-appindicator version >= 40 now also includes
# support for legacy X11 tray icons and the topicons(-plus) extensions
# are no longer maintained upstream
Provides:  gnome-shell-extension-topicons-plus = %{version}-%{release}
Obsoletes: gnome-shell-extension-topicons-plus <= 27-9

%description
This extension integrates Ubuntu AppIndicators and KStatusNotifierItems (KDE's
blessed successor of the systray) into GNOME Shell.

You can use gnome-tweaks (additional package) or run in terminal:

  $ gnome-extensions enable %uuid

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%build
%meson \
    -Dlocal_install=disabled
%meson_build

%install
%meson_install
%find_lang AppIndicatorExtension
rm %{buildroot}%{_datadir}/glib-2.0/schemas/gschemas.compiled

%files -f AppIndicatorExtension.lang
%license LICENSE
%doc README.md AUTHORS.md
%{_datadir}/gnome-shell/extensions/%{uuid}/
%{_datadir}/glib-2.0/schemas/*.gschema.xml

%changelog
%autochangelog
