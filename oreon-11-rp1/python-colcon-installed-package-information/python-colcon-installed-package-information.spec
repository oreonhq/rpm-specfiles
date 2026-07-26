%global source0_hash 371891c27e4c2b5bb5cef609f8b5d50fbe50ee7d8197b6850a05c7c6bf9347b9

%global srcname colcon-installed-package-information

Name:           python-%{srcname}
Version:        0.2.1
Release:        8%{?dist}
Summary:        Extensions for colcon to inspect packages which have already been installed

License:        Apache-2.0
URL:            https://github.com/colcon/%{srcname}
Source0:        https://github.com/colcon/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

# Not submitted upstream - compatibility with pytest < 3.9.0
Patch0:         %{name}-0.2.1-pytest-compat.patch

BuildArch:      noarch

%description
Extensions for colcon-core to inspect packages which have already been
installed.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-colcon-core
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-setuptools >= 30.3.0
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-colcon-core
%endif

%description -n python%{python3_pkgversion}-%{srcname}
These colcon extensions provide a mechanism which can be used for getting
information about packages outside of the workspace, which have already been
built and installed prior to the current operation.

In general, they work similarly to and are based on the
PackageDiscoveryExtensionPoint and PackageAugmentationExtensionPoint
extensions provided by colcon_core.

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
%{python3_sitelib}/colcon_installed_package_information/
%{python3_sitelib}/colcon_installed_package_information-%{version}-py%{python3_version}.egg-info/

%changelog
%autochangelog
