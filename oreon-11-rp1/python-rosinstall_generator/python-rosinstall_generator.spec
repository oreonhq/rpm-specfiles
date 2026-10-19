%global source0_hash 48ab6704f5393bf400b02f775c40302edfa2fd58f7cfa7c2702c74f23f150edc
%global srcname rosinstall_generator
Name:           python-%{srcname}
Version:        0.1.23
Release:        14%{?dist}
Summary:        Generates rosinstall files
License:        LicenseRef-Callaway-BSD
URL:            http://wiki.ros.org/%{srcname}
Source0:        https://github.com/ros-infrastructure/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-catkin_pkg
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-rosdistro
BuildRequires:  python3-rospkg
BuildRequires:  python3-setuptools
BuildRequires:  python3-yaml
# /oreon:deps
%description
The rosinstall_generator generates rosinstall files containing information
about repositories with ROS packages/stacks.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        Generates rosinstall files
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pytest test
%files -f %{oreon_filedir}/main.list
%files -n python3-rosinstall_generator -f %{oreon_filedir}/python3-rosinstall_generator.list

%changelog

%autochangelog
