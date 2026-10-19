%global source0_hash 9c9c788ae03a088d0c03a9a59ff7ac6c492caadd4942d4fc58795ee859fc228f
%global pypi_name python-digitalocean
%global pkgname digitalocean
%bcond_without python3
Name:           python-%{pkgname}
Version:        1.17.0
Release:        1%{?dist}
Summary:        Easy access to Digital Ocean APIs to deploy droplets, images and more
License:        LGPL-3.0-only
URL:            https://pypi.python.org/pypi/python-digitalocean
Source0:        https://github.com/koalalorenzo/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-digitalocean = %{version}-%{release}
# /oreon:deps
%description
Easy access to Digital Ocean APIs to deploy droplets, images and
more.

%package -n python3-%{pkgname}
Requires:       python3-jsonpickle
Requires:       python3-requests
Summary:        Easy access to Digital Ocean APIs to deploy droplets, images and more
%{?python_provide:%python_provide python3-%{pkgname}}
%description -n python3-%{pkgname}
Easy access to Digital Ocean APIs to deploy droplets, images and
more.

This is the Python 3 version of the package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%pyproject_wheel
%check

%pytest -k "not TestFirewall"
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/digitalocean* usr/lib64/python3*/site-packages/digitalocean* usr/bin/*

%files
%files -n python3-digitalocean -f %{oreon_filedir}/python3-digitalocean.list

%changelog

%autochangelog
