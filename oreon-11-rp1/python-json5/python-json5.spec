%global source0_hash 7424d1f1eb1d56da6e3d70643f53619862b4ce81440bdb8ecfd6f875e5ba4a71
Name:           python-json5
Version:        0.15.0
Release:        1%{?dist}
Summary:        A Python implementation of the JSON5 data format.
License:        ...
URL:            https://github.com/dpranke/pyjson5
Source0:        https://files.pythonhosted.org/packages/source/j/json5/json5-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61
Requires:       python3-json5 = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-json5
Summary:        A Python implementation of the JSON5 data format.
%description -n python3-json5

%prep
%global oreon_srcdir json5-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-json5 usr/lib/python3*/site-packages/json5* usr/lib64/python3*/site-packages/json5* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/json5* usr/lib64/python3*/site-packages/json5* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-json5 -f %{oreon_filedir}/python3-json5.list

%changelog

%autochangelog
