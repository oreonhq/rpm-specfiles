%global source0_hash 11d78c8fbc1a4bb04a453cdd65c99db8d41ec5cd6ba6d68c8638e6ba170de806
Version: 2.004
Release:        1%{?dist}
URL:     https://github.com/adobe-fonts/source-han-sans/
%global foundry           Adobe
%global fontlicense       OFL-1.1-RFN
%global fontlicenses      LICENSE.txt
%global fontfamily        Source Han Sans TW
%global fontsummary       Adobe OpenType Pan-CJK font family for Traditional Chinese
%global fonts             SubsetOTF/TW/SourceHanSansTW*.otf
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
Source0:        https://github.com/adobe-fonts/source-han-sans/releases/download/%{version}R/SourceHanSansTW.zip
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
