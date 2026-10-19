%global source0_hash 2afbaaf2503afe912de0881e4c577383e6f90f8762931fb4d32f2b54123ce450
Name:           python-sievelib
Version:        1.5.0
Release:        1%{?dist}
Summary:        Client-side SIEVE library
License:        MIT
URL:            https://github.com/tonioo/sievelib
Source0:        https://files.pythonhosted.org/packages/source/s/sievelib/sievelib-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0
BuildRequires:  python3dist(setuptools-scm[toml]) >= 6.4
Requires:       python3-sievelib = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-sievelib
Summary:        Client-side SIEVE library
%description -n python3-sievelib

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir sievelib-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-sievelib usr/lib/python3*/site-packages/sievelib* usr/lib64/python3*/site-packages/sievelib* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/sievelib* usr/lib64/python3*/site-packages/sievelib* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-sievelib -f %{oreon_filedir}/python3-sievelib.list

%changelog

%autochangelog
