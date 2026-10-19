%global source0_hash 0e87c5a4e285f16750e91c75aeba33b1e4682cdabf4a3effe5a1de7398394a1d
Name:           R-nycflights13
Version:        %R_rpm_version 1.0.2
Release:        1%{?dist}
Summary:        Flights that Departed NYC in 2013
License:        CC0-1.0
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=nycflights13&version=%{version}#/nycflights13_%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Airline on-time data for all flights departing NYC in 2013. Also includes
useful 'metadata' on airlines, airports, weather, and planes.

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
