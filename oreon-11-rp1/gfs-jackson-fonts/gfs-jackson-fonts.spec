%global source0_hash 688626f59f463d17f2da341f33146ae213563a45cc3bc29bdf415c0f8f77d6d9

# SPDX-License-Identifier: MIT
Version: 20080303
Release: 41%{?dist}
URL:     http://www.greekfontsociety-gfs.gr/typefaces/majuscule

%global foundry           GFS
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Jackson
%global fontsummary       GFS Jackson, a majuscule Greek font family
%global fonts             *.otf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
As it is known, the Greek alphabet was used in majuscule form for over a
millennium before the minuscule letters gradually replaced it until they became
the official script in the 9th century A.D. Thereafter, majuscule letters were
confined to sparse use as initials or elaborate titles until the Italian
Renaissance.

The new art of Typography, as well as the need of the humanists to mimic the
ancient Greco-Roman period brought back the extensive use of the majuscule
letter-forms in both Latin and Greek typography. Greek books of the time were
printed using the contemporary Byzantine hand with which they combined capital
letters modeled on the Roman antiquity, i.e. with thick and thin strokes and
serifs. At the same time the Byzantine majuscule tradition, principally used on
theological editions, remained alive until the early 19th century.

GFS Jackson is an edition of the font cut, in 1788, by Joseph Jackson on
commission by the Cambridge University in preparation of the edition of the
Beza codex containing the New Testament from the 5th-6th century. Theodore
Beza was the erudite scholar from Geneva who had given the codex as a gift to
the University in 1581.

It has been designed by George D. Matthiopoulos.}

%global archivename %{lua:t=string.gsub(rpm.expand("%{foundry} %{fontfamily}"), "[%p%s]+", "_");print(t)}

Source0:  http://www.greekfontsociety-gfs.gr/_assets/fonts/%{archivename}.zip
Source10: 61-%{fontpkgname}.xml

%fontpkg

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

%changelog
%autochangelog
