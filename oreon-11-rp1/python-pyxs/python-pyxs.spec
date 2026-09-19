%global source0_hash 9eb0e793f7696284a6c4a134e230cd594b790cb45ae97680e4aa995ccaaffecb

# what it's called on pypi
%global srcname pyxs
# what it's imported as
%global libname pyxs
# name of egg info directory
%global eggname pyxs
# package name fragment
%global pkgname pyxs

%global common_description %{expand:
It's a pure Python XenStore client implementation, which covers all of the
libxs features and adds some nice Pythonic sugar on top.}

%if (%{defined fedora} && 0%{?fedora} < 30) || (%{defined rhel} && 0%{?rhel} < 8)
%bcond_without  python2
%endif

%bcond_without  python3

%bcond_without  tests

Name:           python-%{pkgname}
Version:        0.4.1
Release:        33%{?dist}
Summary:        Pure Python bindings to XenStore
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            https://github.com/selectel/pyxs
# PyPI tarball doesn't have tests
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
Patch0:         remove-pytest-runner-requirement.patch
BuildArch:      noarch

%description %{common_description}

%if %{with python2}
%package -n python2-%{pkgname}
Summary:        %{summary}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%if %{with tests}
# Test use pytest's yield_fixture decorator, which was first added in 2.4.
# https://github.com/pytest-dev/pytest/blob/2.4.0/CHANGELOG#L26-L33
BuildRequires:  python2-pytest >= 2.4
%endif
%{?python_provide:%python_provide python2-%{pkgname}}

%description -n python2-%{pkgname} %{common_description}
%endif

%if %{with python3}
%package -n python%{python3_pkgversion}-%{pkgname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%if %{with tests}
# Test use pytest's yield_fixture decorator, which was first added in 2.4.
# https://github.com/pytest-dev/pytest/blob/2.4.0/CHANGELOG#L26-L33
BuildRequires:  python%{python3_pkgversion}-pytest >= 2.4
%endif
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pkgname}}

%description -n python%{python3_pkgversion}-%{pkgname} %{common_description}
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p 1

%build
%{?with_python2:%py2_build}
%{?with_python3:%py3_build}

%install
%{?with_python2:%py2_install}
%{?with_python3:%py3_install}

%if %{with tests}
%check
%{?with_python2:PYTHONPATH=%{buildroot}%{python2_sitelib} py.test-%{python2_version} --verbose}
%{?with_python3:PYTHONPATH=%{buildroot}%{python3_sitelib} py.test-%{python3_version} --verbose}
%endif

%if %{with python2}
%files -n python2-%{pkgname}
%license LICENSE
%doc README
%{python2_sitelib}/%{libname}
%{python2_sitelib}/%{eggname}-%{version}-py%{python2_version}.egg-info
%endif

%if %{with python3}
%files -n python%{python3_pkgversion}-%{pkgname}
%license LICENSE
%doc README
%{python3_sitelib}/%{libname}
%{python3_sitelib}/%{eggname}-%{version}-py%{python3_version}.egg-info
%endif

%changelog
%autochangelog
