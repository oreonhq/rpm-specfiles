%global source0_hash aa97dcd2a8576ae18de6c16c19744aae1573a3da7541af4b98a91930a30a3178

Name:           screenfetch
Version:        3.9.1
Release:        15%{?dist}
Summary:        A "Bash Screenshot Information Tool"

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/KittyKatt/screenFetch
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
Recommends:     scrot
Requires:       pciutils

%description
This handy Bash script can be used to generate one of
those nifty terminal theme information + ASCII distribution
logos you see in everyone's screen-shots nowadays. It will
auto-detect your distribution and display an ASCII version
of that distribution's logo and some valuable information
to the right. There are options to specify no ASCII art,
colors, taking a screen-shot upon displaying info, and even
customizing the screen-shot command! This script is very easy
to add to and can easily be extended.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn screenFetch-%{version}
sed -i -e '1s|.*|#!/bin/bash|' screenfetch-dev

%build
#Nothing to build

%install
install -m 755 -p -D screenfetch-dev %{buildroot}%{_bindir}/screenfetch
install -m 644 -p -D screenfetch.1 %{buildroot}%{_mandir}/man1/screenfetch.1

%files
%license COPYING
%doc CHANGELOG README.mkdn TODO
%{_bindir}/screenfetch
%{_mandir}/man1/screenfetch.1*

%changelog
%autochangelog
