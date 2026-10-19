%global source0_hash 7c944d9d2b688f14c4ef1b1d962dbaabd53dc05e3a04a89da62e2eece6a2ad5a
%global srcname colcon-python-setup-py
Name:           python-%{srcname}
Version:        0.2.9
Release:        1%{?dist}
Summary:        Extension for colcon to support Python packages with a setup.py file
License:        Apache-2.0
URL:            https://colcon.readthedocs.io
Source0:        https://github.com/colcon/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-colcon-core
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
# /oreon:deps
%description
An extension for colcon-core to identify packages with a setup.py file by
introspecting the arguments to the setup() function call of setuptools.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        Extension for colcon to support Python packages with a setup.py file
BuildRequires:  python%{python3_pkgversion}-colcon-core >= 0.6.1
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-setuptools >= 30.3.0
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-colcon-core >= 0.6.1
Requires:       python%{python3_pkgversion}-setuptools
%endif
%description -n python%{python3_pkgversion}-%{srcname}
An extension for colcon-core to identify packages with a setup.py file by
introspecting the arguments to the setup() function call of setuptools.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%build

%py3_build
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pytest -k 'not linter' test
%files -f %{oreon_filedir}/main.list
%files -n python3-colcon-python-setup-py -f %{oreon_filedir}/python3-colcon-python-setup-py.list

%changelog

%autochangelog
