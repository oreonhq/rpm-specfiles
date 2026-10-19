%global source0_hash 9604c77067396b4d2ab49816b3e18db741a70c8b1d43eb28669ae75cd1ce5237
%global archivever 00401
Version: 004.01
Release:        1%{?dist}
URL:     https://moji.or.jp/ipafont/
%global foundry           IPA 
%global fontlicense       IPA
%global fontlicenses      IPA_Font_License_Agreement_v1.0.txt
%global fontdocs          Readme_ipaexm00401.txt
%global fontdocsex        %{fontlicenses}
%global fontfamily        IPAexMincho
%global fontsummary       Japanese Mincho-typeface OpenType font by IPA
%global fontpkgheader     %{expand:
Obsoletes: ipa-ex-mincho-fonts < %{version}-%{release}
Provides:  ipa-ex-mincho-fonts = %{version}-%{release}
}
%global fonts             ipaexm.ttf
%global fontconfs         %{SOURCE10}
%global fontdescription   %{expand:
IPAex Font is a Japanese OpenType fonts that is JIS X 0213:2004
compliant, provided by Information-technology Promotion Agency, Japan.
This package contains Mincho style font.
}
Source0:        https://moji.or.jp/wp-content/ipafont/%{foundry}exfont/ipaexm%{archivever}.zip
Source10: 68-ipa-exmincho-fonts.conf
%fontpkg
# oreon:deps
BuildRequires:  fonts-rpm-macros
# /oreon:deps
%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n ipaexm%{archivever}
chmod 0644 Readme_ipaexm%{archivever}.txt
sed -ie 's/\r//g' Readme_ipaexm%{archivever}.txt

%build

%fontbuild
%install
%fontinstall
%oreon_autofiles main

%check

%fontcheck
%fontfiles
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
