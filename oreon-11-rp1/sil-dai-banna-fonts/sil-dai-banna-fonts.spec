%global source0_hash bab67e560484ee9bc041d1e95ae2e36a08ceb9cde6800ef032381fae0700f691

# SPDX-License-Identifier: MIT
Version: 2.200
Release: 19%{?dist}

%global foundry           SIL
%global fontlicense       OFL-1.1-RFN
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Dai Banna SIL
%global fontsummary       Dai Banna SIL, a font family for rendering New Tai Lue (Xishuangbanna Dai)
%global projectname       %{lua:t=string.gsub(rpm.expand("%{fontfamily}"), " SIL$", ""); t=string.gsub(t, "[%p%s]+", ""); print(string.lower(t))}
%global archivename       %{lua:t=string.gsub(rpm.expand("%{fontfamily}"), " SIL$", ""); t=string.gsub(t, "[%p%s]+", ""); print(t)}-%{version}
URL:                      https://software.sil.org/%{projectname}/
%global fonts             *.ttf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Dai Banna includes a complete set of New Tai Lue (Xishuangbanna Dai)
consonants, vowels, tones, and digits, along with punctuation and other useful
symbols. A basic set of Latin glyphs, including Arabic numerals, is also
provided.

The New Tai Lue script is used by approximately 300 000 people who speak the
Xishuangbanna Dai language in Yunnan, China.  It is a simplification of the Tai
Tham (Old Tai Lue) script as used for this language for hundreds of years.

The Dai News Department of Xishuangbanna Daily provided valuable advice during
the development of this font family. Xishuangbanna Daily, established in 1957,
is the largest newspaper company in Yunnan, China that publishes in the New Tai
Lue script.}

Source0:  https://software.sil.org/downloads/r/%{projectname}/%{archivename}.zip
Source10: 65-%{fontpkgname}.xml

%fontpkg

%package doc
Summary:   Optional documentation files of %{name}
BuildArch: noarch
%description doc
This package provides optional documentation files shipped with
%{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n dai-banna-%{version}
%linuxtext *.txt doc/*.txt

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
%doc doc/*.pdf doc/*.txt

%changelog
%autochangelog
