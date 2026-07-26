%global source0_hash 35d3abbdc4756ed73371aadb5907f8d38457da374c9ee380cef771b9141c4b80

# SPDX-License-Identifier: MIT
Version: 2.000
Release: 18%{?dist}

%global foundry           SIL
%global fontlicense       OFL-1.1-RFN
%global fontlicenses      OFL.txt
%global fontdocs          *.txt documentation/*.txt documentation/*.odt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Awami Nastaliq
%global fontsummary       Awami Nastaliq, a Nastaliq-style Arabic script font family
%global projectname       awami
%global archivename       %{lua:t=string.gsub(rpm.expand("%{fontfamily}"), "[%p%s]+", ""); print(t)}-%{version}
URL:                      https://software.sil.org/%{projectname}/
%global fontpkgheader     %{expand:
Recommends: font(charissil)
}
%global fonts             *.ttf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Awami Nastaliq is a Nastaliq-style Arabic script font family supporting a wide
variety of languages of southwest Asia, including but not limited to Urdu. This
font is aimed at minority language support. This makes it unique among Nastaliq
fonts.

Nastaliq, based on a centuries-old calligraphic tradition, is considered one of
the most beautiful scripts on the planet. Nastaliq has been called “the bride
of calligraphy” but its complexity also makes it one of the most difficult
scripts to render using a computer font. Its right-to-left direction, vertical
nature, and context-specific shaping provide a challenge to any font rendering
engine and make it much more difficult to render than the flat (Naskh) Arabic
script that it is based on. As a result, font developers have long struggled to
produce a font with the correct shaping but at the same time avoid overlapping
of dots and diacritics. In order to account for the seemingly infinite
variations, the Graphite rendering engine has been extended just to handle
these complexities properly.}

Source0:  https://github.com/silnrsi/font-%{projectname}/releases/download/v%{version}/%{archivename}.tar.xz
Source10: 65-%{fontpkgname}.xml

%fontpkg

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{archivename}
%linuxtext *.txt documentation/*.txt

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
%autochangelog
