%global source0_hash 48ab6704f5393bf400b02f775c40302edfa2fd58f7cfa7c2702c74f23f150edc

%global srcname rosinstall_generator

Name:           python-%{srcname}
Version:        0.1.23
Release:        14%{?dist}
Summary:        Generates rosinstall files

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://wiki.ros.org/%{srcname}
Source0:        https://github.com/ros-infrastructure/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
The rosinstall_generator generates rosinstall files containing information
about repositories with ROS packages/stacks.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-catkin_pkg >= 0.1.28
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-rosdistro >= 0.7.3
BuildRequires:  python%{python3_pkgversion}-rospkg
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-yaml
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-catkin_pkg >= 0.1.28
Requires:       python%{python3_pkgversion}-rosdistro >= 0.7.3
Requires:       python%{python3_pkgversion}-rospkg
Requires:       python%{python3_pkgversion}-setuptools
Requires:       python%{python3_pkgversion}-yaml
%endif

%description -n python%{python3_pkgversion}-%{srcname}
The rosinstall_generator generates rosinstall files containing information
about repositories with ROS packages/stacks.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install
mv %{buildroot}%{_bindir}/%{srcname} %{buildroot}%{_bindir}/%{srcname}-%{python3_version}
ln -s %{srcname}-%{python3_version} %{buildroot}%{_bindir}/%{srcname}

%check
%pytest test

%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/
%{_bindir}/%{srcname}
%{_bindir}/%{srcname}-%{python3_version}

%changelog
%autochangelog
