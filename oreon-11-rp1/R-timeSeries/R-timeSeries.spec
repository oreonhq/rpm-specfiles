%global source0_hash c4e50a669cfa34814a71e47bb93020442ec40694fc3f1c7bcd94edf2368c6993

Name:           R-timeSeries
Version:        %R_rpm_version 4052.112
Release:        %autorelease
Summary:        Financial Time Series Objects (Rmetrics)

License:        GPL-2.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
'S4' classes and various tools for financial time series: Basic functions such
as scaling and sorting, subsetting, mathematical operations and statistical
functions.

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
