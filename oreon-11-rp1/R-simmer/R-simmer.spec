%global source0_hash ac79c5832a54d8e8bbdc1ac3ab7e687b773761bf7cedee3b523edda157964952

Name:           R-simmer
Version:        %R_rpm_version 4.4.7
Release:        %autorelease
Summary:        Discrete-Event Simulation for R

License:        GPL-2.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel
Obsoletes:      %{name}-devel <= 4.4.7

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

%autosetup -c

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check

%files -f %{R_files}

%changelog
%autochangelog
