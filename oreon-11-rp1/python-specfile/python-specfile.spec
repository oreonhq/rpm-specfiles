%global source0_hash 2538321e754b546fef82ec2f853c328a4d5d56334dd3ac15b618f9b803282537
Name:           python-specfile
Version:        0.41.1
Release:        1%{?dist}
Summary:        A library for parsing and manipulating RPM spec files.
License:        MIT
URL:            https://github.com/packit/specfile
Source0:        https://files.pythonhosted.org/packages/source/s/specfile/specfile-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 45
BuildRequires:  python3dist(setuptools-scm[toml]) >= 7
Requires:       python3-specfile = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-specfile
Summary:        A library for parsing and manipulating RPM spec files.
%description -n python3-specfile

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir specfile-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-specfile usr/lib/python3*/site-packages/specfile* usr/lib64/python3*/site-packages/specfile* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/specfile* usr/lib64/python3*/site-packages/specfile* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-specfile -f %{oreon_filedir}/python3-specfile.list

%changelog

%autochangelog
