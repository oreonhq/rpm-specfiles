%global source0_hash 7fd6973616c88689800ff3de17ce929c6dfe34fedf6e2c142e2b7ceab8b2ebbd
Name:           python-esbonio
Version:        2.1.0
Release:        1%{?dist}
Summary:        A language server for sphinx/docutils based documentation projects.
License:        MIT
URL:            https://github.com/swyddfa/esbonio
Source0:        https://files.pythonhosted.org/packages/source/e/esbonio/esbonio-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-esbonio = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-esbonio
Summary:        A language server for sphinx/docutils based documentation projects.
%description -n python3-esbonio

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir esbonio-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-esbonio usr/lib/python3*/site-packages/esbonio* usr/lib64/python3*/site-packages/esbonio* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/esbonio* usr/lib64/python3*/site-packages/esbonio* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-esbonio -f %{oreon_filedir}/python3-esbonio.list

%changelog

%autochangelog
