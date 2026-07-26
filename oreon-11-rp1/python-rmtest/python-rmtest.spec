%global source0_hash 1ba37ea9534a291d2226e802d291a2974b4099a8f6ac29cad8aa04c63c59b7c4

%global srcname rmtest
%global summary A simple framework for testing Redis modules
%if 0%{?rhel} > 7 || 0%{?fedora} >= 30
%global disable_python2 1
%else
%global disable_python2 0
%endif

Name:    python-%{srcname}
Version: 1.0.1
Release: 25%{?dist}
Summary: %{summary}

# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
URL:     https://github.com/goodform/%{srcname}

Source0: https://github.com/goodform/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
Source1: https://raw.githubusercontent.com/goodform/%{srcname}/master/LICENSE
Source2: https://raw.githubusercontent.com/goodform/%{srcname}/master/README.md

# workaround changes introduced in Redis 7
Patch0: redis-compat.patch

BuildArch:      noarch
%if !%{disable_python2}
BuildRequires:  python2-devel python2-redis
%endif
BuildRequires:  python3-devel python3-redis
BuildRequires:  python3-setuptools
BuildRequires:  redis-devel gcc
BuildRequires:  redis >= 4
Requires:       redis >= 4

%description
Simple framework for testing Redis modules using python
unit test and a disposable ephemeral Redis sub-process.

%if !%{disable_python2}
%package -n python2-%{srcname}
Summary:        %{summary}
Requires:       python2-redis
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
Simple framework for testing Redis modules using python
unit test, and a disposable ephemeral Redis sub-process.
%endif

%package -n python3-%{srcname}
Summary:        %{summary}
Requires:       python3-redis
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Simple framework for testing Redis modules using python
unit test, and a disposable ephemeral Redis sub-process.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1
cp %{S:1} %{S:2} .

%build
%if !%{disable_python2}
%py2_build
%endif
%py3_build

%install
%if !%{disable_python2}
%py2_install
%endif
%py3_install

%check
%if !%{disable_python2}
PYTHONPATH=%{buildroot}/%{python2_sitelib}/rmtest %{__python2} setup.py test
%endif
PYTHONPATH=%{buildroot}/%{python3_sitelib}/rmtest %{__python3} test.py

%if !%{disable_python2}
%files -n python2-%{srcname}
%license LICENSE
%doc README.md
%{python2_sitelib}/*
%endif

%files -n python3-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/*

%changelog
%autochangelog
