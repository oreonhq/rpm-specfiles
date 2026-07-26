%global source0_hash 9c9c788ae03a088d0c03a9a59ff7ac6c492caadd4942d4fc58795ee859fc228f

%global pypi_name python-digitalocean
%global pkgname digitalocean

%bcond_without python3

Name:           python-%{pkgname}
Version:        1.17.0
Release:        20%{?dist}
Summary:        Easy access to Digital Ocean APIs to deploy droplets, images and more

# Automatically converted from old format: LGPLv3 - review is highly recommended.
License:        LGPL-3.0-only
URL:            https://pypi.python.org/pypi/python-digitalocean
Source0:        https://github.com/koalalorenzo/%{pypi_name}/archive/v%{version}.tar.gz#/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-responses

%description
Easy access to Digital Ocean APIs to deploy droplets, images and
more.

%package -n python3-%{pkgname}
Requires:       python3-jsonpickle
Requires:       python3-requests

Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pkgname}}

%description -n python3-%{pkgname}
Easy access to Digital Ocean APIs to deploy droplets, images and
more.

This is the Python 3 version of the package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%check
%pytest -k "not TestFirewall"

%install
%pyproject_install
%pyproject_save_files -l %{pkgname}

%files -n python3-%{pkgname} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
