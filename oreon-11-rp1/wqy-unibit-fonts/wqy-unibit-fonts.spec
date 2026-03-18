# SPDX-License-Identifier: MIT

%global fontname wqy-unibit

BuildRequires:  make
BuildRequires:  bdftopcf
BuildRequires:  perl-interpreter

Version: 1.1.0
Release: 40%{?dist}
URL:     http://wenq.org/enindex.cgi

%global foundry           WQY
%global fontlicense       GPL-2.0-only WITH Font-exception-2.0
%global fontlicenses      COPYING
%global fontdocs          AUTHORS ChangeLog README

%global fontfamily        Unibit
%global fontsummary       WenQuanYi Unibit Bitmap Font
%global fonts             *.pcf
%global fontdescription   %{expand:
The Wen Quan Yi Unibit is designed as a dual-width (16x16,16x8) 
bitmap font to provide the most complete international symbol 
coverage, serving as the system-wide fall-back font. This font 
has covered over 46000 Unicode code points in BMP.
It is intended to supersede the outdated GNU Unifont.
This font was created by merging the latest update of GNU 
Unifont [GPL] (by Roman Czyborra and David Starner et al., the 
font was last updated in 2004), WenQuanYi Bitmap Song [GPL] 
0.8.1 (by Qianqian Fang and WenQuanYi contributors) and 
Fixed-16x8 [public domain] bitmap fonts from X11 core fonts. 
The entire CJK Unified Ideographics (U4E00-U9FA5) and CJK Unified 
Ideographics Extension A(U3400-U4DB5) blocks were replaced by 
high-quality glyphs from China National Standard GB19966-2005 
(public domain). Near a thousand of non-CJK characters were improved by 
WenQuanYi contributors via their collaborative font editing website at
http://wenq.org/eindex.cgi?Unicode_Chart_EN

}

Source0:  http://downloads.sourceforge.net/wqy/wqy-unibit-bdf-%{version}-1.tar.gz
Patch0:   wqy-unibit-fixes-build.patch

%fontpkg

%prep
%autosetup -n %{fontname}


%build
make
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.0-40
- Prepare for Oreon 11 (RP1)
