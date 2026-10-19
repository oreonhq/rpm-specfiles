%global source0_hash 051e7332e3074db826efef9059067721864f9d70adc55bbcae3a72e5ae83913a
Name:           R-sys
Version:        %R_rpm_version 3.4.3
Release:        1%{?dist}
Summary:        Powerful and Reliable Tools for Running System Commands in R
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=sys&version=%{version}#/sys_%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Drop-in replacements for the base system2() function with fine control and
consistent behavior across platforms. Supports clean interruption, timeout,
background tasks, and streaming STDIN / STDOUT / STDERR over binary or text
connections. Arguments on Windows automatically get encoded and quoted to work
on different locales.

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
