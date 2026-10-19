%global source0_hash 49e9380d7d2905463583bafe285e818c7366a9ed7b3aee221c1ac79c905d8bc0
Name:           python-soupsieve
Version:        2.10
Release:        1%{?dist}
Summary:        A modern CSS selector implementation for Beautiful Soup.
License:        MIT
URL:            https://github.com/facelessuser/soupsieve
Source0:        https://files.pythonhosted.org/packages/source/s/soupsieve/soupsieve-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatchling) >= 1.26
Requires:       python3-soupsieve = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-soupsieve
Summary:        A modern CSS selector implementation for Beautiful Soup.
%description -n python3-soupsieve

%prep
%global oreon_srcdir soupsieve-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-soupsieve usr/lib/python3*/site-packages/soupsieve* usr/lib64/python3*/site-packages/soupsieve* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/soupsieve* usr/lib64/python3*/site-packages/soupsieve* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-soupsieve -f %{oreon_filedir}/python3-soupsieve.list

%changelog

%autochangelog
