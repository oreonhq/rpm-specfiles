%global source0_hash none

Version:	20170904
Release:	23%{?dist}
URL:		http://fonts.jp/hanazono/

%global	foundry		hanamin
## https://gitlab.com/fedora/legal/fedora-license-data/-/issues/179#note_1331780205
%global	fontlicense	LicenseRef-Fedora-UltraPermissive OR OFL-1.1-RFN
%global	fontlicenses	LICENSE.txt
%global	fontdocs	README.txt THANKS.txt
%global	fontdocsex	%{fontlicenses}

%global	fontfamily	HanaMin
%global	fontsummary	Japanese Mincho-typeface TrueType font
%global	fontpkgheader	%{expand:
Obsoletes:	hanazono-fonts < %{version}-%{release}
Provides:	hanazono-fonts = %{version}-%{release}
}
%global	fonts0		HanaMin*.ttf
%global	fontconfs0	%{SOURCE1}
%global	fontdescription0	%{expand:
Hanazono Mincho typeface is a Japanese TrueType font that developed with
a support of Grant-in-Aid for Publication of Scientific Research Results from
Japan Society for the Promotion of Science and the International Research
Institute for Zen Buddhism (IRIZ), Hanazono University. also with volunteers
who work together on glyphwiki.org.

This font contains 107518 characters in ISO/IEC 10646 and Unicode Standard,
also supports character sets:
 - 6355 characters in JIS X 0208:1997
 - 5801 characters in JIS X 0212:1990
 - 3695 characters in JIS X 0213:2004
 - 6763 characters in GB 2312-80
 - 13053 characters in Big-5
 - 4888 characters in KS X 1001:1992
 - 360 characters in IBM extensions
 - 9810 characters in IICORE
 - Kanji characters in GB18030-2000
 - Kanji characters in Adobe-Japan1-6
}

Source0:	http://ja.osdn.net/projects/hanazono-font/downloads/68253/hanazono-%{version}.zip
Source1:	66-%{fontpkgname0}.conf

%fontpkg -a

%prep
%setup -q -T -c -a 0

%build
%fontbuild -a
for f in %{fontdocs}; do
  sed -e "s/\\r\$//" $f > $f.tmp && touch -r $f $f.tmp && mv $f.tmp $f
done

%install
%fontinstall -a

%check
%fontcheck -a

%fontfiles -a

%changelog
%autochangelog
