%global source0_hash 280c2e42ad704cc899b6535b63ead980ed5b6f781fc718ae80eba9f8f3236d0c
Version: 1.001
Release:        1%{?dist}
URL:     https://github.com/adobe-fonts/source-han-serif/
%global foundry           adobe
%global fontlicense       OFL-1.1
%global fontlicenses      LICENSE.txt
%global fontdocs          %{nil}
%global fontdocsex        %{fontlicenses}
%global fontfamily        Source Han Serif JP
%global fontsummary       Adobe OpenType Pan-CJK font family for Japanese
%global fonts             SourceHanSerifJP-SemiBold.otf SourceHanSerifJP-Regular.otf SourceHanSerifJP-Medium.otf SourceHanSerifJP-Light.otf SourceHanSerifJP-Heavy.otf SourceHanSerifJP-ExtraLight.otf SourceHanSerifJP-Bold.otf
%global fontconfs         %{SOURCE10}
%global fontdescription   %{expand:
Source Han Serif is a set of OpenType/CFF Pan-CJK fonts.
}
Source0:        https://github.com/adobe-fonts/source-han-serif/raw/release/SubsetOTF/SourceHanSerifJP.zip
Source10: 68-adobe-source-han-serif-jp-fonts.conf
%fontpkg
# oreon:deps
BuildRequires:  fonts-rpm-macros
# /oreon:deps
%prep

%setup -q -n SourceHanSerifJP

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
