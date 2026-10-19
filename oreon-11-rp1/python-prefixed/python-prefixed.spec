%global source0_hash 164403fa9ebc83280bbc4705f4b243a28837e164310b4e65c38ccab1ebafeeb3
Name:           python-prefixed
Version:        0.9.0
Release:        1%{?dist}
Summary:        Prefixed alternative numeric library
License:        MPL-2.0
URL:            https://prefixed.readthedocs.io
Source0:        https://files.pythonhosted.org/packages/source/p/prefixed/prefixed-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-prefixed = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-prefixed
Summary:        Prefixed alternative numeric library
%description -n python3-prefixed

%prep
%global oreon_srcdir prefixed-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-prefixed usr/lib/python3*/site-packages/prefixed* usr/lib64/python3*/site-packages/prefixed* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/prefixed* usr/lib64/python3*/site-packages/prefixed* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-prefixed -f %{oreon_filedir}/python3-prefixed.list

%changelog

%autochangelog
