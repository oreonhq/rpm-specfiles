%global source0_hash a1ab708617671dfa30e23068e5ffe3b639747dca65ea171d37ae605080aaeae0

# SPDX-License-Identifqier: MIT
%global forgeurl https://github.com/mitradranirban/font-uniol
Version:   2.001
Release:   5%{?dist}
%forgemeta
URL: %{forgeurl}
%global fontfamily    uniol
%global fontlicense       OFL-1.1
%global fontlicenses      Licence
%global fontdocs       README.md
%global fontdocsex        %{fontlicenses}
%global fontsummary       Unicode compliant Open source Ol Chiki font
%global fonts            *.ttf
%global fontconfs        66-0-%{fontpkgname}.conf
BuildRequires: fontforge

%global fontdescription  %{expand:
 This is an Unicode compliant OlChiki or OlCemet font.
 OlChiki is a modern alphabetic script used to write Santhali
  language used in various states of India.
}

Source0: %{forgesource}

%fontpkg

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup

%build
chmod 755 generate.pe
./generate.pe *.sfd

%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
%autochangelog
