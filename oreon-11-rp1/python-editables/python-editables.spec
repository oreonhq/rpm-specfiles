%global source0_hash 766d9b40616dbcf5cc920e9db26dd915de999cfab75768ff05b3ebf9c389acb2
Name:           python-editables
Version:        0.6
Release:        1%{?dist}
Summary:        Editable installations
License:        MIT
URL:            https://github.com/pfmoore/editables
Source0:        https://github.com/pfmoore/editables/archive/%{version}/editables-%{version}.tar.gz
BuildArch:      noarch
%global common_description %{expand:
A Python library for creating “editable wheels”
This library supports the building of wheels which, when installed, will expose
packages in a local directory on sys.path in “editable mode”. In other words,
changes to the package source will be reflected in the package visible to
Python, without needing a reinstall.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) >= 3.3
Requires:       python3-editables = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n python3-editables
Summary:        Editable installations
Obsoletes:      python-editables-doc < 0.6-5
%description -n python3-editables %{common_description}

%prep
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-editables usr/lib/python3*/site-packages/editables* usr/lib64/python3*/site-packages/editables* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/editables* usr/lib64/python3*/site-packages/editables* usr/bin/*

%check

%pytest
%files
%files -n python3-editables -f %{oreon_filedir}/python3-editables.list

%changelog

%autochangelog
