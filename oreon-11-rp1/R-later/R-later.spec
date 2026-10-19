%global source0_hash de323ae574fb26b642ff1e682775ff75b987976004eb68dc149384cbe8ba1330
Name:           R-later
Version:        %R_rpm_version 1.4.5
Release:        1%{?dist}
Summary:        Utilities for Scheduling Functions to Execute Later with Event Loops
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=later&version=%{version}#/later_%{version}.tar.gz
ExcludeArch:    %{ix86}
Obsoletes:      %{name}-devel <= 1.4.4
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Executes arbitrary R or C functions some time after the current time, after the
R execution stack has emptied. The functions are scheduled in an event loop.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
rm -f later/tests/testthat/test-run_now.R # unconditional suggest
# Ensure we don't use this bundled code.
rm later/src/{badthreads.h,tinycthread.c}
cp %{SOURCE1} later/src/tinycthread.h
sed -i -e '/badthread/d' -e '/tinycthread/d' later/MD5

%build

%install
%R_install
rm %{buildroot}%{_R_libdir}/later/bgtest.cpp
%R_save_files
%oreon_autofiles main

%check

%R_check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
