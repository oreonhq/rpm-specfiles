%global source0_hash none

%global archivename crosextrafonts-carlito-20130920

Version:        1.103
Release:        0.28.20130920%{?dist}
URL:            https://bugs.chromium.org/p/chromium/issues/detail?id=280557

%global foundry           google
# License added in font as "otfinfo -i Carlito-Regular.ttf | grep License"
# also from http://code.google.com/p/chromium/issues/detail?id=280557
%global fontlicense       OFL-1.1

%global fontfamily        Carlito
%global fontsummary       Carlito, a sans-serif font family metric-compatible with Calibri font family
%global fontpkgheader     %{expand:
Obsoletes:      google-crosextra-carlito-fonts < 1.103-0.13.20130920
Provides:       google-crosextra-carlito-fonts = %{version}-%{release}
}
%global fonts             *.ttf
%global fontconfs         %{SOURCE1} %{SOURCE2}
%global fontdescription   %{expand:
Carlito is metric-compatible with Calibri font family. Carlito comes in regular,
bold, italic, and bold italic. The family covers Latin-Greek-Cyrillic (not a
complete set, though) with about 2,000 glyphs. It has the same character
coverage as Calibri. This font is sans-serif typeface family based on Lato.}

Source0:        https://commondatastorage.googleapis.com/chromeos-localmirror/distfiles/crosextrafonts-carlito-20130920.tar.gz
Source1:        30-0-%{fontpkgname}.conf
Source2:        62-%{fontpkgname}.conf

%fontpkg

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n %{archivename}

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.103-0.28.20130920
- Import
