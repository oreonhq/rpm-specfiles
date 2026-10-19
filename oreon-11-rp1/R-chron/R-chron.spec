%global source0_hash 07ad2c77243dbbc9fa3bf4934466a0bc26bfe157172ffcd5a9a421621df1bea1
Name:           R-chron
Version:        %R_rpm_version 2.3-62
Release:        1%{?dist}
Summary:        Chronological Objects which can Handle Dates and Times
License:        GPL-2.0-only
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=chron&version=2.3-62#/chron_2.3-62.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Provides chronological objects which can handle dates and times.

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
