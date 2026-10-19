%global source0_hash 371891c27e4c2b5bb5cef609f8b5d50fbe50ee7d8197b6850a05c7c6bf9347b9
%global srcname colcon-installed-package-information
Name:           python-%{srcname}
Version:        0.2.1
Release:        8%{?dist}
Summary:        Extensions for colcon to inspect packages which have already been installed
License:        Apache-2.0
URL:            https://github.com/colcon/%{srcname}
Source0:        https://github.com/colcon/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
Patch0:         %{name}-0.2.1-pytest-compat.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-colcon-core
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
# /oreon:deps
%description
Extensions for colcon-core to inspect packages which have already been
installed.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        Extensions for colcon to inspect packages which have already been installed
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pytest -m 'not linter' test
%files -f %{oreon_filedir}/main.list
%files -n python3-colcon-installed-package-information -f %{oreon_filedir}/python3-colcon-installed-package-information.list

%changelog

%autochangelog
