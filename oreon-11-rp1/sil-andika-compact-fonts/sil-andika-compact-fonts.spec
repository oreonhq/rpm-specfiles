%global source0_hash 047d7abc6a12abf83fe0e62177e835434392c3c6d79e46433bc610fda05e0331

# SPDX-License-Identifier: MIT
Version: 5.000
Release: 19%{?dist}

%global foundry           SIL
%global fontlicense       OFL-1.1-RFN
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Andika Compact
%global fontsummary       SIL Andika Compact, a font family for literacy and beginning readers
%global projectname       andika
%global archivename       %{lua:t=string.gsub(rpm.expand("%{fontfamily}"), "[%p%s]+", ""); print(t)}-%{version}
URL:                      https://software.sil.org/%{projectname}/
%global fontpkgheader     %{expand:
Suggests: font(andika)
}
%global fonts             *.ttf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Andika is a sans serif, Unicode-compliant font family designed especially for
literacy use, taking into account the needs of beginning readers. The focus is
on clear, easy-to-perceive letter-forms that will not be readily confused with
one another.

A sans serif font is preferred by some literacy personnel for teaching people
to read. Its forms are simpler and less cluttered than those of most serif
fonts. For years, literacy workers have had to make do with fonts that were
not really suitable for beginning readers and writers. In some cases, literacy
specialists have had to tediously assemble letters from a variety of fonts in
order to get all of the characters they need for their particular language
project, resulting in confusing and unattractive publications. Andika
addresses those issues.

The Andika Compact font family was derived from Andika using SIL TypeTuner,
by setting the “Line spacing” feature to “Tight”, and it cannot be TypeTuned
again. It may exhibit some diacritics clipping on screen (but should print
fine).}

Source0:  https://software.sil.org/downloads/r/%{projectname}/%{archivename}.zip
Source10: 62-%{fontpkgname}.xml

%fontpkg

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{archivename}
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
