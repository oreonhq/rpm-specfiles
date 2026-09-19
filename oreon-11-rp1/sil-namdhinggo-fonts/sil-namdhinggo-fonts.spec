%global source0_hash 8bd69ee93687f2b3fcb705b0c8867c8ff573edcaf9a5c51a08a8ca1c1ddc966b

# SPDX-License-Identifier: MIT
Version: 1.004
Release: 19%{?dist}

%global foundry           SIL
%global fontlicense       OFL-1.1-RFN
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Namdhinggo SIL
%global fontsummary       Namdhinggo SIL, a font family for the Limbu writing system of Nepal
%global projectname       %{lua:t=string.gsub(rpm.expand("%{fontfamily}"), " SIL$", ""); t=string.gsub(t, "[%p%s]+", ""); print(string.lower(t))}
%global archivename       %{lua:t=string.gsub(rpm.expand("%{fontfamily}"), "[%p%s]+", ""); print(t)}-%{version}
URL:                      https://software.sil.org/%{projectname}/
%global fonts             *.ttf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Namdhinggo provides glyphs for all Limbu characters and some Latin.

The Limbu, or Kirat Sirijonga, script is used by around 400 000 people in Nepal
and India. This Unicode-encoded font has been designed to support literacy and
materials development in the Limbu language.

According to traditional histories the Limbu script was developed by King
Sirijonga in the 9th Century. It then fell out of use before being reintroduced
in the 18th century by Teongsi Sirijonga (1704-1741) whom many felt to be the
reincarnation of the first Sirijonga. The modern Sirijonga was apparently
martyred in 1741 for the sake of this script by lamas in Sikkim. The script was
named ‘Sirijonga’ in his honor by the Limbu scholar Iman Singh Chemjong.}

Source0:  https://software.sil.org/downloads/r/%{projectname}/%{archivename}.zip
Source10: 66-%{fontpkgname}.xml

%fontpkg

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n NamdhinggoSIL
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
