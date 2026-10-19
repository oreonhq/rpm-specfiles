%global source0_hash a710c093055fd73bb8cfbee548af2916594b17670186bf25b4d59aedcc05ff99
%global forgeurl    https://github.com/kemie/Bellota-Font/
Version:            4.1
%forgemeta
Release:        18%{?dist}
URL:     %{forgeurl}
%global foundry           kemie
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt
%global fontdocs          *txt *TXT *md
%global fontdocsex        %{fontlicenses}
%global common_description %{expand:
The Bellota font families are ornamented, low contrast sans-serifs with text
and swash alternates. They’re just cute enough! They include stylistic
alternates (for swash and non-ornamented characters) and ligatures available
through OpenType features.}
%global fontfamily0       Bellota
%global fontsummary0      An ornamented, cute, low contrast sans-serif font family
%global fonts0            ttf/*ttf
%global fontsex0          %{fonts1}
%global fontconfngs0      %{SOURCE10}
%global fontdescription0  %{expand:
%{common_description}
Bellota, is the most exuberant variation published by the project.}
%global fontfamily1       Bellota Text
%global fontsummary1      An ornamented, slightly demure, cute, low contrast sans-serif font family
%global fontpkgheader1    %{expand:
Suggests: font(bellota)
}
%global fonts1            ttf/BellotaText*ttf
%global fontconfngs1      %{SOURCE11}
%global fontdescription1  %{expand:
%{common_description}
Bellota Text is slightly more demure than Bellota itself.}
Source0:        %{forgeurl}archive/v%{version}/%{fontfamily0}-Font-%{version}.tar.gz
Source10: 60-%{fontpkgname0}.xml
Source11: 60-%{fontpkgname1}.xml
%fontpkg -a
%fontmetapkg
# oreon:deps
BuildRequires:  fonts-rpm-macros
# /oreon:deps
%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup

%build

%fontbuild -a
%install
%fontinstall -a
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%fontcheck -a
%fontfiles -a
%files -f %{oreon_filedir}/main.list
%files -n google-go-fonts -f %{oreon_filedir}/google-go-fonts.list
%files -n adf-gillius-2-fonts -f %{oreon_filedir}/adf-gillius-2-fonts.list
%files -n google-go-smallcaps-fonts -f %{oreon_filedir}/google-go-smallcaps-fonts.list
%files -n adf-gillius-fonts-all -f %{oreon_filedir}/adf-gillius-fonts-all.list

%changelog

%autochangelog
