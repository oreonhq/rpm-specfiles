Version: 0.91
Release: 34%{?dist}
URL:     http://guca.sourceforge.net/typography/fonts/saab/

%global fontlicense       GPL-2.0-or-later WITH Font-exception-2.0
%global fontlicenses      License_font_exception.txt

%global fontfamily        Saab
%global fontsummary       Free Punjabi Unicode OpenType Serif Font
%global fonts             Saab.otf
%global fontconfs         %{SOURCE10}
%global fontdescription   %{expand:
This package provides a free OpenType Punjabi (Gurmukhi) Serif font.
Developed by Bhupinder Singh.
}

Source0:  http://downloads.sf.net/guca/saab.0.91.zip
Source10: 67-saab-fonts.conf
#Font file itself does not add exception text, so add it manually
#from http://guca.sourceforge.net/typography/fonts/saab/
Source20: License_font_exception.txt

%fontpkg

%prep
%autosetup -c
cp -p %{SOURCE20} .

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.91-34
- Prepare for Oreon 11 (RP1)
