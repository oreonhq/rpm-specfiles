%global source0_hash d79943d153f5f6bfbe3f55a5ec611985184bda37fcedb3ecc75322d82ae6ad3b
Name:           python-unicodedata2
Version:        17.0.1
Release:        1%{?dist}
Summary:        Unicodedata backport updated to the latest Unicode version.
License:        ...
URL:            http://github.com/fonttools/unicodedata2
Source0:        https://files.pythonhosted.org/packages/source/u/unicodedata2/unicodedata2-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-unicodedata2 = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-unicodedata2
Summary:        Unicodedata backport updated to the latest Unicode version.
%description -n python3-unicodedata2

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir unicodedata2-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-unicodedata2 usr/lib/python3*/site-packages/unicodedata2* usr/lib64/python3*/site-packages/unicodedata2* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/unicodedata2* usr/lib64/python3*/site-packages/unicodedata2* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-unicodedata2 -f %{oreon_filedir}/python3-unicodedata2.list

%changelog

%autochangelog
