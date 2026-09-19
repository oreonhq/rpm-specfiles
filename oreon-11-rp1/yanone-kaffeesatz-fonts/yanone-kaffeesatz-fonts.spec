%global source0_hash 2277efb5f467a79e92020cf1001e464cb4c3fabfe22fe7cb85422760ddfe114d

# SPDX-License-Identifier: MIT
%global forgeurl    https://github.com/alexeiva/yanone-kaffeesatz/
%global commit      1da49356a388c67da5b51d54fd6ad5a686d96c46
%forgemeta

Epoch:   1
Version: 2.001
Release: 20%{?dist}
URL:     http://www.yanone.de/typedesign/kaffeesatz/

%global foundry           Yanone
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt
%global fontdocs          *txt *html *md
%global fontdocsex        %{fontlicenses}

%global fontfamily        Kaffeesatz
%global fontsummary       Yanone Kaffeesatz, a decorative font family
%global fonts             fonts/ttf/*ttf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Yanone Kaffeesatz is a sans-serif decorative Latin font family by Jan Gerner,
suitable for titles and short runs of text.

Its Bold is reminiscent of 1920s coffee house typography, while the rather thin
fonts bridge the gap to present times.

You can witness Kaffeesatz use on German fresh-water gyms, Dubai mall promos
and New Zealand McDonalds ads. And of course on coffee and foodstuff packaging
and café design around the globe.}

Source0:  %{forgesource}
Source10: 60-%{fontpkgname}.xml

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
