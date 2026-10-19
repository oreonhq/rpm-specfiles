%global source0_hash 181e1484b6a8ab5cff0ef37739150c566f4a72f2ab0dcb79660b6cee69c137a9
Name:           python-blurhash
Version:        1.1.5
Release:        1%{?dist}
Summary:        Pure-Python implementation of the blurhash algorithm.
License:        MIT
URL:            https://github.com/halcy/blurhash-python
Source0:        https://files.pythonhosted.org/packages/source/b/blurhash/blurhash-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-blurhash = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-blurhash
Summary:        Pure-Python implementation of the blurhash algorithm.
%description -n python3-blurhash

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir blurhash-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-blurhash usr/lib/python3*/site-packages/blurhash* usr/lib64/python3*/site-packages/blurhash* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/blurhash* usr/lib64/python3*/site-packages/blurhash* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-blurhash -f %{oreon_filedir}/python3-blurhash.list

%changelog

%autochangelog
