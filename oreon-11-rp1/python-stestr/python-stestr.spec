%global source0_hash b60495225fa783476252572adda29d33ae3706f95fc32564f78fb4e7c9e5df20
Name:           python-stestr
Version:        4.2.1
Release:        1%{?dist}
Summary:        A parallel Python test runner built around subunit
License:        Apache-2.0
URL:            https://stestr.readthedocs.io/en/stable/
Source0:        https://files.pythonhosted.org/packages/source/s/stestr/stestr-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
BuildRequires:  python3dist(flit-core) >= 3.12
Requires:       python3-stestr = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-stestr
Summary:        A parallel Python test runner built around subunit
# oreon:reqs
Requires:       python3dist(cliff) >= 2.8.0
Requires:       python3dist(fixtures) >= 3.0.0
Requires:       python3dist(python-subunit) >= 1.4.0
Requires:       python3dist(pyyaml) >= 3.10.0
Requires:       python3dist(testtools) >= 2.2.0
Requires:       python3dist(tomlkit) >= 0.11.6
Requires:       python3dist(voluptuous) >= 0.8.9
# /oreon:reqs
%description -n python3-stestr

%prep
%global oreon_srcdir stestr-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-stestr usr/lib/python3*/site-packages/stestr* usr/lib64/python3*/site-packages/stestr* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/stestr* usr/lib64/python3*/site-packages/stestr* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-stestr -f %{oreon_filedir}/python3-stestr.list

%changelog

%autochangelog
