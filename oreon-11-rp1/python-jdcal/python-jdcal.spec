%global source0_hash 6cb87959fb9293bdd577967419af735a1a0aee3ce778c443acb219b2668c6597

%global modname jdcal

Name:           python-%{modname}
Version:        1.4.1
Release:        %autorelease
Summary:        Julian dates from proleptic Gregorian and Julian calendars

License:        BSD-2-Clause
URL:            https://github.com/phn/jdcal
Source0:        %{url}/archive/v%{version}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:		python3-devel
BuildRequires:		python3-pytest

%description
This module contains functions for converting between Julian dates and calendar
dates.

A function for converting Gregorian calendar dates to Julian dates, and another
function for converting Julian calendar dates to Julian dates are defined.
Two functions for the reverse calculations are also defined.

%package -n python3-%{modname}
Summary:        %{summary}

%description -n python3-%{modname}
This module contains functions for converting between Julian dates and calendar
dates.

A function for converting Gregorian calendar dates to Julian dates, and another
function for converting Julian calendar dates to Julian dates are defined.
Two functions for the reverse calculations are also defined.

Python 3 version.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{modname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{modname}

%check
%pytest -v

%files -n python3-%{modname} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
