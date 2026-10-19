%global source0_hash 5a24bc1b5f9e0f0d1c0b6ddd1111e84c15dac44a07e3c1d24e74dd9bb4fc22eb
Name:           python-pyramid
Version:        2.1
Release:        1%{?dist}
Summary:        The Pyramid Web Framework, a Pylons project
License:        LicenseRef-Repoze-BSD-derived
URL:            https://trypyramid.com
Source0:        https://files.pythonhosted.org/packages/source/p/pyramid/pyramid-%{version}.tar.gz
BuildArch:      noarch
Patch:          https://github.com/Pylons/pyramid/pull/3762.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pyramid = %{version}-%{release}
# /oreon:deps
%package -n       python3-pyramid+testing
Summary:        Metapackage for python3-pyramid testing extras
Requires:       python3-pyramid = %{version}-%{release}
Provides:       python3dist(pyramid[testing]) = %{version}-%{release}

%description -n python3-pyramid+testing
Metapackage for python3-pyramid testing extras.

%description

%package -n     python3-pyramid
Summary:        The Pyramid Web Framework, a Pylons project
%description -n python3-pyramid

%prep
%global oreon_srcdir pyramid-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pyramid usr/lib/python3*/site-packages/pyramid* usr/lib64/python3*/site-packages/pyramid* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pyramid* usr/lib64/python3*/site-packages/pyramid* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pyramid -f %{oreon_filedir}/python3-pyramid.list

%changelog

%autochangelog
