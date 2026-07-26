%global source0_hash 21f4e24bbd7b24c31ba13ddb10600db3a61565f20f2ccf2347f4e114e6e34596

Version:        3.052
Release:        9%{?dist}
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

Source0:        %{url}/archive/%{version}R/%{fontpkgname}-%{version}.tar.gz
# Adjust as necessary. Keeping the filename in sync with the package name is a good idea.
# See the fontconfig templates in fonts-rpm-templates for information on how to
# write good fontconfig files and choose the correct priority [number].
Source10:       63-%{fontpkgname}.conf

%fontpkg

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n source-sans-%{version}R

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
%autochangelog
