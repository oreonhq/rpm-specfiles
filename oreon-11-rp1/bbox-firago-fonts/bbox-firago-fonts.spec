%global source0_hash none

Version: 1.001
Release: 6%{?dist}
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

Source0:  https://carrois.com/downloads/FiraGO/Download_Folder_FiraGO_%{version_nodots}.zip
Source1:  https://carrois.com/downloads/FiraGO/OFL.txt
Source2:  60-%{fontpkgname}.conf

%fontpkg

%prep
%autosetup -n Download_Folder_FiraGO_%{version_nodots} -a 0
cp %{SOURCE1} .

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
%autochangelog
