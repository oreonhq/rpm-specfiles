%global source0_hash 3c62982f57e7e93f1e494f207054c6c4713e7bc9959ee4eb738e5f9fb98b80d2

Version:        1.100
Release:        10%{?dist}
URL:            https://software.sil.org/mingzat/
BuildRequires:  fonts-rpm-macros

%global foundry         SIL
%global fontlicense     OFL-1.1
%global fontlicenses    OFL.txt OFL-FAQ.txt
%global fontdocs        *.txt
%global fontdocsex      %{fontlicenses}

%global fontfamily      Mingzat
%global fontsummary     A font for Lepcha script
%global fonts           *.ttf
%global fontconfs       %{SOURCE10}
%global fontdescription %{expand:
Mingzat is based on Jason Glavy's JG Lepcha font which was a custom-encoded
font. The goal for this product was to provide a single Unicode-based font
that would contain all Lepcha characters. In addition, there is provision for
other Latin characters and symbols. This font makes use of state-of-the-art
font technologies (Graphite and OpenType) to support the need for conjuncts
and to position arbitrary combinations of Lepcha glyphs and combining marks
optimally.}

# Licenses
# Mingzat-Regular.ttf:  OFL
# OFL.txt:      OFL and OFL text
# OFL-FAQ.txt:  No-modification. Handle it as an extension of OFL text so that
#               we can distribute it.
# org.fedoraproject.sil-mingzat-fonts.metainfo.xml: MIT # bug #2089366
# README.txt:   OFL
## Not in any binary package
# web/Mingzat-Regular.woff:         OFL
# web/Mingzat-Regular.woff2:        OFL
# web/Mingzat-webfont-example.css:  OFL
Source0:    https://software.sil.org/downloads/r/mingzat/%{fontfamily}-%{version}.zip
Source10:   65-sil-mingzat.conf

%fontpkg

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{fontfamily}-%{version}
%linuxtext -n *.txt

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
%autochangelog
