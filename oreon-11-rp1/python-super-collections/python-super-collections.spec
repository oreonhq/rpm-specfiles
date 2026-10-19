%global source0_hash 0c8d8abacd9fad2c7c1c715f036c29f5db213f8cac65f24d45ecba12b4da187a
Name:           python-super-collections
Version:        0.6.2
Release:        1%{?dist}
Summary:        file: README.md
License:        MIT
URL:            https://github.com/fralau/super-collections
Source0:        https://files.pythonhosted.org/packages/source/s/super_collections/super_collections-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0
Requires:       python3-super-collections = %{version}-%{release}
# /oreon:deps
%package -n       python3-super-collections+test
Summary:        Metapackage for python3-super-collections test extras
Requires:       python3-super-collections = %{version}-%{release}
Requires:       python3dist(pytest) >= 7.0
Provides:       python3dist(super-collections[test]) = %{version}-%{release}

%description -n python3-super-collections+test
Metapackage for python3-super-collections test extras.

%description

%package -n     python3-super-collections
Summary:        file: README.md
%description -n python3-super-collections

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir super_collections-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-super-collections usr/lib/python3*/site-packages/super_collections* usr/lib64/python3*/site-packages/super_collections* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/super_collections* usr/lib64/python3*/site-packages/super_collections* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-super-collections -f %{oreon_filedir}/python3-super-collections.list

%changelog

%autochangelog
