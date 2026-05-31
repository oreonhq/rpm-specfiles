%global source0_hash none

%global commit0 90abd17b4f97671435798b6147b698aa9087612f

Version:       1.100263
Release:       0.28.20150923git%{?dist}
# cf. https://github.com/googlefonts/robotoslab
URL:           https://fonts.google.com/specimen/Roboto+Slab

%global foundry           google
%global fontlicense       Apache-2.0
%global fontlicenses      LICENSE.txt

%global fontfamily        Roboto Slab
%global fontsummary       Google Roboto Slab fonts
%global fonts             *.ttf
%global fontconfs         %{SOURCE5}
%global fontdescription   %{expand:
Roboto has a dual nature. It has a mechanical skeleton and the forms are
largely geometric. At the same time, the font features friendly and open
curves. While some grotesks distort their letterforms to force a rigid
rhythm, Roboto doesn't compromise, allowing letters to be settled into
their natural width. This makes for a more natural reading rhythm more
commonly found in humanist and serif types.

This is the Roboto Slab family, which can be used alongside the normal
Roboto family and the Roboto Condensed family.}

# There are no tar archive so let's pick all the individual source files from github
Source0:        https://raw.githubusercontent.com/google/fonts/90abd17b4f97671435798b6147b698aa9087612f/apache/robotoslab/RobotoSlab-Regular.ttf
Source1:        https://raw.githubusercontent.com/google/fonts/90abd17b4f97671435798b6147b698aa9087612f/apache/robotoslab/RobotoSlab-Bold.ttf
Source2:        https://raw.githubusercontent.com/google/fonts/90abd17b4f97671435798b6147b698aa9087612f/apache/robotoslab/RobotoSlab-Light.ttf
Source3:        https://raw.githubusercontent.com/google/fonts/90abd17b4f97671435798b6147b698aa9087612f/apache/robotoslab/RobotoSlab-Thin.ttf
Source4:        https://raw.githubusercontent.com/google/fonts/90abd17b4f97671435798b6147b698aa9087612f/apache/robotoslab/LICENSE.txt
Source5:       64-%{fontpkgname}.conf

%fontpkg

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -c -T
cp -p %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} .

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.100263-0.28.20150923git
- Prepare for Oreon 11 (RP1)
