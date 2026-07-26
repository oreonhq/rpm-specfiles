%global source0_hash 0cb0a90d5207e19057112bafac2f44226f0b4141bd1b2569ea6a7c3c348dcf01

%global srcname colcon-bundle

Name:           python-%{srcname}
Version:        0.1.3
Release:        13%{?dist}
Summary:        Plugin to bundle built software for the colcon command line tool

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://colcon.readthedocs.io
Source0:        https://github.com/colcon/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
This package is a plugin to colcon-core. It provides functionality to bundle a
built workspace. A bundle is a portable environment which can be moved to a
different linux system and executed as if the contents of the bundle was
installed locally.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-colcon-core >= 0.3.15
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-jinja2 >= 2.9.0
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-setuptools >= 30.3.0
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%if !0%{?rhel} || 0%{?rhel} >= 8
BuildRequires:  python%{python3_pkgversion}-pytest-asyncio
%endif

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-colcon-bash >= 0.4.2
Requires:       python%{python3_pkgversion}-colcon-core >= 0.3.15
Requires:       python%{python3_pkgversion}-colcon-python-setup-py >= 0.2.1
Requires:       python%{python3_pkgversion}-distro >= 1.2.0
Requires:       python%{python3_pkgversion}-jinja2 >= 2.9.0
Requires:       python%{python3_pkgversion}-setuptools >= 30.3.0
%endif

%description -n python%{python3_pkgversion}-%{srcname}
This package is a plugin to colcon-core. It provides functionality to bundle a
built workspace. A bundle is a portable environment which can be moved to a
different linux system and executed as if the contents of the bundle was
installed locally.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{__python3} -m pytest \
    --ignore=test/test_flake8.py \
    test

%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc NOTICE README.md
%{python3_sitelib}/colcon_bundle/
%{python3_sitelib}/colcon_bundle-%{version}-py%{python3_version}.egg-info/

%changelog
%autochangelog
