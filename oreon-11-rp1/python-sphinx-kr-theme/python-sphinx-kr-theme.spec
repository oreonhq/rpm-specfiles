%global source1_hash 01a03a793676753aa553d7b19f858d4aa3630605b22ea8b6158b7af9555b787d
%global source0_hash 4241d0ad37f46ad3db954a3d9cb557d697b63eadc6fc38d856117996d12a4e15
%bcond_without tests
%global pypi_name sphinx-kr-theme
Name:           python-%{pypi_name}
Version:        0.2.1
Release:        1%{?dist}
Summary:        Kenneth Reitz's krTheme for Sphinx
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/tonyseek/sphinx-kr-theme
Source0:        https://files.pythonhosted.org/packages/source/p/python-sphinx-kr-theme/python-sphinx-kr-theme-%{version}.tar.gz
%if %{with tests}
Source1:        https://raw.githubusercontent.com/tonyseek/sphinx-kr-theme/57834e237e35b59b5957aacb7ac072e434dd5e93/tests.py
%endif
BuildArch:      noarch
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
# /oreon:deps
%description
This is a repackaging of Kenneth Reitz's krTheme, a theme for use in 
Sphinx documentation, originally derived from Mitsuhiko's Flask theme.

%package -n     python3-%{pypi_name}
Summary:        Kenneth Reitz's krTheme for Sphinx
Requires:       python3dist(setuptools)
%description -n python3-%{pypi_name}
This is a repackaging of Kenneth Reitz's krTheme, a theme for use in 
Sphinx documentation, originally derived from Mitsuhiko's Flask theme.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build

%py3_build
%if %{with tests}
%check

export PYTHONPATH=%{buildroot}%{python3_sitelib}
%pytest %{SOURCE1}
%endif
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-sphinx-kr-theme -f %{oreon_filedir}/python3-sphinx-kr-theme.list

%changelog

%autochangelog
