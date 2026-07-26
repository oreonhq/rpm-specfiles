%global source0_hash bdaa4dcfc4b20a9ce1f5cb6da3116b6cb8fe37527d991fd242856ef2cccd218e

%if 0%{?fedora}
%global with_python2 0
%global with_python3 1
%endif

%global pypi_name persist-queue

Name:           python-%{pypi_name}
Version:        0.8.0
Release:        15%{?dist}
Summary:        A single process, persistent multi-producer, multi-consumer queue

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        https://pypi.io/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
A single process, persistent multi-producer, multi-consumer queue

%if 0%{?with_python2}
%package -n python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}

BuildRequires:  python2-devel
BuildRequires:  python2-mock
BuildRequires:  python2-setuptools
BuildRequires:  python2-nose2
BuildRequires:  python2-msgpack

Requires: python2-msgpack

%description -n python2-%{pypi_name}
A single process, persistent multi-producer, multi-consumer queue

%endif

%if 0%{?with_python3}
%package -n python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-devel
BuildRequires:  python3-nose2
BuildRequires:  python3-msgpack
BuildRequires:  python3-setuptools

Requires: python3-msgpack

%description -n python3-%{pypi_name}
A single process, persistent multi-producer, multi-consumer queue

%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -n %{pypi_name}-%{version}

%build
%if 0%{?with_python2}
%py2_build
%endif

%if 0%{?with_python3}
%py3_build
%endif

%install
%if 0%{?with_python2}
%py2_install
%endif

%if 0%{?with_python3}
%py3_install
%endif

%check
%if 0%{?with_python2}
nose2-2.7 persistqueue.tests.test_queue
%endif
%if 0%{?with_python3}
nose2 persistqueue.tests.test_queue
%endif

%if 0%{?with_python2}
%files -n python2-%{pypi_name}
%license LICENSE
%doc README.rst
%{python2_sitelib}/*
%exclude %{python2_sitelib}/tests
%endif

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/*
%exclude %{python3_sitelib}/tests
%endif

%changelog
%autochangelog
