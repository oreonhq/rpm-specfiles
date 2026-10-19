%global source0_hash 52799ad96fcf92aab2fc96a9e03869bbf1a634300f7cd91c38dbfd51f639f6fa
Name:           python-faker
Version:        40.39.0
Release:        1%{?dist}
Summary:        Faker is a Python package that generates fake data for you.
License:        MIT
URL:            https://github.com/joke2k/faker
Source0:        https://files.pythonhosted.org/packages/source/f/faker/faker-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-faker = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-faker
Summary:        Faker is a Python package that generates fake data for you.
%description -n python3-faker

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir faker-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-faker usr/lib/python3*/site-packages/faker* usr/lib64/python3*/site-packages/faker* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/faker* usr/lib64/python3*/site-packages/faker* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-faker -f %{oreon_filedir}/python3-faker.list

%changelog

%autochangelog
