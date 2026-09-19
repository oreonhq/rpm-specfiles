%global source0_hash 32283d9417f1233708dccce244a176aee1cee40b7b030e440cfba8d68fe56b78

# SPDX-License-Identifier: MIT
Version: 1.000
Release: 19%{?dist}

%global foundry           SIL
%global fontlicense       OFL-1.1-RFN
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Shimenkan
%global fontsummary       Shimenkan, a Miao (Pollard) script font family
%global projectname       %{lua:t=string.gsub(rpm.expand("%{fontfamily}"), " SIL$", ""); t=string.gsub(t, "[%p%s]+", ""); print(string.lower(t))}
%global archivename       %{lua:t=string.gsub(rpm.expand("%{fontfamily}"), "[%p%s]+", ""); print(t)}-%{version}
URL:                      https://software.sil.org/%{projectname}/
%global fontpkgheader     %{expand:
Recommends: font(sourcesanspro)
}
%global fonts             *.ttf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
The Shimenkan font family supports the broad variety of writing systems that
use the Miao (Pollard) script. It leverages OpenType features to provide the
correct alternates and positioning for each language. Therefore, making use of
this font requires good OpenType support in applications.

The Latin glyphs are based on the OFL-licensed Source Sans Pro fonts. The Miao
glyphs are designed to harmonize with the Latin, but remain true to the unique
characteristics of Miao writing systems. The project is inspired by, but not
based on, the Miao Unicode project.

Languages that use the Miao script have different positioning and glyphs
shaping conventions. Accessing the correct alternates and positioning for a
given language requires application support for the corresponding OpenType
feature.}

Source0:  https://github.com/silnrsi/font-%{projectname}/releases/download/v%{version}/%{archivename}.tar.xz
Source10: 65-%{fontpkgname}.xml

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
