%global source0_hash 6cb9544a004609061e86873fe36500da6c2101042e9c7b9c3b804a29a12b98bf
Name:           python-pyopencl
Version:        2026.1.4
Release:        1%{?dist}
Summary:        Python wrapper for OpenCL
License:        MIT
URL:            https://mathema.tician.de/software/pyopencl
Source0:        https://files.pythonhosted.org/packages/source/p/pyopencl/pyopencl-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pyopencl = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pyopencl
Summary:        Python wrapper for OpenCL
%description -n python3-pyopencl

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir pyopencl-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pyopencl usr/lib/python3*/site-packages/pyopencl* usr/lib64/python3*/site-packages/pyopencl* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pyopencl* usr/lib64/python3*/site-packages/pyopencl* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pyopencl -f %{oreon_filedir}/python3-pyopencl.list

%changelog

%autochangelog
