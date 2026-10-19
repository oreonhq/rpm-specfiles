%global source0_hash 87d3480dbb083c1d736222511a8cf380012a8176c2456d01ef483242abbbcf8c
Name:           python-incremental
Version:        24.11.0
Release:        1%{?dist}
Summary:        A CalVer version manager that supports the future.
License:        MIT
URL:            https://github.com/twisted/incremental
Source0:        https://files.pythonhosted.org/packages/source/i/incremental/incremental-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-incremental = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-incremental
Summary:        A CalVer version manager that supports the future.
%description -n python3-incremental

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir incremental-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-incremental usr/lib/python3*/site-packages/incremental* usr/lib64/python3*/site-packages/incremental* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/incremental* usr/lib64/python3*/site-packages/incremental* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-incremental -f %{oreon_filedir}/python3-incremental.list

%changelog

%autochangelog
