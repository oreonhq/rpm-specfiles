%global source0_hash bceafaec359f032393ddd560ae2cc8d163613833ec63c93ce7189f85904e53d6

%global srcname nagiosplugin

Name:           python-%{srcname}
Version:        1.3.3
Release:        15%{?dist}
License:        ZPL-2.1
Summary:        Library for writing Nagios (Icinga) plugins

URL:            https://nagiosplugin.readthedocs.io
Source:         %{pypi_source}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)

BuildArch:      noarch

%global _description %{expand:
nagiosplugin is a Python class library which helps writing Nagios (or Icinga)
compatible plugins easily in Python. It cares for much of the boilerplate
code and default logic commonly found in Nagios checks, including:

- Nagios 3 Plugin API compliant parameters and output formatting
- Full Nagios range syntax support
- Automatic threshold checking
- Multiple independend measures
- Custom status line to communicate the main point quickly
- Long output and performance data
- Timeout handling
- Persistent “cookies” to retain state information between check runs
- Resume log file processing at the point where the last run left}

%description %{_description}

%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
%pytest

%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.txt
%{python3_sitelib}/nagiosplugin-*.egg-info/
%{python3_sitelib}/nagiosplugin/

%changelog
%autochangelog
