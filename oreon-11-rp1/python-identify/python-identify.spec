%global source0_hash 6be5020c38fcb07da56c53733538a3081ea5aa70d36a156f83044bfbf9173842
Name:           python-identify
Version:        2.6.19
Release:        1%{?dist}
Summary:        File identification library for Python
License:        MIT
URL:            https://github.com/pre-commit/identify
Source0:        https://files.pythonhosted.org/packages/source/i/identify/identify-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-identify = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-identify
Summary:        File identification library for Python
%description -n python3-identify

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir identify-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-identify usr/lib/python3*/site-packages/identify* usr/lib64/python3*/site-packages/identify* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/identify* usr/lib64/python3*/site-packages/identify* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-identify -f %{oreon_filedir}/python3-identify.list

%changelog

%autochangelog
