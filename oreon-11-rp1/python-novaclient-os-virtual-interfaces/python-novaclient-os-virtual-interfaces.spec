%global source0_hash 6d39ff4174496a0f795d11f20240805a16bbf452091cf8eb9bd1d5ae2fca449d

%global srcname os_virtual_interfacesv2_python_novaclient_ext
%global pkgname novaclient-os-virtual-interfaces

Name:		python-%{pkgname}
Version:	0.20
Release:	35%{dist}
Summary:	Adds Virtual Interfaces support to python-novaclient
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:	Apache-2.0
URL:		http://pypi.python.org/pypi/%{srcname}
Source0:	https://files.pythonhosted.org/packages/source/o/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	python3-devel

%description
%{summary}

%package -n python3-%{pkgname}
Summary:	%{summary}
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

%files -n python3-%{pkgname}
%doc README.rst
%{python3_sitelib}/%{srcname}*
%{python3_sitelib}/__pycache__/%{srcname}*

%changelog
%autochangelog
