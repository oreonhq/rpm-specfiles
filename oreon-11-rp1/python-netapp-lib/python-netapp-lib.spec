%global source0_hash d60e050923324bc4fa17f4fc04ea9a9388759c98acf20f6368e96e0381533690
%global srcname netapp-lib
%global libname netapp_lib
%global eggname %{libname}
%global pkgname %{srcname}
%global common_description %{expand:
Library to allow Ansible deployments to interact with NetApp storage systems}
Name:           python-%{srcname}
Version:        2021.6.25
Release:        1%{?dist}
Summary:        NetApp library for Python
License:        Apache-2.0
URL:            https://pypi.org/project/netapp-lib/
Source0:        https://files.pythonhosted.org/packages/source/p/python-netapp-lib/python-netapp-lib-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description %{common_description}

%package -n python%{python3_pkgversion}-%{pkgname}
Summary:        NetApp library for Python
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
%doc README.rst
%license LICENSE.txt
%exclude /usr/LICENSE.txt
%{python3_sitelib}/%{libname}/
%{python3_sitelib}/%{eggname}-%{version}-py%{python3_version}.egg-info/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-netapp-lib -f %{oreon_filedir}/python3-netapp-lib.list

%changelog

%autochangelog
