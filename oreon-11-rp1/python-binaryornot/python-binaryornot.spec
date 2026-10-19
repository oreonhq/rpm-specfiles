%global source0_hash cc8d57cfa71d74ff8c28a7726734d53a851d02fad9e3a5581fb807f989f702f0
Name:           python-binaryornot
Version:        0.6.0
Release:        1%{?dist}
Summary:        Ultra-lightweight pure Python package to check if a file is binary or text.
License:        MIT
URL:            https://github.com/binaryornot/binaryornot
Source0:        https://files.pythonhosted.org/packages/source/b/binaryornot/binaryornot-%{version}.tar.gz
BuildArch:      noarch
Patch:              38dee57986c6679d99.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-binaryornot = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-binaryornot
Summary:        Ultra-lightweight pure Python package to check if a file is binary or text.
%description -n python3-binaryornot

%prep
%global oreon_srcdir binaryornot-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-binaryornot usr/lib/python3*/site-packages/binaryornot* usr/lib64/python3*/site-packages/binaryornot* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/binaryornot* usr/lib64/python3*/site-packages/binaryornot* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-binaryornot -f %{oreon_filedir}/python3-binaryornot.list

%changelog

%autochangelog
