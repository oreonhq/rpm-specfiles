%global source0_hash 09aec202f0d6bf58e3c9efdae6fb73f3b49d5b4f4013b5e9da686aa634973d18

Name:           R-measurements
Version:        %R_rpm_version 1.5.1
Release:        %autorelease
Summary:        Tools for Units of Measurement

License:        GPL-3.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Collection of tools to make working with physical measurements easier. Convert
between metric and imperial units, or calculate a dimension's unknown value
from other dimensions' measurements.

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
