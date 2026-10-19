%global source0_hash c9d3aa6825fdd06af7ebb05b4ef291d2db63e62bb1f9b7d9b71354be9d362714
Name:           python-anytree
Version:        2.13.0
Release:        1%{?dist}
Summary:        Powerful and Lightweight Python Tree Data Structure with various plugins
License:        Apache-2.0
URL:            https://github.com/c0fec0de/anytree
Source0:        https://files.pythonhosted.org/packages/source/a/anytree/anytree-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-anytree = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-anytree
Summary:        Powerful and Lightweight Python Tree Data Structure with various plugins
%description -n python3-anytree

%prep
%global oreon_srcdir anytree-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-anytree usr/lib/python3*/site-packages/anytree* usr/lib64/python3*/site-packages/anytree* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/anytree* usr/lib64/python3*/site-packages/anytree* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-anytree -f %{oreon_filedir}/python3-anytree.list

%changelog

%autochangelog
