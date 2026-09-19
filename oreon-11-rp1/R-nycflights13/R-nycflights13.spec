%global source0_hash 0e87c5a4e285f16750e91c75aeba33b1e4682cdabf4a3effe5a1de7398394a1d

Name:           R-nycflights13
Version:        %R_rpm_version 1.0.2
Release:        %autorelease
Summary:        Flights that Departed NYC in 2013

License:        CC0-1.0
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Airline on-time data for all flights departing NYC in 2013. Also includes
useful 'metadata' on airlines, airports, weather, and planes.

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
