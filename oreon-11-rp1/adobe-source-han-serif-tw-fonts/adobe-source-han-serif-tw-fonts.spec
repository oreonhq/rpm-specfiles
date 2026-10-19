%global source0_hash 3ed024c37f3d4be42dff0003d7ad71d6e0d92bf8e078dc187400295a20d11042
Version: 2.003R
Release:        1%{?dist}
URL:     https://github.com/adobe-fonts/source-han-serif/
%global foundry           Adobe
%global fontlicense       OFL-1.1
%global fontlicenses      LICENSE.txt
%global fontfamily        Source Han Serif TW
%global fontsummary       Adobe OpenType Pan-CJK font family for Traditional Chinese
%global fonts             SourceHanSerifTW*.otf
%global fontconfs         %{SOURCE10}
%global fontdescription   %{expand:
Source Han Serif is a set of OpenType/CFF Pan-CJK fonts.
}
Source0:        https://github.com/adobe-fonts/source-han-serif/raw/release/SubsetOTF/SourceHanSerifTW.zip
Source10: 65-2-%{fontpkgname}.conf
%fontpkg
# oreon:deps
BuildRequires:  fonts-rpm-macros
# /oreon:deps
%prep
%oreon_prep
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
