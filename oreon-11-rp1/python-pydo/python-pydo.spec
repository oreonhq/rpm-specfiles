%global source0_hash af53bb4324ae51811254fd2e777db32dc20040fda0a04aa6a132298f98b1e3fc
Name:           python-pydo
Version:        0.40.0
Release:        1%{?dist}
Summary:        The official client for interacting with the DigitalOcean API
License:        Apache-2.0
URL:            https://github.com/digitalocean/pydo
Source0:        https://files.pythonhosted.org/packages/source/p/pydo/pydo-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) >= 1.0.0
Requires:       python3-pydo = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pydo
Summary:        The official client for interacting with the DigitalOcean API
%description -n python3-pydo

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir pydo-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pydo usr/lib/python3*/site-packages/pydo* usr/lib64/python3*/site-packages/pydo* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pydo* usr/lib64/python3*/site-packages/pydo* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pydo -f %{oreon_filedir}/python3-pydo.list

%changelog

%autochangelog
