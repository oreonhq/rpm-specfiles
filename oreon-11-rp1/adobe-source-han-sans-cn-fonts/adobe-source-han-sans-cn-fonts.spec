%global source0_hash none

# SPDX-License-Identifier: MIT

Version: 2.004
Release: 13%{?dist}
URL:     https://github.com/adobe-fonts/source-han-sans/

%global foundry           Adobe
%global fontlicense       OFL-1.1-RFN
%global fontlicenses      LICENSE.txt

%global fontfamily        Source Han Sans CN
%global fontsummary       Adobe OpenType Pan-CJK font family for Simplified Chinese
%global fonts             SubsetOTF/CN/SourceHanSansCN*.otf
%global fontconfs         %{SOURCE10}
%global fontdescription   %{expand:
Source Han Sans is a sans serif Pan-CJK font family 
that is offered in seven weights—ExtraLight, Light, 
Normal, Regular, Medium, Bold, and Heavy—and 
in several OpenType/CFF-based deployment configurations
to accommodate various system requirements or limitations.

As the name suggests, Pan-CJK fonts are intended to
support the characters necessary to render or
display text in Simplified Chinese, Traditional Chinese,
Japanese, and Korean.
}

Source0:  https://github.com/adobe-fonts/source-han-sans/releases/download/%{version}R/SourceHanSansCN.zip
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
