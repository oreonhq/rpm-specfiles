%global source0_hash 68f62d33446b80c0567ff310ea3789922117469d57068e563ce997fa3fbb1299

# SPDX-License-Identifier: MIT
%global forgeurl    https://github.com/googlefonts/rubik
%global commit      2e360a2044e6d1d4e3a6ddd992144a9a0b5446af
%forgemeta

Version: 2.100
Release: 15%{?dist}
URL:     %{forgeurl}

%global foundry           google
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt
%global fontdocs          *txt *md
%global fontdocsex        %{fontlicenses}

%global fontfamily        Rubik
%global fontsummary       Rubik, a sans serif font family with slightly rounded corners
%global fonts             fonts/ttf/*ttf fonts/variable*fonts/*ttf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Rubik is a sans serif font family with slightly rounded corners designed by
Philipp Hubert and Sebastian Fischer at Hubert & Fischer as part of the Chrome
Cube Lab project.}

Source0:  %{forgesource}
Source10: 58-%{fontpkgname}.xml

%fontpkg

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup
chmod 644 %{fontdocs} %{fontlicenses}

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
%autochangelog
