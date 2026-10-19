%global source0_hash 4ab6fee94bf6f94b3eeb31be2b73c559f738dc6b336d722d5301b1f3f592f850
%global archivever 00401
Version: 004.01
Release:        21%{?dist}
URL:     https://moji.or.jp/ipafont/
%global foundry           IPA 
%global fontlicense       IPA
%global fontlicenses      IPA_Font_License_Agreement_v1.0.txt
%global fontdocs          Readme_ipaexg00401.txt
%global fontdocsex        %{fontlicenses}
%global fontfamily        IPAexGothic
%global fontsummary       Japanese Gothic-typeface OpenType font by IPA
%global fontpkgheader     %{expand:
Obsoletes: ipa-ex-gothic-fonts < %{version}-%{release}
Provides:  ipa-ex-gothic-fonts = %{version}-%{release}
}
%global fonts             ipaexg.ttf
%global fontconfs         %{SOURCE10}
%global fontdescription   %{expand:
IPAex Font is a Japanese OpenType fonts that is JIS X 0213:2004
compliant, provided by Information-technology Promotion Agency, Japan.
This package contains Gothic (sans-serif) style font.
}
Source0:        https://moji.or.jp/wp-content/ipafont/%{foundry}exfont/ipaexg%{archivever}.zip
Source10: 68-%{fontpkgname}.conf
%fontpkg
# oreon:deps
BuildRequires:  fonts-rpm-macros
# /oreon:deps
%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n ipaexg00401
chmod 0644 Readme_ipaexg%{archivever}.txt
sed -ie 's/\r//g' Readme_ipaexg%{archivever}.txt

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
