%global source0_hash 5f0b9e53c1e82e88c10d7c180069363980136b9d7a8306c4dca4f760d60c39f0
Name:           python-lz4
Version:        4.4.5
Release:        1%{?dist}
Summary:        LZ4 Bindings for Python
License:        ...
URL:            https://github.com/python-lz4/python-lz4
Source0:        https://files.pythonhosted.org/packages/source/l/lz4/lz4-%{version}.tar.gz
Patch:          python-lz4-deps.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 45
BuildRequires:  python3dist(setuptools-scm[toml]) >= 6.2
Requires:       python3-lz4 = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-lz4
Summary:        LZ4 Bindings for Python
%description -n python3-lz4

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir lz4-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-lz4 usr/lib/python3*/site-packages/lz4* usr/lib64/python3*/site-packages/lz4* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/lz4* usr/lib64/python3*/site-packages/lz4* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-lz4 -f %{oreon_filedir}/python3-lz4.list

%changelog

%autochangelog
