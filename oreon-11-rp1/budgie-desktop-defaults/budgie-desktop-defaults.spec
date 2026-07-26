%global source0_hash a790335563234c9f023d071d9ed8c78ab30570e836d3e973818bea369733f616

Name:           budgie-desktop-defaults
Version:        0.5.4
Release:        3%{?dist}
Summary:        Budgie Desktop Defaults for Fedora

License:        CC-BY-SA-4.0
URL:            https://forge.moderndesktop.dev/BuddiesOfBudgie/fedora-budgie-desktop-defaults
Source0:        %{url}/releases/download/v%{version}/%{name}-v%{version}.tar.xz
Source1:        %{url}/releases/download/v%{version}/%{name}-v%{version}.tar.xz.asc
Source2:        https://forge.moderndesktop.dev/BuddiesOfBudgie/keyrings/raw/branch/main/JoshuaStrobl.gpg

BuildArch:      noarch
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  meson
Requires:       budgie-desktop
Requires:       desktop-backgrounds-budgie
Requires:       papirus-icon-theme
Requires:       pocillo-gtk-theme

%description
Budgie Desktop Defaults for Fedora.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README.md
%license LICENSE
%dir %{_datadir}/glib-2.0/schemas
%{_datadir}/glib-2.0/schemas/10_budgie_*.gschema.override

%changelog
%autochangelog
