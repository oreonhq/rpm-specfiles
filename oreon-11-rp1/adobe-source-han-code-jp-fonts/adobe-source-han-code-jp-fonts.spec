%global source0_hash 0f98beb0a381d9d19067f9b58f65d2dd65c808a3012ac9cb9866e575ad6d2e7f
Version: 2.011
Release:        1%{?dist}
URL:     https://github.com/adobe-fonts/source-han-code-jp/
%global foundry           adobe
%global fontlicense       OFL-1.1
%global fontlicenses      LICENSE.txt
%global fontdocs          relnotes.txt README.md README-JP.md
%global fontdocsex        %{fontlicenses}
%global fontfamily        Source Han Code JP
%global fontsummary       Adobe OpenType UI font for mixed Latin and Japanese text
%global fonts             OTF/SourceHanCodeJP-RegularIt.otf OTF/SourceHanCodeJP-Regular.otf OTF/SourceHanCodeJP-NormalIt.otf OTF/SourceHanCodeJP-Normal.otf OTF/SourceHanCodeJP-MediumIt.otf OTF/SourceHanCodeJP-Medium.otf OTF/SourceHanCodeJP-LightIt.otf OTF/SourceHanCodeJP-Light.otf OTF/SourceHanCodeJP-HeavyIt.otf OTF/SourceHanCodeJP-Heavy.otf OTF/SourceHanCodeJP-ExtraLightIt.otf OTF/SourceHanCodeJP-ExtraLight.otf OTF/SourceHanCodeJP-BoldIt.otf OTF/SourceHanCodeJP-Bold.otf
%global fontconfs         %{SOURCE10}
%global fontdescription   %{expand:
Source Han Code JP is a derivative of Source Han Sans that replaces
its proportional Latin glyphs with fixed-width 667-unit glyphs from
Source Code Pro. The Latin glyphs are scaled to match the glyphs for
Japanese kana and kanji, and their widths are adjusted to be exactly
667 units (two-thirds of an EM). Source Han Code JP is intended to be
used as a UI font for mixed Latin and Japanese text on displays,
for programming, editing HTML/CSS, viewing text or inputing to
the command line in a terminal app, and so on.
}
Source0:        https://github.com/adobe-fonts/source-han-code-jp/archive/2.011R/source-han-code-jp-2.011R.zip
Source10: 68-adobe-source-han-code-jp-fonts.conf
%fontpkg
# oreon:deps
BuildRequires:  fonts-rpm-macros
# /oreon:deps
%prep

%setup -q -n source-han-code-jp-%{version}R
chmod 0644 README.md README-JP.md

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

%autochangelog
