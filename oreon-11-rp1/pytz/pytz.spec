%global source0_hash none

# Allow build without test
%bcond_without tests

Name:           pytz
Version:        2026.1
Release:        1%{?dist}
Summary:        World Timezone Definitions for Python

License:        MIT
URL:            http://pytz.sourceforge.net/
Source:         %pypi_source
# Patch to use the system supplied zoneinfo files
Patch:          pytz-zoneinfo.patch
# https://bugzilla.redhat.com/1497572
Patch:          remove_tzinfo_test.patch

BuildArch:      noarch
BuildRequires:  tzdata

%global _description\
pytz brings the Olson tz database into Python. This library allows accurate\
and cross platform timezone calculations using Python 2.3 or higher. It\
also solves the issue of ambiguous times at the end of daylight savings,\
which you can read more about in the Python Library Reference\
(datetime.tzinfo).\
\
Almost all (over 540) of the Olson timezones are supported.

%description %_description


%package -n python3-%{name}
Summary:        %summary
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3-pytest
%endif
Requires:       tzdata

%description -n python3-%{name} %_description


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
rm -r %{buildroot}%{python3_sitelib}/pytz/zoneinfo


%if %{with tests}
%check
%pytest -v
%endif


%files -n python3-pytz
%doc README.rst
%{python3_sitelib}/pytz/
%{python3_sitelib}/pytz-%{version}.dist-info

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2026.1-1
- Prepare for Oreon 11 (RP1)
