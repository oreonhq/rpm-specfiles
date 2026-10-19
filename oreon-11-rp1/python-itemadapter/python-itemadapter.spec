%global source0_hash 2655c8c50f1a8405c9fa74b8cdc4da7fec541ca217bc821b90acc8451c98a9d2
%global pkg_name itemadapter
%global desc %{expand:
The ItemAdapter class is a wrapper for data container objects,
providing a common interface to handle objects of different
types in an uniform manner, regardless of their underlying implementation.}
Name:		python-itemadapter
Version:	0.10.0
Release:        1%{?dist}
Summary:        The ItemAdapter class is a wrapper for data container object
License:	LicenseRef-Callaway-BSD
URL:		https://github.com/scrapy/itemadapter
Source0:        https://files.pythonhosted.org/packages/source/%/%pkg_name/%pkg_name-%{version}.tar.gz
BuildArch:	noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description
%{desc}

%package -n python3-%{pkg_name}
Summary:        The ItemAdapter class is a wrapper for data container object
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
Requires:	python3-attrs
%py_provides  python3-%{pkg_name}
%description -n python3-%{pkg_name}
%{desc}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pkg_name}-%{version}

%build

%py3_build
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-itemadapter -f %{oreon_filedir}/python3-itemadapter.list

%changelog

%autochangelog
