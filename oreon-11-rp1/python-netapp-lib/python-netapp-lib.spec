%global source0_hash d60e050923324bc4fa17f4fc04ea9a9388759c98acf20f6368e96e0381533690

# what it's called on pypi
%global srcname netapp-lib
# what it's imported as
%global libname netapp_lib
# name of egg info directory
%global eggname %{libname}
# package name fragment
%global pkgname %{srcname}

%global common_description %{expand:
Library to allow Ansible deployments to interact with NetApp storage systems}

Name:           python-%{srcname}
Version:        2021.6.25
Release:        18%{?dist}
Summary:        NetApp library for Python

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://pypi.org/project/netapp-lib/
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description %{common_description}

%package -n python%{python3_pkgversion}-%{pkgname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pkgname}}

%description -n python%{python3_pkgversion}-%{pkgname} %{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}
rm -rf %{eggname}.egg-info

%build
%py3_build

%install
%py3_install

# Note that there is no %%files section for the unversioned python module
%files -n python%{python3_pkgversion}-%{srcname}
%doc README.rst
%license LICENSE.txt
%exclude /usr/LICENSE.txt
%{python3_sitelib}/%{libname}/
%{python3_sitelib}/%{eggname}-%{version}-py%{python3_version}.egg-info/

%changelog
%autochangelog
