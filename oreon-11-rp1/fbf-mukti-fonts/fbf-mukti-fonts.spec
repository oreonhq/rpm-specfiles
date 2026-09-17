%global source0_hash b01a974032c0bf7af8e5dea0e16828b89b41e528c646da2d852e2f69d9b2730a

# SPDX-License-Identifqier: MIT
%global forgeurl https://github.com/mitradranirban/fonts-mukti

Version:   3.4.3
Release:   5%{?dist}

%forgemeta

URL: %{forgeurl}

Source0: %{forgesource}
Source1: https://github.com/mitradranirban/fbf-mukti-fonts/raw/main/SOURCES/66-0-fbf-mukti-fonts.conf

%global foundry fbf 
%global fontfamily    mukti         
%global fontlicense       GPL-3.0-or-later WITH Font-exception-2.0
%global fontlicenses      LICENCE 
%global fontdocs          README.md changelog
%global fontdocsex        %{fontlicenses}
%global fontsummary       Bangla open source Opentype font
%global fonts            *.otf
%global fontconfs        %{SOURCE1}
BuildRequires: fontforge 

%global fontdescription  %{expand:
This is a one of the earliest Open Source OpenType Bengali / Bangla font 
made for Mukta Bangla Font project. It was  made by using good quality glyphs
 of GPLed font bng2-n from Cyberscape Multimedia
<https://web.archive.org/web/20021113130716/http://www.akruti.com/freedom/>.
}

%fontpkg 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup -v
chmod 755 generate.pe
./generate.pe *.sfd

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
%autochangelog
