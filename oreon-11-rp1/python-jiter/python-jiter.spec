%global source0_hash 03e432f226a453851079fb84cd17c6da9991eab723e28d716f14ae3d906e0c12
Name:           python-jiter
Version:        0.17.0
Release:        1%{?dist}
Summary:        Fast iterable JSON parser.
License:        MIT
URL:            https://github.com/pydantic/jiter/
Source0:        https://files.pythonhosted.org/packages/source/j/jiter/jiter-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(maturin) < 2
BuildRequires:  python3dist(maturin) >= 1.15.0
Requires:       python3-jiter = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-jiter
Summary:        Fast iterable JSON parser.
%description -n python3-jiter

%prep
%global oreon_srcdir jiter-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-jiter usr/lib/python3*/site-packages/jiter* usr/lib64/python3*/site-packages/jiter* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/jiter* usr/lib64/python3*/site-packages/jiter* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-jiter -f %{oreon_filedir}/python3-jiter.list

%changelog

%autochangelog
