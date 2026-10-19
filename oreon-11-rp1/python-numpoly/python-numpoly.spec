%global source0_hash 7724d8ff0ab5014c0704c92892ffd845cefc9e17a6cf4a06d9398e45502554fd
Name:           python-numpoly
Version:        1.3.9
Release:        1%{?dist}
Summary:        Polynomials as a numpy datatype
License:        BSD-2-Clause
URL:            https://pypi.org/project/numpoly/
Source0:        https://files.pythonhosted.org/packages/source/n/numpoly/numpoly-%{version}.tar.gz
BuildArch:      noarch
Patch:      %{forgeurl}/pull/127.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 40.9.0
Requires:       python3-numpoly = %{version}-%{release}
# /oreon:deps
%package -n       python3-numpoly+dev
Summary:        Metapackage for python3-numpoly dev extras
Requires:       python3-numpoly = %{version}-%{release}
Requires:       python3dist(pydocstyle) == 3.0.0
Provides:       python3dist(numpoly[dev]) = %{version}-%{release}

%description -n python3-numpoly+dev
Metapackage for python3-numpoly dev extras.

%description

%package -n     python3-numpoly
Summary:        Polynomials as a numpy datatype
# oreon:reqs
Requires:       python3dist(numpy) >= 2.0.0
Requires:       python3dist(setuptools) >= 40.9.0
# /oreon:reqs
%description -n python3-numpoly

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir numpoly-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-numpoly usr/lib/python3*/site-packages/numpoly* usr/lib64/python3*/site-packages/numpoly* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/numpoly* usr/lib64/python3*/site-packages/numpoly* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-numpoly -f %{oreon_filedir}/python3-numpoly.list

%changelog

%autochangelog
