%global source0_hash 10e5dc4aef9def319ec42c7e441ff37074009635f4d6ba6759bf9c3f2cc84ca4

# SPDX-License-Identifier: MIT
Version: 6.101
Release: 9%{?dist}

%global foundry           SIL
%global fontlicense       OFL-1.1-RFN
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Andika
%global fontsummary       SIL Andika, a font family for literacy and beginning readers
URL:                      https://software.sil.org/andika
%global fontpkgheader     %{expand:
Suggests: font(andikanewbasic)
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
addresses those issues.}

Source0: https://github.com/silnrsi/font-andika/releases/download/v%{version}/Andika-%{version}.tar.xz
Source10: 61-%{fontpkgname}.xml

%fontpkg -a

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Andika-%{version}
%linuxtext *.txt

%build
%fontbuild -a

%install
%fontinstall -a

%check
%fontcheck -a

%fontfiles -a

%changelog
%autochangelog
