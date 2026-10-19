%global source0_hash c49742155ff7d1d9b9bf295f9473edfd4a01fd1cb72d135f4324cc98b5cb315e
Version: 1.001
Release:        1%{?dist}
URL:     https://github.com/adobe-fonts/source-han-serif/
%global foundry           adobe
%global fontlicense       OFL-1.1
%global fontlicenses      LICENSE.txt
%global fontdocs          %{nil}
%global fontdocsex        %{fontlicenses}
%global fontfamily        Source Han Serif KR
%global fontsummary       Adobe OpenType Pan-CJK font family for Korean
%global fonts             SourceHanSerifKR-SemiBold.otf SourceHanSerifKR-Regular.otf SourceHanSerifKR-Medium.otf SourceHanSerifKR-Light.otf SourceHanSerifKR-Heavy.otf SourceHanSerifKR-ExtraLight.otf SourceHanSerifKR-Bold.otf
%global fontconfs         %{SOURCE10}
%global fontdescription   %{expand:
Source Han Serif is a set of OpenType/CFF Pan-CJK fonts.
}
Source0:        https://github.com/adobe-fonts/source-han-serif/raw/release/SubsetOTF/SourceHanSerifKR.zip
Source10: 68-adobe-source-han-serif-kr-fonts.conf
%fontpkg
# oreon:deps
BuildRequires:  fonts-rpm-macros
# /oreon:deps
%prep

%setup -q -n SourceHanSerifKR

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
