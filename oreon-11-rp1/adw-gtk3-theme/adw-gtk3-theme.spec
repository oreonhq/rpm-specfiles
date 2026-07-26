%global source0_hash c396e4f0df3eea081186ae13321345f21b9934691b4b4d75b4956f00cbd033d1

Name:           adw-gtk3-theme
Version:        6.4
Release:        %autorelease
Summary:        The theme from libadwaita ported to GTK-3
BuildArch:      noarch

License:        LGPL-2.1-only
URL:            https://github.com/lassekongo83/adw-gtk3
Source0:        %{url}/releases/download/v%{version}/adw-gtk3v%{version}.tar.xz
Source1:        https://raw.githubusercontent.com/lassekongo83/adw-gtk3/refs/heads/main/README.md#/README.md.upstream
Source2:        https://raw.githubusercontent.com/lassekongo83/adw-gtk3/refs/heads/main/LICENSE#/LICENSE.upstream

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c

%install
install -Dpm644 %{SOURCE1} README.md
install -Dpm644 %{SOURCE2} LICENSE
mkdir -p %{buildroot}%{_datadir}/themes
cp -ap adw-gtk3 %{buildroot}%{_datadir}/themes/adw-gtk3/
cp -ap adw-gtk3-dark %{buildroot}%{_datadir}/themes/adw-gtk3-dark/

%files
%license LICENSE
%doc README.md
%{_datadir}/themes/adw-gtk3/
%{_datadir}/themes/adw-gtk3-dark/

%changelog
%autochangelog
