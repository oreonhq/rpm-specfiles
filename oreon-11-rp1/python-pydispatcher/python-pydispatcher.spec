%global source0_hash b777c6ad080dc1bad74a4c29d6a46914fa6701ac70f94b0d66fbcfde62f5be31
%global pypi_name PyDispatcher
%global srcname pydispatcher
Name:           python-%{srcname}
Version:        2.0.7
Release:        1%{?dist}
Summary:        Multi-producer-multi-consumer signal dispatching mechanism
License:        LicenseRef-Callaway-BSD
URL:            http://pydispatcher.sourceforge.net
Source0:        https://files.pythonhosted.org/packages/source/P/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description
Dispatcher mechanism for creating event models. \

%package -n     python3-%{srcname}
Summary:        Multi-producer-multi-consumer signal dispatching mechanism
%{?python_provide:%python_provide python3-%{srcname}}
%description -n python3-%{srcname}
%{_description}

This package contains the Python 3 version of %{pypi_name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build

%py3_build
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%{__python3} -m unittest
%files -f %{oreon_filedir}/main.list
%files -n python3-pydispatcher -f %{oreon_filedir}/python3-pydispatcher.list

%changelog

%autochangelog
