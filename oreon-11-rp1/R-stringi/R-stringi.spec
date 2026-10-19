%global source0_hash 0526decdcd41b7c42278aca96945394c2cb66ba6fdd47fd917b5d3d38ed5c8c6
Name:           R-stringi
Version:        %R_rpm_version 1.8.7
Release:        1%{?dist}
Summary:        Character String Processing Facilities
License:        BSD-3-Clause AND GPL-2.0-or-later
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=stringi&version=%{version}#/stringi_%{version}.tar.gz
ExcludeArch:    %{ix86}
Obsoletes:      %{name}-devel <= 1.8.7
# oreon:deps
BuildRequires:  R-devel
BuildRequires:  libicu-devel
# /oreon:deps
%description
A multitude of character string/text/natural language processing tools: pattern
searching (e.g., with 'Java'-like regular expressions or the 'Unicode'
collation algorithm), random string generation, case mapping, string
transliteration, concatenation, sorting, padding, wrapping, Unicode
normalisation, date-time formatting and parsing, and many more. They are fast,
consistent, convenient, and - owing to the use of the 'ICU' (International
Components for Unicode) library - portable across all locales and platforms.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c

# Remove bundled code.
rm -r stringi/src/icu74
sed -i -e '/src\/icu74\//d' stringi/MD5

%build

%install
%R_install \--configure-args="--disable-icu-bundle"
%R_save_files
%oreon_autofiles main

%check

%R_check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
