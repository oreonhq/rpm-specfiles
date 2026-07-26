%global source0_hash eaccd68db5c73d6a089ce5b323cdd51bc6a6a58ce467987158ba8c9be6a0a94e

Name:           R-NISTunits
Version:        %R_rpm_version 1.0.1
Release:        %autorelease
Summary:        Fundamental Physical Constants and Unit Conversions from NIST

License:        GPL-3.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Fundamental physical constants (Quantity, Value, Uncertainty, Unit) for SI
(International System of Units) and non-SI units, plus unit conversions. Based
on the data from NIST (National Institute of Standards and Technology, USA)

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
