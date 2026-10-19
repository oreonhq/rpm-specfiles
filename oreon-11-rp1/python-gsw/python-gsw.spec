%global source0_hash d14a734addfc96445ae84c800ad642d453ff174d48d6c30c0879a4425185b82a
Name:           python-gsw
Version:        3.6.23
Release:        1%{?dist}
Summary:        Gibbs Seawater Oceanographic Package of TEOS-10
License:        BSD-3-Clause
URL:            https://www.teos-10.org/
Source0:        https://files.pythonhosted.org/packages/source/g/gsw/gsw-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(numpy) < 3
BuildRequires:  python3dist(numpy) >= 2
BuildRequires:  python3dist(pip) > 9.0.1
BuildRequires:  python3dist(setuptools) >= 42
BuildRequires:  python3dist(setuptools-scm[toml]) >= 3.4
Requires:       python3-gsw = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-gsw
Summary:        Gibbs Seawater Oceanographic Package of TEOS-10
# oreon:reqs
Requires:       python3dist(numpy) >= 2
# /oreon:reqs
%description -n python3-gsw

%prep
%global oreon_srcdir gsw-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-gsw usr/lib/python3*/site-packages/gsw* usr/lib64/python3*/site-packages/gsw* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/gsw* usr/lib64/python3*/site-packages/gsw* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-gsw -f %{oreon_filedir}/python3-gsw.list

%changelog

%autochangelog
