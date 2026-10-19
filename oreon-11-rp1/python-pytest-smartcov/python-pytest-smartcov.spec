%global source0_hash db99c7a1a9717f5386303a528ee6bcbe8cbcb43ce08e239cfc32bd68bb1281a1
%global pypi_name pytest-smartcov
%global common_description %{expand:
Smart coverage measurement and reporting for py.test test suites. Test suites
are usually structured parallel to (or integrated with) the structure of the
code they test. If you ask py.test to run a certain subset of your tests, you
shouldn't have to also tell coverage which subset of your code it should
measure coverage on for that run. With pytest-smartcov, you don't have to.}
Name:           python-%{pypi_name}
Version:        0.3
Release:        1%{?dist}
Summary:        Smart coverage plugin for pytest
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/carljm/pytest-smartcov
Source0:        https://files.pythonhosted.org/packages/source/p/python-pytest-smartcov/python-pytest-smartcov-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
# /oreon:deps
%description
%{common_description}

%package -n     python3-%{pypi_name}
Summary:        Smart coverage plugin for pytest
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-pytest-smartcov -f %{oreon_filedir}/python3-pytest-smartcov.list

%changelog

%autochangelog
