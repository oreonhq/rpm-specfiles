%global source0_hash f7f0a889c8fb80deaacb95e918d88e05148850a32d2b8eda28446291b2bf7c35
Name:           python-nanobind
Version:        3.0.1
Release:        1%{?dist}
Summary:        nanobind: tiny and efficient C++/Python bindings
License:        ...
URL:            https://github.com/wjakob/nanobind
Source0:        https://files.pythonhosted.org/packages/source/n/nanobind/nanobind-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(scikit-build-core) >= 0.10
Requires:       python3-nanobind = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-nanobind
Summary:        nanobind: tiny and efficient C++/Python bindings
%description -n python3-nanobind

%prep
%global oreon_srcdir nanobind-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-nanobind usr/lib/python3*/site-packages/nanobind* usr/lib64/python3*/site-packages/nanobind* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/nanobind* usr/lib64/python3*/site-packages/nanobind* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-nanobind -f %{oreon_filedir}/python3-nanobind.list

%changelog

%autochangelog
