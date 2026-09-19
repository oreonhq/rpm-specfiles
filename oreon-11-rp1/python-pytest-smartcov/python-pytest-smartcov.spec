%global source0_hash db99c7a1a9717f5386303a528ee6bcbe8cbcb43ce08e239cfc32bd68bb1281a1

# Created by pyp2rpm-3.3.5
%global pypi_name pytest-smartcov

%global common_description %{expand:
Smart coverage measurement and reporting for py.test test suites. Test suites
are usually structured parallel to (or integrated with) the structure of the
code they test. If you ask py.test to run a certain subset of your tests, you
shouldn't have to also tell coverage which subset of your code it should
measure coverage on for that run. With pytest-smartcov, you don't have to.}

Name:           python-%{pypi_name}
Version:        0.3
Release:        20%{?dist}
Summary:        Smart coverage plugin for pytest

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/carljm/pytest-smartcov
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
%{common_description}

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
%{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/smartcov.py
%{python3_sitelib}/pytest_smartcov-%{version}-py%{python3_version}.egg-info

%changelog
%autochangelog
