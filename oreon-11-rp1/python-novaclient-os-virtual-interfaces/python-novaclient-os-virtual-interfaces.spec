%global source0_hash 6d39ff4174496a0f795d11f20240805a16bbf452091cf8eb9bd1d5ae2fca449d
%global srcname os_virtual_interfacesv2_python_novaclient_ext
%global pkgname novaclient-os-virtual-interfaces
Name:		python-%{pkgname}
Version:	0.20
Release:        1%{?dist}
Summary:        Adds Virtual Interfaces support to python-novaclient
License:	Apache-2.0
URL:		http://pypi.python.org/pypi/%{srcname}
Source0:        https://files.pythonhosted.org/packages/source/o/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:	noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-novaclient
# /oreon:deps
%description
%{summary}

%package -n python3-%{pkgname}
Summary:        Adds Virtual Interfaces support to python-novaclient
BuildRequires:	python3-novaclient
Requires:	python3-novaclient
%{?python_provide:%python_provide python3-%{pkgname}}
%description -n python3-%{pkgname}
%{summary}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%build

%py3_build
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-novaclient-os-virtual-interfaces -f %{oreon_filedir}/python3-novaclient-os-virtual-interfaces.list

%changelog

%autochangelog
