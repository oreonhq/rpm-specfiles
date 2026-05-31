%global source0_hash none

%global fontname paktype-naskh-basic
%global release_date 20231228

Version:       7.0
Release:       4.%{release_date}%{?dist}
URL:           https://sourceforge.net/projects/paktype/

%global foundry           paktype
%global fontlicense       GPL-2.0-only WITH Font-exception-2.0
%global fontlicenses      PakType_Naskh_Basic_License.txt
%global fontdocs          PakTypeNaskhBasicFeatures.pdf

%global fontfamily        PakType Naskh Basic
%global fontsummary       Fonts for Arabic, Farsi, Urdu and Sindhi from PakType
%global fonts             PakTypeNaskhBasic*.ttf
%global fontconfs         %{SOURCE10}

%global fontdescription   %{expand:
The paktype-naskh-basic-fonts package contains fonts for the display of \
Arabic, Farsi, Urdu and Sindhi from PakType by Lateef Sagar.
}

Source0:        https://downloads.sourceforge.net/project/paktype/PakType-Release-2023-12-28.tar.gz
Source10:       55-0-%{fontpkgname}.conf

%fontpkg

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -c
pwd
pushd License\ files/
%linuxtext -e ascii "PakType Naskh Basic License.txt"
popd

mv License\ files/PakType\ Naskh\ Basic\ License.txt PakType_Naskh_Basic_License.txt
mv Features/PakType\ Naskh\ Basic\ Features.pdf PakTypeNaskhBasicFeatures.pdf
chmod 644 PakTypeNaskhBasicFeatures.pdf

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 7.0-4.20231228
- Import
