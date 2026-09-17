%global source0_hash c328921048c09236c14b2bf9773cb4d82c71288aa07ce7e0781e7d154794e179

Name:           gnome-shell-extension-gamemode
Version:        11.0
Release:        %autorelease
Summary:        GameMode integration for GNOME Shell
License:        LGPL-2.1-only
URL:            https://github.com/trsnaqe/gamemode-shell-extension
Source0:        %{url}/archive/V%{version}/gamemode-extension-V%{version}.tar.gz
Source1:        lgpl-2.1.md

BuildRequires:  meson
BuildRequires:  gettext
BuildRequires:  glib2
Requires:       gnome-shell >= 45
Requires:       gamemode
BuildArch:      noarch

%description
GNOME Shell extension to integrate with GameMode. Can display
an icon when GameMode is active and also emit notifications
when the global GameMode status changes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n gamemode-shell-extension-%{version}%{?prerelease:-%{prerelease}}
cp %{SOURCE1} .

%build
%meson
%meson_build

%install
%meson_install
rm %{buildroot}/%{_datadir}/glib-2.0/schemas/gschemas.compiled

%files
%doc README.md
%license
%{_datadir}/gnome-shell/extensions/gamemodeshellextension@trsnaqe.com/
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.gamemodeshellextension.gschema.xml

%changelog
%autochangelog
