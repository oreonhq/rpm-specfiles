%global source1_hash e44ab0daf1a4e0c71d141fec66a09d157edee00b1a24f441425e2dbb824d5018
%global source0_hash d3866120498c496931265a7b199dc0a54f44330170dde1178bb982fffcc6bb52
Version: 1.001
Release:        6%{?dist}
URL:     https://carrois.com/fira/
%global version_nodots %{gsub %{version} %. %{quote:}}
%global foundry           BBOX
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt
%global fontfamily        FiraGO
%global fontsummary       An independent Open Source typeface
%global fonts             Fonts/FiraGO_OTF_%{version_nodots}/*/*.otf
%global fontconfs         %{SOURCE2}
%global fontdescription   %{expand:
Based on the Fira Sans 4.3 glyph set, FiraGO now supports Arabic, Devanagari,
Georgian, Hebrew and Thai. With this script support, FiraGO catches up with
other globally extended and free typefaces such as Noto.
}
Source0:        https://carrois.com/downloads/%{fontfamily}/Download_Folder_%{fontfamily}_1001.zip
Source1:  https://carrois.com/downloads/FiraGO/OFL.txt
Source2:  60-%{fontpkgname}.conf
%fontpkg
# oreon:deps
BuildRequires:  fonts-rpm-macros
# /oreon:deps
%prep

%autosetup -n Download_Folder_FiraGO_%{version_nodots} -a 0
cp %{SOURCE1} .

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
