%global source0_hash d6e302974bd518ff215cb0112d576b11afb44847e28559700e434bf01e353449

# SPDX-License-Identifier: MIT
%global forgeurl    https://github.com/googlefonts/MuliFont
%global commit      580b05e1f2ad319cd98a8de03fd2da7b36677954
%forgemeta

Version: 2.001
Release: 20%{?dist}
URL:     %{forgeurl}

%global foundry           vernnobile
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt
%global fontdocs          *txt *md
%global fontdocsex        %{fontlicenses}

%global fontfamily        Muli
%global fontsummary       Muli, a minimalist sans serif font family
%global fonts             fonts/*ttf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Muli is a minimalist sans serif font family, designed for both display and text
typography.}

Source0:  %{forgesource}
Source10: 60-%{fontpkgname}.xml

%fontpkg

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
%autochangelog
