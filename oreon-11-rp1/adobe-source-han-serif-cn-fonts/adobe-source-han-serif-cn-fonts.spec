%global source0_hash e0bcfcb323efa83b5305dbcd5873cc85ad634e15353580ec449103d3763f9a60
Version: 2.003R
Release:        1%{?dist}
URL:     https://github.com/adobe-fonts/source-han-serif/
%global foundry           Adobe
%global fontlicense       OFL-1.1
%global fontlicenses      LICENSE.txt
%global fontfamily        Source Han Serif CN
%global fontsummary       Adobe OpenType Pan-CJK font family for Simplified Chinese
%global fonts             SourceHanSerifCN*.otf
%global fontconfs         %{SOURCE10}
%global fontdescription   %{expand:
Source Han Serif is a set of OpenType/CFF Pan-CJK fonts.
}
Source0:        https://github.com/adobe-fonts/source-han-serif/raw/release/SubsetOTF/SourceHanSerifCN.zip
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
