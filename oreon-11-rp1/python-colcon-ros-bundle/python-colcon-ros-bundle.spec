%global source0_hash 14d3e995939a63c088f320992c2c6be809be6b4808c97477568048fb318497a3

%global srcname colcon-ros-bundle

Name:           python-%{srcname}
Version:        0.1.0
Release:        20%{?dist}
Summary:        Plugin for colcon to bundle ros applications

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://colcon.readthedocs.io
Source0:        https://github.com/colcon/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

# Submitted upstream as colcon/colcon-ros-bundle#51
Patch0:         %{name}-0.1.0-unittest-mock.patch

BuildArch:      noarch

%description
This package is a plugin to colcon-core, that contains extensions for
colcon-bundle.

With this package you can use colcon bundle to create bundles of ROS
applications. A bundle is a portable environment that allows for execution of
the bundled application on a Linux host that does not have the application or
its dependencies installed in the root filesystem.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-colcon-bundle >= 0.0.18
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-rosdep >= 0.14.0
BuildRequires:  python%{python3_pkgversion}-setuptools >= 30.3.0
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%if !0%{?rhel} || 0%{?rhel} >= 8
BuildRequires:  python%{python3_pkgversion}-pytest-asyncio
%endif

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-colcon-bundle >= 0.0.18
Requires:       python%{python3_pkgversion}-colcon-ros >= 0.3.5
Requires:       python%{python3_pkgversion}-rosdep >= 0.14.0
Requires:       python%{python3_pkgversion}-setuptools >= 30.3.0
%endif

%description -n python%{python3_pkgversion}-%{srcname}
This package is a plugin to colcon-core, that contains extensions for
colcon-bundle.

With this package you can use colcon bundle to create bundles of ROS
applications. A bundle is a portable environment that allows for execution of
the bundled application on a Linux host that does not have the application or
its dependencies installed in the root filesystem.

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
%{python3_sitelib}/colcon_ros_bundle/
%{python3_sitelib}/colcon_ros_bundle-%{version}-py%{python3_version}.egg-info/

%changelog
%autochangelog
