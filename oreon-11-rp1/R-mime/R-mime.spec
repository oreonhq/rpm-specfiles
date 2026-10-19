%global source0_hash 7132834cf3c3388eff12bad376d69fbcf8275acc37d36c290e59174fe3c7f3eb
Name:           R-mime
Version:        %R_rpm_version 0.13
Release:        1%{?dist}
Summary:        Map Filenames to MIME Types
License:        GPL-2.0-only OR GPL-3.0-only
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=mime&version=%{version}#/mime_%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Guesses the MIME type from a filename extension using the data derived from
/etc/mime.types in UNIX-type systems.

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
