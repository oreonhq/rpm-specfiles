%global source0_hash 6a02470b1716ec7a32abe89a873a4795c41c938468225f8a53d860980ec9e3c6

%global pypi_name jmespath

Name:           python-%{pypi_name}
Version:        1.0.1
Release:        14%{?dist}
Summary:        JSON Matching Expressions

License:        MIT
URL:            https://github.com/jmespath/jmespath.py
Source0:        https://github.com/jmespath/jmespath.py/archive/1.0.1/jmespath.py-1.0.1.tar.gz
BuildArch:      noarch

%description
JMESPath allows you to declaratively specify how to extract elements from
a JSON document.

%package -n     python3-%{pypi_name}
Summary:        JSON Matching Expressions
%{?python_provide:%python_provide python3-%{pypi_name}}
%{?python_provide:%python_provide python-%{pypi_name}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

BuildRequires:  python3-pytest
%if %{undefined rhel}
BuildRequires:  python3-hypothesis
%endif

Obsoletes: python2-jmespath < 0.9.4-2

%description -n python3-%{pypi_name}
JMESPath allows you to declaratively specify how to extract elements from
a JSON document.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n jmespath.py-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
# RHEL does not have python3-hypothesis. Only one file in the upstream repo
# depends on hypothesis, so we can omit this dependency for RHEL.
%pytest %{?rhel:--ignore=extra/test_hypothesis.py}

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE.txt
%{_bindir}/jp.py
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.1-14
- Prepare for Oreon 11 (RP1)
