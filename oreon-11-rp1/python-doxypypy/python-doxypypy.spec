%global source0_hash 671ac8bb06927b78a924726187f6e3dde272ae960856ffc053e6e5bea42cd09e
Name:           python-doxypypy
Version:        0.8.8.7
Release:        1%{?dist}
Summary:        A Doxygen filter for Python
License:        GPL-2.0-only
URL:            https://github.com/Feneric/doxypypy
Source0:        https://files.pythonhosted.org/packages/source/d/doxypypy/doxypypy-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-doxypypy = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-doxypypy
Summary:        A Doxygen filter for Python
%description -n python3-doxypypy

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir doxypypy-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
rm -rf %{buildroot}%{python3_sitelib}/doxypypy/test
sed -i '\|/doxypypy/test/|d' %{pyproject_files}
%oreon_autofiles python3-doxypypy usr/lib/python3*/site-packages/doxypypy* usr/lib64/python3*/site-packages/doxypypy* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/doxypypy* usr/lib64/python3*/site-packages/doxypypy* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-doxypypy -f %{oreon_filedir}/python3-doxypypy.list

%changelog

%autochangelog
