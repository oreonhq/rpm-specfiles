%global source0_hash 44dacbe3c4b60c203b1d60f0a55ebf6c139823f83fd234f9b078ece7cb15676e

# SPDX-License-Identifier: MIT
%global forgeurl    https://github.com/huertatipografica/Alegreya
Version: 2.008
%forgemeta

Release: 18%{?dist}
URL:     https://www.huertatipografica.com/en/fonts/alegreya-ht-pro

%global foundry           HT
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt
%global fontdocs          *txt *md
%global fontdocsex        %{fontlicenses}

%global fontfamily        Alegreya
%global fontsummary       Alegreya, a dynamic and varied serif font family
%global fontpkgheader     %{expand:
# Small Caps are accessible in the main family using OpenType features
Obsoletes: ht-alegreya-smallcaps-fonts < %{version}-%{release}
}
%global fonts             fonts/otf/*otf
%global fontsex           fonts/otf/*SC*otf
%global fontconfs         %{SOURCE10}
%global fontdescription   %{expand:
Alegreya is a font family originally intended for literature. Among its
crowning characteristics, it conveys a dynamic and varied rhythm which
facilitates the reading of long texts. Also, it provides freshness to the page
while referring to the calligraphic letter, not as a literal interpretation,
but rather in a contemporary typographic language.

The italic has just as much care and attention to detail in the design as the
roman. The bold weights are strong, and the Black weights are really
experimental for the genre.

Not only does Alegreya provide great performance, but also achieves a strong
and harmonious text by means of elements designed in an atmosphere of
diversity.

Alegreya was chosen as one of 53 “Fonts of the Decade” at the ATypI Letter2
competition in September 2011, and one of the top 14 text type systems. It was
also selected in the 2nd Bienal Iberoamericana de Diseño, competition held in
Madrid in 2010.}

Source0:  %{forgesource}
Source10: 58-%{fontpkgname}.conf

%fontpkg

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
%autochangelog
