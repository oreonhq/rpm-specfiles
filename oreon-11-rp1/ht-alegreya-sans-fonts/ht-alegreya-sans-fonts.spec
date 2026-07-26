%global source0_hash ea545572d49e18e675d6b72a6754da344e24b9cacc3d2b76c1eb2bf9ae73a402

# SPDX-License-Identifier: MIT
%global forgeurl    https://github.com/huertatipografica/Alegreya-Sans
Version: 2.008
%forgemeta

Release: 22%{?dist}
URL:     https://www.huertatipografica.com/en/fonts/alegreya-sans-ht

%global foundry           HT
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt
%global fontdocs          *txt *md
%global fontdocsex        %{fontlicenses}

%global fontfamily        Alegreya Sans
%global fontsummary       Alegreya Sans, a humanist sans serif font family with a calligraphic feeling
%global fonts             fonts/otf/*otf
%global fontsex           fonts/otf/*SC*otf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Alegreya Sans is a humanist sans serif font family with a calligraphic feeling
that conveys a dynamic and varied rhythm. This gives a pleasant feeling to
readers of long texts.

The family follows humanist proportions and principles, just like the serif
version of the family, Alegreya. It achieves a playful and harmonious paragraph
through elements carefully designed in an atmosphere of diversity.}

Source0:  %{forgesource}
Source10: 58-%{fontpkgname}.xml

%fontpkg

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup
%linuxtext %{fontdocs} %{fontlicenses}
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
