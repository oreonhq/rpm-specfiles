%global source0_hash c569a9714faf115cdb20b51e830e798c1f4de8dabb07f6ff25d221b5d09d8d7f
Name:           python-pyrfc3339
Version:        2.1.0
Release:        1%{?dist}
Summary:        Generate and parse RFC 3339 timestamps
License:        MIT
URL:            https://github.com/kurtraschke/pyrfc3339
Source0:        https://files.pythonhosted.org/packages/source/p/pyrfc3339/pyrfc3339-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 64
BuildRequires:  python3dist(setuptools-scm) >= 8
Requires:       python3-pyrfc3339 = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pyrfc3339
Summary:        Generate and parse RFC 3339 timestamps
%description -n python3-pyrfc3339

%prep
%global oreon_srcdir pyrfc3339-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pyrfc3339 usr/lib/python3*/site-packages/pyrfc3339* usr/lib64/python3*/site-packages/pyrfc3339* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pyrfc3339* usr/lib64/python3*/site-packages/pyrfc3339* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pyrfc3339 -f %{oreon_filedir}/python3-pyrfc3339.list

%changelog

%autochangelog
