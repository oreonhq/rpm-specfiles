%global source0_hash 9bd968a1f74c33cd9070000252430fd48e4a3867aa413cf8c11891f0f5c8ed44

%global forgeurl https://github.com/derrod/legendary
%global commit 42af7b5db78eb22210ae6cf2dd1b913c64ca3183

Name:           legendary
Version:        0.20.34
%forgemeta
Release:        %autorelease
Summary:        Free and open-source replacement for the Epic Games Launcher
BuildArch:      noarch

License:        GPL-3.0-or-later
URL:            https://github.com/derrod/legendary
Source:         %{forgesource}

BuildRequires:  python3-devel >= 3.9
Recommends:     wine
Recommends:     wine-dxvk

%description
Legendary is an open-source game launcher that can download and install games
from the Epic Games platform on Linux, macOS, and Windows. Its name as a
tongue-in-cheek play on tiers of item rarity in many MMORPGs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup
%generate_buildrequires
%pyproject_buildrequires

# E: non-executable-script
for lib in %{name}/{*.py,downloader/*.py,lfs/*.py,models/*.py}; do
  sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
  touch -r $lib $lib.new &&
  mv $lib.new $lib
done

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{name}

%check
%dnl %pyproject_check_import

%files -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
%autochangelog
