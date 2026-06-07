%global source0_hash none

%global fontname paktype-naskh-basic
%global release_date 20231228

Version:       7.0
Release:       4.%{release_date}%{?dist}
URL:           https://sourceforge.net/projects/paktype/

%global foundry           paktype
%global fontlicense       GPL-2.0-only WITH Font-exception-2.0
%global fontlicenses      PakType_Naskh_Basic_License.txt
%global fontdocs          For_Code_and_Features.txt

%global fontfamily        PakType Naskh Basic
%global fontsummary       Fonts for Arabic, Farsi, Urdu and Sindhi from PakType
%global fonts             PakTypeNaskhBasic*.ttf
%global fontconfs         %{SOURCE10}

%global fontdescription   %{expand:
The paktype-naskh-basic-fonts package contains fonts for the display of \
Arabic, Farsi, Urdu and Sindhi from PakType by Lateef Sagar.
}

Source0:        https://deb.debian.org/debian/pool/main/f/fonts-paktype/fonts-paktype_0.0svn20121225.orig.tar.bz2
Source10:       55-0-%{fontpkgname}.conf

%fontpkg

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -c -T
tar xf %{SOURCE0}
cp fonts-paktype-0.0svn20121225/Development/Code/Naskh\ Basic/PakTypeNaskhBasic*.ttf .
cp fonts-paktype-0.0svn20121225/Documentation/For\ Code\ and\ Features.txt For_Code_and_Features.txt
cp -r fonts-paktype-0.0svn20121225/License\ files .
rm -rf fonts-paktype-0.0svn20121225
pushd License\ files/
sed -i 's/\r$//' "PakType Naskh Basic License.txt"
popd
mv License\ files/PakType\ Naskh\ Basic\ License.txt PakType_Naskh_Basic_License.txt
chmod 644 For_Code_and_Features.txt

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
