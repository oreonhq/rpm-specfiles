%global source1_hash f7c2c3b012e870077ef159890f614f83bb430bfd7dde0a77d978ea1e6a677236
%global source0_hash a5b6d8ab3d098796ef93178b5a384419738f3ac573b6943b2dc11500347be973
Version: 1.00
Release:        1%{?dist}
URL:     https://www.businesswire.com/news/home/20100608005491/en/Monotype-Imaging-Contributes-Simplified-Chinese-Font-%E2%80%9CMYuppy%E2%80%9D
%global foundry           Symbian
%global fontlicense       EPL-1.0
%global fontlicenses      *.TXT
%global fontfamily        M Yuppy GB
%global fontsummary       M Yuppy GB, a Chinese font family with a unique, modern feel
%global fonts             %{SOURCE0}
%global fontconfngs       %{SOURCE2}
%global fontdescription   %{expand:
Designed to appeal to young urban professionals, M Yuppy is a font family with
a unique, modern feel. The design combines elements of handwriting with classic
letter-form characteristics, such as open shapes and proper proportions that
help the typeface retain legibility.}
Source0:        https://raw.githubusercontent.com/SymbianSource/oss.FCL.sf.os.textandloc/59666d6704fee305b0fdd74974f7b4f42659c6a6/fontservices/referencefonts/truetype/MYuppyGB-Medium.ttf
Source1: https://raw.githubusercontent.com/SymbianSource/oss.FCL.sf.os.textandloc/59666d6704fee305b0fdd74974f7b4f42659c6a6/fontservices/referencefonts/truetype/MYuppyGB-Medium_README.TXT
Source2: 65-%{fontpkgname}.xml
%fontpkg
# oreon:deps
BuildRequires:  fonts-rpm-macros
# /oreon:deps
%prep

%setup -q -c -T
cp %{SOURCE1} .
%linuxtext *TXT

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
