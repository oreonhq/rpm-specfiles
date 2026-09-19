%global source0_hash d1c4748b712cd43f3fd30f8a6a34ee362d102912e900c82f04380206ae7b9b5f

# SPDX-License-Identifier: MIT
Version: 1.0
Release: 19%{?dist}

%global foundry           SIL
%global fontlicense       OFL-1.1-RFN
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Sophia Nubian
%global fontsummary       Sophia Nubian, a font family for Nubian languages which use the Coptic script
%global projectname       %{lua:t=string.gsub(rpm.expand("%{fontfamily}"), " SIL$", ""); t=string.gsub(t, "[%p%s]+", ""); print(string.lower(t))}
%global archivename       SN%{version}
URL:                      https://software.sil.org/%{projectname}/
%global fonts             *.ttf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Sophia Nubian is a sans serif font family based on SIL Sophia. Its primary
purpose is to provide adequate representation for Nubian languages which use
the Coptic script. Since Nubian languages do not use casing, uppercase
characters are not included in this font. A basic set of Latin glyphs is also
provided.}

Source0:  https://scripts.sil.org/cms/scripts/render_download.php?format=file&media_id=%{archivename}.zip&filename=%{archivename}.zip#/%{archivename}.zip
Source10: 65-%{fontpkgname}.xml

%fontpkg

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c -T
unzip -j -q %{SOURCE0}
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
