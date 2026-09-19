%global source0_hash 05f1598f9bb8da0f78f28e80f897899f992b29368713ce8d33ab5e0ac3979350

# SPDX-License-Identifier: MIT
%global forgeurl    https://github.com/ossobuffo/jura
%global commit      6e2614af65721fe74167b1f74b90e7bf5c0d0260
%forgemeta

Version: 5.103
Release: 16%{?dist}
URL:     %{forgeurl}

%global foundry           ossobuffo
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt
%global fontdocs          *txt *html *md
%global fontdocsex        %{fontlicenses}

%global fontfamily        Jura
%global fontsummary       Jura, a sans-serif font family in the Eurostile vein
%global fonts             fonts/otf/*otf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Jura is a sans-serif font family in the Eurostile vein.}

Source0:  %{forgesource}
Source10: 60-%{fontpkgname}.xml

%fontpkg

%package   doc
Summary:   Optional documentation files of %{name}
BuildArch: noarch
%description doc
This package provides optional documentation files shipped with
%{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup
%linuxtext %{fontdocs} %{fontlicenses}
chmod 644 %{fontdocs} %{fontlicenses}

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
%doc documentation/*

%changelog
%autochangelog
