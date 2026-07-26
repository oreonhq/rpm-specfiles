%global source0_hash 2c824e6919bf3fbfd097b088f1b3e7fd3bc903360d80169b82b7ecf595160b39

# SPDX-License-Identifier: MIT
Version: 20071114
Release: 47%{?dist}
URL:     http://www.greekfontsociety-gfs.gr/typefaces/19th_century

%global foundry           GFS
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Solomos
%global fontsummary       GFS Solomos, a 19th century italic Greek font family
%global fonts             *.otf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
From the middle of the 19th century an italic font with many calligraphic
overtones was introduced into Greek printing. Its source is unknown, but it
almost certainly was the product of a German or Italian foundry. In the first
type specimen printed in Greece by the type cutter K. Miliadis (1850), the font
was listed anonymously along others of 11pts and in the Gr. Doumas’ undated
specimen appeared as “11pt Greek inclined”. For most of the second half of the
century the type was used extensively as an italic for emphasis in words,
sentences or excerpts. In 1889, the folio size Type Specimen of Anestis
Konstantinidis’ publishing, printing and type founding establishment also
included the type as “Greek inclined [9 & 12 pt]”.

Nevertheless, the excessively calligraphic style of the characters, combined
with the steep and uncomfortable obliqueness of the capitals, was out of
favor in the 20th century and the type did not survive the conformity of the
mechanical type cutting and casting.

The font has been digitally revived, as part of our typographic tradition, by
George D. Matthiopoulos and is part of GFS’ type library under the name GFS
Solomos, in commemoration of the great Greek poet of the 19th century,
Dionisios Solomos.}

%global archivename %{lua:t=string.gsub(rpm.expand("%{foundry} %{fontfamily}"), "[%p%s]+", "_");print(t)}

Source0:  http://www.greekfontsociety-gfs.gr/_assets/fonts/%{archivename}.zip
Source10: 61-%{fontpkgname}.xml

%fontpkg

%package doc
Summary:   Optional documentation files of %{name}
BuildArch: noarch
%description doc
This package provides optional documentation files shipped with
%{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c -T
unzip -j -q  %{SOURCE0}
%linuxtext *.txt

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%files doc
%defattr(644, root, root, 0755)
%license OFL.txt
%doc *.pdf

%changelog
%autochangelog
