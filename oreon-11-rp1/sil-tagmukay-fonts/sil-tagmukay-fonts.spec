%global source0_hash 0ac09c04f3907324a24135d73036975cde7f2df4c22c8024b50dbec9e2142704

# SPDX-License-Identifier: MIT
Version: 2.000
Release: 20%{?dist}

%global foundry           SIL
%global fontlicense       OFL-1.1-RFN
%global fontlicenses      OFL.txt
%global fontdocs          *.txt documentation/*.txt documentation/*.odt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Tagmukay
%global fontsummary       Tagmukay, a Shifinagh font that supports the Tawallammat dialect of Tamajaq
%global projectname       %{lua:t=string.gsub(rpm.expand("%{fontfamily}"), " SIL$", ""); t=string.gsub(t, "[%p%s]+", ""); print(string.lower(t))}
%global archivename       %{lua:t=string.gsub(rpm.expand("%{fontfamily}"), "[%p%s]+", ""); print(t)}-%{version}
URL:                      https://software.sil.org/%{projectname}/
%global fonts             *.ttf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Tagmukay is a Shifinagh script font with support for the Tawallammat Tamajaq
language. The script name is more commonly spelled Tifinagh, but Shifinagh is
the preferred spelling in the region where Tawallammat Tamajaq is spoken.

Tawallammat Tamajaq, when written in the Shifinagh script, follows the
traditional “consonant only” way of writing this ancient script. The Tagmukay
font family has these consonants and also the logic needed to form the
bi-consonant ligatures needed to distinguish between vocalic and non-vocalic
consonant clusters.}

Source0:  https://github.com/silnrsi/font-%{projectname}/releases/download/v%{version}/%{archivename}.tar.xz
Source10: 65-%{fontpkgname}.xml

%fontpkg

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{archivename}
%linuxtext *.txt documentation/*.txt
chmod 644 %{fontdocs} %{fontlicenses}

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
%autochangelog
