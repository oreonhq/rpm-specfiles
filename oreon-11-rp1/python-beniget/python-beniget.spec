%global source0_hash e7af11fa8ec7de3d3eb3d98b1e722d15d44017d8b35d8aa11d54f6719b312f22
Name:           python-beniget
Version:        0.5.0
Release:        1%{?dist}
Summary:        Extract semantic information about static Python code
License:        ...
URL:            https://github.com/serge-sans-paille/beniget/
Source0:        https://files.pythonhosted.org/packages/source/b/beniget/beniget-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-beniget = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-beniget
Summary:        Extract semantic information about static Python code
%description -n python3-beniget

%prep
%global oreon_srcdir beniget-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-beniget usr/lib/python3*/site-packages/beniget* usr/lib64/python3*/site-packages/beniget* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/beniget* usr/lib64/python3*/site-packages/beniget* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-beniget -f %{oreon_filedir}/python3-beniget.list

%changelog

%autochangelog
