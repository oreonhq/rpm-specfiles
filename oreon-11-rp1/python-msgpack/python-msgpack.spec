%global source0_hash 9eb0b0e602064527a045ea28c4f174ed69383587e29cebe28947e3b84106eb2a
Name:           python-msgpack
Version:        1.2.2
Release:        1%{?dist}
Summary:        MessagePack serializer
License:        Apache-2.0
URL:            https://msgpack.org/
Source0:        https://files.pythonhosted.org/packages/source/m/msgpack/msgpack-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 78.1.1
Requires:       python3-msgpack = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-msgpack
Summary:        MessagePack serializer
%description -n python3-msgpack

%prep
%global oreon_srcdir msgpack-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-msgpack usr/lib/python3*/site-packages/msgpack* usr/lib64/python3*/site-packages/msgpack* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/msgpack* usr/lib64/python3*/site-packages/msgpack* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-msgpack -f %{oreon_filedir}/python3-msgpack.list

%changelog

%autochangelog
