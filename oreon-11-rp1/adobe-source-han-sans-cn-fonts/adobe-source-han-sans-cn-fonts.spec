%global source0_hash 6841fc13f1c0d255cfeb33d2a2c68d24bbebd94ae2c070347a2b2b200a1db4d6
Version: 2.004
Release:        1%{?dist}
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
Source0:        https://github.com/adobe-fonts/source-han-sans/releases/download/%{version}R/SourceHanSansCN.zip
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
