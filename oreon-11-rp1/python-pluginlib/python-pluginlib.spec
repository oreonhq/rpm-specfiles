%global source0_hash 88727037138f759a3952f6391ae3751536f04ad8be6023607620ea49695a3a83

%global pypi_name pluginlib
%global sum  A framework for creating and importing plugins in Python
%global desc Pluginlib is a Python framework for creating and importing plugins.\
Pluginlib makes creating plugins for your project simple.

%bcond_without python3

Name:           python-%{pypi_name}
Version:        0.9.4
Release:        7%{?dist}
Summary:        %{sum}

License:        MPL-2.0
URL:            https://github.com/Rockhopper-Technologies/pluginlib
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%if %{with python3}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%endif

%if 0%{?with_python3_other}
BuildRequires:  python%{python3_other_pkgversion}-devel
BuildRequires:  python%{python3_other_pkgversion}-setuptools
%endif

%description
%{desc}

# Python 3 package
%if %{with python3}
%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{sum}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-setuptools

%description -n python%{python3_pkgversion}-%{pypi_name}
%{desc}
%endif

# Python 3 other package
%if 0%{?with_python3_other}
%package -n     python%{python3_other_pkgversion}-%{pypi_name}
Summary:        %{sum}
%{?python_provide:%python_provide python%{python3_other_pkgversion}-%{pypi_name}}
Requires:       python%{python3_other_pkgversion}-setuptools

%description -n python%{python3_other_pkgversion}-%{pypi_name}
%{desc}
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p0 -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%if %{with python3}
%py3_build
%endif

%if 0%{?with_python3_other}
%py3_other_build
%endif

%install
%if 0%{?with_python3_other}
%py3_other_install
%endif

%if %{with python3}
%py3_install
%endif

%check
%if %{with python3}
%{__python3} -m unittest
%endif

%if 0%{?with_python3_other}
%{__python3_other} -m unittest
%endif

%if %{with python3}
%files -n python%{python3_pkgversion}-%{pypi_name}
%doc README*
%license LICENSE
%{python3_sitelib}/pluginlib*
%endif

%if 0%{?with_python3_other}
%files -n python%{python3_other_pkgversion}-%{pypi_name}
%doc README*
%license LICENSE
%{python3_other_sitelib}/pluginlib*
%endif

%changelog
%autochangelog
