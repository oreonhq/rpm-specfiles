%global source0_hash 4a14c67d520fda9d42b0da6134638578caae1d374b9bb462d8de00587dba764c

%{?python_enable_dependency_generator}
# Created by pyp2rpm-1.0.1
%global pypi_name cov-core
%global summary Plugin core for use by pytest-cov, nose-cov and nose2-cov
%global _description \
This is a lib package for use by pytest-cov, nose-cov and nose2-cov. \
If you're developing a coverage plugin for a test framework then you \
probably want one of those.

Name:           python-%{pypi_name}
Version:        1.15.0
Release:        39%{?dist}
Summary:        %{summary}

License:        MIT
URL:            http://bitbucket.org/memedough/cov-core/overview
Source0:        https://pypi.python.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
%description %{_description}

# Python3
%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-coverage >= 3.6
%endif

%description -n python%{python3_pkgversion}-%{pypi_name} %{_description}

%if 0%{?with_python3_other}
%package -n python%{python3_other_pkgversion}-%{pypi_name}
Summary: %{summary}
BuildRequires:  python%{python3_other_pkgversion}-devel
BuildRequires:  python%{python3_other_pkgversion}-setuptools
%{?python_provide:%python_provide python%{python3_other_pkgversion}-%{pypi_name}}
%if %{undefined __pythondist_requires}
Requires: python%{python3_other_pkgversion}-coverage >= 3.6
%endif

%description -n python%{python3_other_pkgversion}-%{pypi_name} %{_description}
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
%if 0%{?with_python3_other}
%py3_other_build
%endif

%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install (and we want the python2 version
# to be the default for now).
%if 0%{?with_python3_other}
%py3_other_install
%endif
%py3_install

# Python3
%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/cov_core*
%{python3_sitelib}/__pycache__/*

%if 0%{?with_python3_other}
%files -n python%{python3_other_pkgversion}-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python3_other_sitelib}/cov_core*
%{python3_other_sitelib}/__pycache__/*
%endif

%changelog
%autochangelog
