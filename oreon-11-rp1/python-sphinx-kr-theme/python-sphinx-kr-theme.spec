%global source0_hash 4241d0ad37f46ad3db954a3d9cb557d697b63eadc6fc38d856117996d12a4e15

%bcond_without tests

%global pypi_name sphinx-kr-theme

Name:           python-%{pypi_name}
Version:        0.2.1
Release:        23%{?dist}
Summary:        Kenneth Reitz's krTheme for Sphinx

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/tonyseek/sphinx-kr-theme
Source0:        %{pypi_source}
%if %{with tests}
# Tests are not included in the PyPI tarball
Source1:        https://raw.githubusercontent.com/tonyseek/sphinx-kr-theme/57834e237e35b59b5957aacb7ac072e434dd5e93/tests.py
%endif
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%if %{with tests}
BuildRequires:  python3dist(pytest)
%endif

%description
This is a repackaging of Kenneth Reitz's krTheme, a theme for use in 
Sphinx documentation, originally derived from Mitsuhiko's Flask theme.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

Requires:       python3dist(setuptools)
%if 0%{?fedora} < 33 || 0%{?rhel} < 9
%py_provides    python3-%{pypi_name}
%endif

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

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/sphinx_kr_theme
%{python3_sitelib}/sphinx_kr_theme-%{version}-py%{python3_version}.egg-info

%changelog
%autochangelog
