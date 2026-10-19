%global source0_hash fb01e6b72c246b3b3ecb39e238cc9483e22a48c1986db6e9afaa3fdfa1b159d0
Name:           python-annarchy
Version:        5.0.4.1
Release:        1%{?dist}
Summary:        Artificial Neural Networks architect
License:        ...
URL:            https://github.com/ANNarchy/ANNarchy
Source0:        https://files.pythonhosted.org/packages/source/a/annarchy/annarchy-%{version}.tar.gz
BuildArch:      noarch
Patch:          drop-march-native.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-annarchy = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-annarchy
Summary:        Artificial Neural Networks architect
# oreon:reqs
Requires:       python3dist(cython) >= 3.0
Requires:       python3dist(matplotlib) >= 3.0
Requires:       python3dist(nanobind) <= 2.7.0
Requires:       python3dist(numpy) >= 1.21
Requires:       python3dist(scipy) > 1.9
Requires:       python3dist(setuptools) >= 65.0
Requires:       python3dist(sympy) > 1.11
# /oreon:reqs
%description -n python3-annarchy

%prep
%global oreon_srcdir annarchy-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-annarchy usr/lib/python3*/site-packages/annarchy* usr/lib64/python3*/site-packages/annarchy* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/annarchy* usr/lib64/python3*/site-packages/annarchy* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-annarchy -f %{oreon_filedir}/python3-annarchy.list

%changelog

%autochangelog
