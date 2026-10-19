%global source4_hash cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30
%global source3_hash 4e2f26097538925162cad2a3e6051f659b9895386559a1890a4664d8e9a9a0c1
%global source2_hash 153bf5b428d5cd0b27a63f9a36941cd7d6c7523a7afd59c76a12f798e4c33127
%global source1_hash ba12d2eab1fa765b6b05398fa7e047dd76293f0c051ce57a8f7b0c591c14d42b
%global source0_hash 13aa5f54c6f2fa2e388fe0e675cdbcc6a81f6270a8bf9c03a5df8af9cb022810
%global commit0 90abd17b4f97671435798b6147b698aa9087612f
Version:       1.100263
Release:        1%{?dist}
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
Source0:        https://raw.githubusercontent.com/google/fonts/90abd17b4f97671435798b6147b698aa9087612f/apache/robotoslab/RobotoSlab-Regular.ttf
Source1:        https://raw.githubusercontent.com/google/fonts/90abd17b4f97671435798b6147b698aa9087612f/apache/robotoslab/RobotoSlab-Bold.ttf
Source2:        https://raw.githubusercontent.com/google/fonts/90abd17b4f97671435798b6147b698aa9087612f/apache/robotoslab/RobotoSlab-Light.ttf
Source3:        https://raw.githubusercontent.com/google/fonts/90abd17b4f97671435798b6147b698aa9087612f/apache/robotoslab/RobotoSlab-Thin.ttf
Source4:        https://raw.githubusercontent.com/google/fonts/90abd17b4f97671435798b6147b698aa9087612f/apache/robotoslab/LICENSE.txt
Source5:       64-%{fontpkgname}.conf
%fontpkg
# oreon:deps
BuildRequires:  fonts-rpm-macros
# /oreon:deps
%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -c -T
cp -p %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} .

%build

%fontbuild
%install
%fontinstall
%oreon_autofiles main

%check

%fontcheck
%fontfiles
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.100263-0.28.20150923git
- Prepare for Oreon 11 (RP1)
