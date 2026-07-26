%global source0_hash 0d8e3143b9c46c97916ab2cf85ae2187fe33b9b40859567a5524266dd58581bc

# SPDX-License-Identifier: MIT
Version: 1.0
Release: 19%{?dist}

%global foundry           SIL
%global fontlicense       OFL-1.1-RFN
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Apparatus SIL
%global fontsummary       Apparatus SIL, a font family for rendering Greek & Hebrew biblical texts
%global archivename       %{lua:t=string.gsub(rpm.expand("%{fontfamily}"), "[%p%s]+", "");print(t)}
%global projectname       %{archivename}
URL:                      https://scripts.sil.org/ApparatusSIL
%global fonts             *.ttf *.TTF
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
The Apparatus SIL font family was designed to provide most of the symbols
needed to reproduce the textual apparatus found in major editions of Greek &
Hebrew biblical texts. It is based on SIL Charis, a font family designed for
optimum clarity and compactness when printed at small point sizes. This assures
that both Charis SIL and Apparatus SIL can be used together in documents with a
consistency of style.

Most lines of text in the apparatus can be reproduced by combining the Greek
and Hebrew fonts, transliteration (using a font such as Charis SIL), and the
Apparatus SIL font.}

Source0:  https://scripts.sil.org/cms/scripts/render_download.php?format=file&media_id=AppSIL%{version}.zip&filename=%{archivename}.zip#/%{archivename}.zip
Source10: 60-%{fontpkgname}.xml

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
