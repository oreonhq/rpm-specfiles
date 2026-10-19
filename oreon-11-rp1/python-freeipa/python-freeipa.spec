%global source0_hash 191e9fa1c6924b9e88b48747ed05383c22ef023ece8ba0d09b3634189204a55f
%{?python_enable_dependency_generator}
%global pypi_name python-freeipa
%global srcname freeipa
Name:           python-%{srcname}
Version:        4.13.1
Release:        1%{?dist}
Summary:        Lightweight FreeIPA client
License:        MIT
URL:            https://python-freeipa.readthedocs.io/
Source0:        https://github.com/opennode/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(responses)
BuildRequires:  python3dist(setuptools)
# /oreon:deps
%description
python-freeipa is lightweight FreeIPA client.

%package -n     python%{python3_pkgversion}-%{srcname}
Summary:        Lightweight FreeIPA client
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
%description -n python%{python3_pkgversion}-%{srcname}
python-freeipa is lightweight FreeIPA client.

This package provides the Python %{python3_version} variant.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# Fix version
sed -e "s/version='1.0.6',/version='%{version}',/" -i setup.py

%build

%py3_build
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pytest src/python_freeipa/tests/*.py
%files -f %{oreon_filedir}/main.list
%files -n python3-freeipa -f %{oreon_filedir}/python3-freeipa.list

%changelog

%autochangelog
