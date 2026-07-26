%global source0_hash 2e17a82041af4f831a63806d082ca78727fda888a1fafe32ca45f769cf6554f8

%global srcname catkin-sphinx

Name:           python-%{srcname}
Version:        0.3.2
Release:        7%{?dist}
Summary:        Sphinx extension for Catkin projects

License:        BSD-3-Clause
URL:            https://github.com/ros-infrastructure/%{srcname}
Source0:        https://github.com/ros-infrastructure/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
Sphinx extension for Catkin projects that provides a custom ROS theme and a
Sphinx domain for CMake.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
Requires:       python%{python3_pkgversion}-sphinx
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

Recommends:     python%{python3_pkgversion}-docutils
Recommends:     python%{python3_pkgversion}-pygments

%description -n python%{python3_pkgversion}-%{srcname}
Sphinx extension for Catkin projects that provides a custom ROS theme and a
Sphinx domain for CMake.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python%{python3_pkgversion}-%{srcname}
%doc README.md
%{python3_sitelib}/catkin_sphinx-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/catkin_sphinx/

%changelog
%autochangelog
