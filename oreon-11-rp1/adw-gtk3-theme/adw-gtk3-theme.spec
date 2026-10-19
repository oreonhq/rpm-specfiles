%global source2_hash 20c17d8b8c48a600800dfd14f95d5cb9ff47066a9641ddeab48dc54aec96e331
%global source1_hash a96ce4af3bc5b7855a21078c1393e694d4bef8dd091df00fa5a2e52233242200
%global source0_hash a81780fadfc432be0fc3d89c4ebb41aa28e4f032d42c36f9789c57dd10cfa41c
Name:           adw-gtk3-theme
Version:        6.5
Release:        1%{?dist}
Summary:        The theme from libadwaita ported to GTK-3
BuildArch:      noarch
License:        LGPL-2.1-only
URL:            https://github.com/lassekongo83/adw-gtk3
Source0:        https://github.com/lassekongo83/adw-gtk3/releases/download/v%{version}/adw-gtk3v%{version}.tar.xz
Source1:        https://raw.githubusercontent.com/lassekongo83/adw-gtk3/refs/heads/main/README.md#/README.md.upstream
Source2:        https://raw.githubusercontent.com/lassekongo83/adw-gtk3/refs/heads/main/LICENSE#/LICENSE.upstream
# oreon:deps

# /oreon:deps
%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%install
install -Dpm644 %{SOURCE1} README.md
install -Dpm644 %{SOURCE2} LICENSE
mkdir -p %{buildroot}%{_datadir}/themes
cp -ap adw-gtk3 %{buildroot}%{_datadir}/themes/adw-gtk3/
cp -ap adw-gtk3-dark %{buildroot}%{_datadir}/themes/adw-gtk3-dark/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
