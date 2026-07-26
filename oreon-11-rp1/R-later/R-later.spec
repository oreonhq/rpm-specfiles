%global source0_hash de323ae574fb26b642ff1e682775ff75b987976004eb68dc149384cbe8ba1330

Name:           R-later
Version:        %R_rpm_version 1.4.5
Release:        %autorelease
Summary:        Utilities for Scheduling Functions to Execute Later with Event Loops

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}
# Remove bundled tinycthread and use C11 threads directly.
Source:         tinycthread-threads-wrapper.h

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel
Obsoletes:      %{name}-devel <= 1.4.4

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

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
# A file used in tests; tests aren't installed.
rm %{buildroot}%{_R_libdir}/later/bgtest.cpp
%R_save_files

%check
%R_check

%files -f %{R_files}

%changelog
%autochangelog
