%global source0_hash none

Version: 2.015
Release: 25%{?dist}
URL:     http://www.latofonts.com/

%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt
%global fontdocs          README.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Lato
%global fontsummary       A san-serif typeface family
%global fonts             Lato-*.ttf
%global fontconfs         %{SOURCE10}

%global fontdescription   %{expand:
Lato is a sanserif typeface family designed in the Summer 2010 by Warsaw-based
designer Łukasz Dziedzic ("Lato" means "Summer" in Polish). In December 2010 the
Lato family was published under the open-source Open Font License by his foundry
tyPoland, with support from Google.

When working on Lato, Łukasz tried to carefully balance some potentially
conflicting priorities. He wanted to create a typeface that would seem quite
"transparent" when used in body text but would display some original treats when
used in larger sizes. He used classical proportions (particularly visible in the
uppercase) to give the letterforms familiar harmony and elegance. At the same
time, he created a sleek sanserif look, which makes evident the fact that Lato
was designed in 2010 - even though it does not follow any current trend.

The semi-rounded details of the letters give Lato a feeling of warmth, while the
strong structure provides stability and seriousness. "Male and female, serious
but friendly. With the feeling of the Summer," says Łukasz.

Lato consists of nine weights (plus corresponding italics), including a
beautiful hairline style. It covers 2300+ glyphs per style and supports 100+
Latin-based languages, 50+ Cyrillic-based languages as well as Greek and IPA
phonetics.
}

# Fonts retrieved 2015-08-07 from http://www.latofonts.com/download/Lato2OFL.zip
Source0:  %{name}-%{version}.zip
Source10:        https://src.fedoraproject.org/rpms/lato-fonts/raw/rawhide/f/61-lato-fonts.conf

%fontpkg

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Lato2OFL

# Fix wrong end-of-lines encoding
%linuxtext OFL.txt

# Fix permissions
chmod 0644 OFL.txt README.txt

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.015-25
- Import
