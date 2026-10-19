%global source0_hash d0450b24f8b7b937033ad748b5fad76d23e9464f3e8c0c57a256d64829249a52
Name:           R-zip
Version:        %R_rpm_version 2.3.3
Release:        1%{?dist}
Summary:        Cross-Platform 'zip' Compression
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=zip&version=%{version}#/zip_%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Cross-Platform 'zip' Compression Library. A replacement for the 'zip'
function, that does not require any additional external tools on any
platform.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%install
%R_install
%R_save_files
%oreon_autofiles main

%check

%R_check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
