%global source0_hash 4aee34ff36927065b30b9ff85d00108e1003d0ac78a3c90b7d4357b977dda80a

%global srcname colcon-ros

Name:           python-%{srcname}
Version:        0.5.0
Release:        7%{?dist}
Summary:        Extension for colcon to support ROS packages

License:        Apache-2.0
URL:            https://colcon.readthedocs.io
Source0:        https://github.com/colcon/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
An extension for colcon-core to support ROS packages.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-catkin_pkg >= 0.4.14
BuildRequires:  python%{python3_pkgversion}-colcon-core >= 0.7.0
BuildRequires:  python%{python3_pkgversion}-colcon-python-setup-py >= 0.2.4
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-setuptools >= 30.3.0
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-catkin_pkg >= 0.4.14
Requires:       python%{python3_pkgversion}-colcon-cmake >= 0.2.6
Requires:       python%{python3_pkgversion}-colcon-core >= 0.7.0
Requires:       python%{python3_pkgversion}-colcon-pkg-config
Requires:       python%{python3_pkgversion}-colcon-python-setup-py >= 0.2.4
Requires:       python%{python3_pkgversion}-colcon-recursive-crawl
%endif

%if !0%{?rhel} || 0%{?rhel} >= 8
Suggests:       dpkg-dev
%else
Requires:       dpkg-dev
%endif

%description -n python%{python3_pkgversion}-%{srcname}
An extension for colcon-core to support ROS packages.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
%pytest -m 'not linter' test

%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/colcon_ros/
%{python3_sitelib}/colcon_ros-%{version}-py%{python3_version}.egg-info/

%changelog
%autochangelog
