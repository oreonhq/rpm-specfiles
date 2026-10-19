%global source0_hash 21f4e24bbd7b24c31ba13ddb10600db3a61565f20f2ccf2347f4e114e6e34596
Version:        3.052R
Release:        1%{?dist}
URL:            https://github.com/adobe-fonts/source-sans
%global foundry adobe
%global fontlicense OFL-1.1
%global fontlicenses LICENSE.md
%global fontdocs README.md
%global fontdocsex %{fontlicenses}
%global fontfamily Source Sans Pro
%global fontsummary A set of OpenType fonts designed for user interfaces
%global fonts OTF/*.otf
%global fontconfs %{SOURCE10}
%global fontdescription %{expand:Source Sans is a set of OpenType fonts that have been designed to work well in
user interface (UI) environments, as well as in text setting for screen and
print.}
Source0:        https://github.com/%{foundry}-fonts/source-sans/archive/%{version}/%{foundry}-source-sans-pro-fonts-%{version}.tar.gz
Source10:       63-%{fontpkgname}.conf
%fontpkg
# oreon:deps
BuildRequires:  fonts-rpm-macros
# /oreon:deps
%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir source-sans-%{version}
%oreon_prep
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
