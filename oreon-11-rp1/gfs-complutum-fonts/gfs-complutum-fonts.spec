%global source0_hash 913b18fd5fe073a1dc03a2086dd8dea63f5d7d5bacffa27808cfd70ac467f19b

# SPDX-License-Identifier: MIT
Version: 20070413
Release: 49%{?dist}
URL:     http://www.greekfontsociety-gfs.gr/typefaces/16th_century

%global foundry           GFS
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Complutum
%global fontsummary       GFS Complutum, a 16th century Greek font family
%global fonts             *.otf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
The ancient Greek alphabet evolved during the millennium of the Byzantine era
from majuscule to minuscule form and gradually incorporated a wide array of
ligatures, flourishes and other decorative nuances which defined its
extravagant cursive character. Until the late 15th century, typographers who
had to deal with Greek text avoided emulating this complicated hand; instead
they would use only the twenty four letters of the alphabet separately, often
without accents and other diacritics.

A celebrated example is the type cut and cast for the typesetting of the New
Testament in the so-called Complutensian Polyglot Bible (1512), edited by the
Greek scholar, Demetrios Doukas. The type was cut by Arnaldo Guillén de Brocar
and the whole edition was a commission by cardinal Francisco Ximénez, in the
University of Alcalá (Complutum), Spain. It is one of the best and most
representative models of this early tradition in Greek typography which was
revived in the early 20th century by the eminent bibliographer of the British
Library, Richard Proctor. A font named Otter Greek was cut in 1903 and a book
was printed using the new type. The original type had no capitals so Proctor
added his own, which were rather large and ill-fitted. The early death of
Proctor, the big size of the font and the different aesthetic notions of the
time were the reasons that Otter Greek was destined to oblivion, as a
curiosity.

Greek Font Society incorporated Brocar’s famous and distinctive type in the
commemorative edition of Pindar’s Odes for the Athens Olympics (2004) and the
type with a new set of capitals, revived digitally by George D. Matthiopoulos,
is now available for general use.}

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
