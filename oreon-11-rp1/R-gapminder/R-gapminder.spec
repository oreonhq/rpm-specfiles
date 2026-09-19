%global source0_hash edd138576fcff02ac41f9580dbd9713f3e98a9bd32039decd098078b421a351f

Name:           R-gapminder
Version:        %R_rpm_version 1.0.1
Release:        %autorelease
Summary:        Data from Gapminder

License:        CC0-1.0
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
An excerpt of the data available at Gapminder.org. For each of 142 countries,
the package provides values for life expectancy, GDP per capita, and
population, every five years, from 1952 to 2007.

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
