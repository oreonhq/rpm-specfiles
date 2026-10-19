%global source0_hash 63b9485408bdfdde544fced107045a8c0086cdc4bd0ef2f797b9e0dd111b964b
Name:           python-trio
Version:        0.34.0
Release:        1%{?dist}
Summary:        A friendly Python library for async concurrency and I/O
License:        MIT OR Apache-2.0
URL:            https://github.com/python-trio/trio
Source0:        https://files.pythonhosted.org/packages/source/t/trio/trio-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77
Requires:       python3-trio = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-trio
Summary:        A friendly Python library for async concurrency and I/O
# oreon:reqs
Requires:       python3dist(attrs) >= 23.2.0
Requires:       python3dist(cffi) >= 1.14
Requires:       python3dist(sniffio) >= 1.3.0
# /oreon:reqs
%description -n python3-trio

%prep
%global oreon_srcdir trio-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-trio usr/lib/python3*/site-packages/trio* usr/lib64/python3*/site-packages/trio* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/trio* usr/lib64/python3*/site-packages/trio* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-trio -f %{oreon_filedir}/python3-trio.list

%changelog

%autochangelog
