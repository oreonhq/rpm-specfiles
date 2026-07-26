%global source0_hash bf4b24e5e38c7df908ddff1344de732b20c9f3aafd724e112f4315597aaf6be3

# SPDX-License-Identifier: MIT
Version: 1.001
Release: 18%{?dist}

%global foundry           SIL
%global fontlicense       OFL-1.1-RFN
%global fontlicenses      OFL.txt
%global fontdocs          *.txt documentation/*.txt documentation/*.odt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Harmattan
%global fontsummary       Harmattan, a Warsh-style Arabic script font family
%global projectname       %{lua:t=string.gsub(rpm.expand("%{fontfamily}"), " SIL$", ""); t=string.gsub(t, "[%p%s]+", ""); print(string.lower(t))}
%global archivename       %{lua:t=string.gsub(rpm.expand("%{fontfamily}"), "[%p%s]+", ""); print(t)}-%{version}
URL:                      https://software.sil.org/%{projectname}/
%global fontpkgheader     %{expand:
# We blacklist the Andika subset in Harmattan, to use the latest full version
Requires: font(andikanewbasic)
}
%global fonts             *.ttf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Harmattan, named after the trade winds that blow during the dry season in West
Africa, is designed in a Warsh style to suit the needs of languages using the
Arabic script in West Africa.

Because the font style is specifically intended for West Africa, the character
set for this font is aimed at West African languages. Thus, Asia-specific
glyphs are not included.}

Source0:  https://software.sil.org/downloads/r/%{projectname}/%{archivename}.zip
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
