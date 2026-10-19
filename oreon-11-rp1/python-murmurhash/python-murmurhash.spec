%global source0_hash 58e2b27b7847f9e2a6edf10b47a8c8dd70a4705f45dccb7bf76aeadacf56ba01
Name:           python-murmurhash
Version:        1.0.15
Release:        1%{?dist}
Summary:        Cython bindings for MurmurHash
License:        MIT
URL:            https://github.com/explosion/murmurhash
Source0:        https://files.pythonhosted.org/packages/source/m/murmurhash/murmurhash-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(cython) >= 3.1
Requires:       python3-murmurhash = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-murmurhash
Summary:        Cython bindings for MurmurHash
%description -n python3-murmurhash

%prep
%global oreon_srcdir murmurhash-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-murmurhash usr/lib/python3*/site-packages/murmurhash* usr/lib64/python3*/site-packages/murmurhash* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/murmurhash* usr/lib64/python3*/site-packages/murmurhash* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-murmurhash -f %{oreon_filedir}/python3-murmurhash.list

%changelog

%autochangelog
