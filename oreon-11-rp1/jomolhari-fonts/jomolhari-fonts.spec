Version:        0.003
Release:        45%{?dist}

URL: https://fonts.google.com/specimen/Jomolhari

%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Jomolhari
%global fontsummary       Jomolhari a Bhutanese style font for Tibetan and Dzongkha
%global archivename       jomolhari-alpha003c
%global fonts             *.ttf
%global fontconfs         %{SOURCE1}
%global fontdescription   %{expand:
Jomolhari is an TrueType OpenType Bhutanese style font for Dzongkha and
Tibetan text. It is based on Bhutanese manuscript examples, supports the
Unicode and the Chinese encoding for Tibetan.
The font supports the standard combinations used in most texts.}

Source0: http://chris.fynn.googlepages.com/%{archivename}.zip
Source1:        65-0-%{fontpkgname}.conf 

%fontpkg

%prep
%setup -q -c
%linuxtext FONTLOG.txt OFL-FAQ.txt OFL.txt

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.003-45
- Prepare for Oreon 11 (RP1)
