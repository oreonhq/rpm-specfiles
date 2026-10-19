%global source0_hash c92c59e48107fc64d175840a2e408c7d9e6e608cde1a0568db490b92825fac30
Name:           R-procmaps
Version:        %R_rpm_version 0.0.5
Release:        1%{?dist}
Summary:        Portable Address Space Mapping
License:        GPL-3.0-only AND BSD-3-Clause
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=procmaps&version=%{version}#/procmaps_%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Portable '/proc/self/maps' as a data frame. Determine which library or
other region is mapped to a specific address of a process. -- R packages
can contain native code, compiled to shared libraries at build or
installation time. When loaded, each shared library occupies a portion of
the address space of the main process. When only a machine instruction
pointer is available (e.g. from a backtrace during error inspection or
profiling), the address space map determines which library this instruction
pointer corresponds to.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%install
%R_install
%R_save_files
%oreon_autofiles main

%check

%R_check \--no-tests
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
