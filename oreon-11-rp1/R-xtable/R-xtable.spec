%global source0_hash 5abec0e8c27865ef0880f1d19c9f9ca7cc0fd24eadaa72bcd270c3fb4075fd1c
Name:           R-xtable
Version:        %R_rpm_version 1.8-4
Release:        1%{?dist}
Summary:        Export Tables to LaTeX or HTML
License:        GPL-2.0-or-later
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=xtable&version=1.8-4#/xtable_1.8-4.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Coerce data to LaTeX and HTML tables.

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
