%global source0_hash 15dbebf8b46814e6e4cf9affb83439b253477900b1159d6f0c3a919fc44e1828
Name:           R-getPass
Version:        %R_rpm_version 0.2-4
Release:        1%{?dist}
Summary:        Masked User Input
License:        BSD-2-Clause
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=getPass&version=0.2-4#/getPass_0.2-4.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
A micro-package for reading "passwords", i.e.  reading user input with
masking, so that the input is not displayed as it is typed.  Currently we
have support for 'RStudio', the command line (every OS), and any platform
where 'tcltk' is present.

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
