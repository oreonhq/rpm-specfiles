%global source0_hash d8a138009ca66032e6bd39e1bc0a5d8f3bc0f272763c8646ad73d1b6faf37915

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%if 0%{?fedora}
%global with_python2 0
%global with_python3 1
%endif

%global pypi_name retryz

Name:           python-%{pypi_name}
Version:        0.1.9
Release:        34%{?dist}
Summary:        Retry decorator with a bunch of configuration parameters

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://pypi.python.org/pypi/retryz
Source0:        https://pypi.io/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Retry decorator with a bunch of configuration parameters.

%if 0%{?with_python2}
%package -n python2-%{pypi_name}
Summary:        %{summary}

%{?python_provide:%python_provide python2-%{pypi_name}}

Requires:       python2

BuildRequires:  python2-devel

# for running tests
BuildRequires:  python2-pytest
BuildRequires:  python2-hamcrest

%description -n python2-%{pypi_name}
Retry decorator with a bunch of configuration parameters.

%endif

%if 0%{?with_python3}
%package -n python3-%{pypi_name}
Summary:        %{summary}

%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

# for running tests
BuildRequires:  python3-pytest
BuildRequires:  python3-hamcrest

%description -n python3-%{pypi_name}
Retry decorator with a bunch of configuration parameters.

%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{pypi_name}-%{upstream_version}

%build
%if 0%{?with_python2}
%py2_build
%endif
%if 0%{?with_python3}
%py3_build
%endif

%check
%if 0%{?with_python2}
PYTHONPATH=. py.test-2.7
%endif
%if 0%{?with_python3}
PYTHONPATH=. py.test-3
%endif

%install
%if 0%{?with_python2}
%py2_install
%endif

%if 0%{?with_python3}
%py3_install
%endif

%if 0%{?with_python2}
%files -n python2-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python2_sitelib}/retryz*
%endif

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/retryz*
%endif

%changelog
%autochangelog
