%global source0_hash none

# SPDX-License-Identifier: MIT

Version: 2.003
Release: 5%{?dist}
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

Source0:  https://github.com/adobe-fonts/source-han-serif/raw/release/SubsetOTF/SourceHanSerifTW.zip
Source10: 65-2-%{fontpkgname}.conf

%fontpkg

%prep
%autosetup -c

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
%autochangelog
