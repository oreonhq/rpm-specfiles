%global source0_hash 9dc353119eda80c01c03f28fc33c8b37c105710305783ed29e46f5136570a53e

Name:           R-errors
Version:        %R_rpm_version 0.4.4
Release:        %autorelease
Summary:        Uncertainty Propagation for R Vectors

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Support for measurement errors in R vectors, matrices and arrays:
automatic uncertainty propagation and reporting.
Documentation about 'errors' is provided in the paper by Ucar,
Pebesma & Azcorra (2018, <doi:10.32614/RJ-2018-075>), included in
this package as a vignette; see 'citation("errors")' for details.

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
