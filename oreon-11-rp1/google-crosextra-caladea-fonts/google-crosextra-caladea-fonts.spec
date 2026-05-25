%global archivename crosextrafonts-20130214

Version:        1.002
Release:        0.22.20130214%{?dist}
Epoch:          1
URL:            http://code.google.com/p/chromium/issues/detail?id=168879

%global foundry           Google Crosextra
# License added in font as "otfinfo -i Caladea-Regular.ttf | grep License"
# also from http://code.google.com/p/chromium/issues/detail?id=280557
%global fontlicense       Apache-2.0
%global fontlicenses      LICENSE-2.0.txt

%global fontfamily        Caladea
%global fontsummary       Serif font metric-compatible with Cambria font

%global fonts             *.ttf
%global fontconfs         %{SOURCE1} %{SOURCE2}
%global fontdescription   %{expand:
Caladea is metric-compatible with Cambria font. This font is a serif
typeface family based on Lato.
}

Source0:        http://gsdview.appspot.com/chromeos-localmirror/distfiles/%{archivename}.tar.gz
Source1:        30-0-%{fontpkgname}.conf
Source2:        62-%{fontpkgname}.conf
Source3:        https://www.apache.org/licenses/LICENSE-2.0.txt

%global fontpkgheader     %{expand:
Obsoletes: ht-caladea-fonts < 1:1.001-10.20200428git336a529
}

%fontpkg

%prep
%autosetup -n %{archivename}
cp -p %{SOURCE3} .

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1:1.002-0.22.20130214
- Import
