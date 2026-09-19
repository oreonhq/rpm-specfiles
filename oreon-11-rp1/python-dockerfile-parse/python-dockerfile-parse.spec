%global source0_hash 695cc70201d7bea38458d7e513c4bf3ab664a15c8113e99e276d49c489179931

%bcond_without tests

%global srcname dockerfile-parse
%global modname %(n=%{srcname}; echo ${n//-/_})

Name:           python-%{srcname}
Version:        2.0.1
Release:        12%{?dist}

Summary:        Python library for Dockerfile manipulation
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/containerbuildsystem/dockerfile-parse
Source0:        https://github.com/containerbuildsystem/dockerfile-parse/archive/%{version}.tar.gz

BuildArch:      noarch

%description
%{summary}.

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if %{with tests}
BuildRequires:  python3-pytest
%endif

%description -n python3-%{srcname}
%{summary}.

Python 3 version.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%if %{with tests}
%check
export LANG=C.UTF-8
py.test-%{python3_version} -v tests
%endif

%files -n python3-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{modname}-*.egg-info/
%{python3_sitelib}/%{modname}/

%changelog
%autochangelog
