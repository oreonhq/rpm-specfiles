%global source0_hash ac79c5832a54d8e8bbdc1ac3ab7e687b773761bf7cedee3b523edda157964952
Name:           R-simmer
Version:        %R_rpm_version 4.4.7
Release:        1%{?dist}
Summary:        Discrete-Event Simulation for R
License:        GPL-2.0-or-later
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=simmer&version=%{version}#/simmer_%{version}.tar.gz
ExcludeArch:    %{ix86}
Obsoletes:      %{name}-devel <= 4.4.7
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
A process-oriented and trajectory-based Discrete-Event Simulation (DES)
package for R. It is designed as a generic yet powerful framework. The
architecture encloses a robust and fast simulation core written in 'C++'
with automatic monitoring capabilities. It provides a rich and flexible R
API that revolves around the concept of trajectory, a common path in the
simulation model for entities of the same type.
Documentation about 'simmer' is provided by several vignettes included in
this package, via the paper by Ucar, Smeets & Azcorra (2019,
<doi:10.18637/jss.v090.i02>), and the paper by Ucar, Hernández, Serrano &
Azcorra (2018, <doi:10.1109/MCOM.2018.1700960>); see 'citation("simmer")'
for details.

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
