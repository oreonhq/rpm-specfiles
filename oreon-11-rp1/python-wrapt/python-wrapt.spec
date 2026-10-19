%global source0_hash fd6390aab9e8aa40c52eff3c180f098e8d9f5894b1fd4c4fd2c207067b33ed16
Name:           python-wrapt
Version:        2.4.1
Release:        1%{?dist}
Summary:        Module for decorators, wrappers and monkey patching.
License:        BSD-2-Clause
URL:            https://github.com/GrahamDumpleton/wrapt
Source0:        https://files.pythonhosted.org/packages/source/w/wrapt/wrapt-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 62.0
Requires:       python3-wrapt = %{version}-%{release}
# /oreon:deps
%package -n       python3-wrapt+dev
Summary:        Metapackage for python3-wrapt dev extras
Requires:       python3-wrapt = %{version}-%{release}
Provides:       python3dist(wrapt[dev]) = %{version}-%{release}

%description -n python3-wrapt+dev
Metapackage for python3-wrapt dev extras.

%description

%package -n     python3-wrapt
Summary:        Module for decorators, wrappers and monkey patching.
%description -n python3-wrapt

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir wrapt-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-wrapt usr/lib/python3*/site-packages/wrapt* usr/lib64/python3*/site-packages/wrapt* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/wrapt* usr/lib64/python3*/site-packages/wrapt* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-wrapt -f %{oreon_filedir}/python3-wrapt.list

%changelog

%autochangelog
