%global source0_hash 669ccbb8545a4a67a6213a23ab6201368bb0c960d9d0861f236a9829f05b6abf
Name:           python-construct-classes
Version:        0.2.3
Release:        1%{?dist}
Summary:        Parse your binary structs into dataclasses
License:        MIT
URL:            https://github.com/matejcik/construct-classes
Source0:        https://files.pythonhosted.org/packages/source/c/construct_classes/construct_classes-%{version}.tar.gz
BuildArch:      noarch
Patch0:    https://patch-diff.githubusercontent.com/raw/matejcik/construct-classes/pull/2.patch#/only-include-license-documentation-for-sdist.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
BuildRequires:  python3dist(flit-core) >= 3.4
Requires:       python3-construct-classes = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-construct-classes
Summary:        Parse your binary structs into dataclasses
# oreon:reqs
Requires:       python3dist(construct) >= 2.10
# /oreon:reqs
%description -n python3-construct-classes

%prep
%global oreon_srcdir construct_classes-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-construct-classes usr/lib/python3*/site-packages/construct_classes* usr/lib64/python3*/site-packages/construct_classes* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/construct_classes* usr/lib64/python3*/site-packages/construct_classes* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-construct-classes -f %{oreon_filedir}/python3-construct-classes.list

%changelog

%autochangelog
