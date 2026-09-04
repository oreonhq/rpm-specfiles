%global source0_hash 2b0b8d0dfc94c95e0cf47cf6d206ce11e116808875409e21d06fefef82b353aa

%global srcname colcon-notification

Name:           python-%{srcname}
Version:        0.3.1
Release:        1%{?dist}
Summary:        Extension for colcon to provide status notifications

License:        Apache-2.0
URL:            https://colcon.readthedocs.io
Source0:        https://github.com/colcon/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

# Taken from sources - disables install of data files per platform
Patch0:         %{name}-0.2.8-data-files.patch

BuildArch:      noarch

%description
An extension for colcon-core to provide status notifications.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-colcon-core >= 0.3.7
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-setuptools >= 30.3.0
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-colcon-core >= 0.3.7
Requires:       python%{python3_pkgversion}-notify2
%endif

%description -n python%{python3_pkgversion}-%{srcname}
An extension for colcon-core to provide status notifications.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%build
BUILD_DEBIAN_PACKAGE=1 \
    %py3_build

%install
BUILD_DEBIAN_PACKAGE=1 \
    %py3_install

%check
%pytest -m 'not linter' test

%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/colcon_notification/
%{python3_sitelib}/colcon_notification-%{version}-py%{python3_version}.egg-info/

%changelog
%autochangelog
