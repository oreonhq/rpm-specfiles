%global source0_hash 4a4aa9a2d9dd08bb60945e9a74c17f723e92dfffd1c2a721299963cdad0f0582

%global srcname colcon-ros-bazel

Name:           python-%{srcname}
Version:        0.0.1
Release:        28%{?dist}
Summary:        Extension for colcon to support ROS2 Bazel packages

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://colcon.readthedocs.io
Source0:        https://github.com/colcon/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
An extension for colcon-core to support ROS2 Bazel projects.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-setuptools >= 30.3.0
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-colcon-bazel >= 0.1.0
Requires:       python%{python3_pkgversion}-colcon-core
Requires:       python%{python3_pkgversion}-colcon-library-path
Requires:       python%{python3_pkgversion}-colcon-ros >= 0.3.2
%endif # __pythondist_requires

%description -n python%{python3_pkgversion}-%{srcname}
An extension for colcon-core to support ROS2 Bazel projects.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{__python3} -m pytest \
    --ignore=test/test_spell_check.py \
    --ignore=test/test_flake8.py \
    test

%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/colcon_ros_bazel/
%{python3_sitelib}/colcon_ros_bazel-%{version}-py%{python3_version}.egg-info/

%changelog
%autochangelog
