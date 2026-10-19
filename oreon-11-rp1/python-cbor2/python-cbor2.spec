%global source0_hash 01ecc79a28f33d17331943ce508fc1e21f4b06553c73f874f4c77120d72b2ef9
Name:           python-cbor2
Version:        6.1.4
Release:        1%{?dist}
Summary:        CBOR _de_serializer with extensive tag support
License:        MIT
URL:            https://github.com/agronholm/cbor2
Source0:        https://files.pythonhosted.org/packages/source/c/cbor2/cbor2-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77
BuildRequires:  python3dist(setuptools-scm[toml]) >= 6.4
Requires:       python3-cbor2 = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-cbor2
Summary:        CBOR _de_serializer with extensive tag support
%description -n python3-cbor2

%prep
%global oreon_srcdir cbor2-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-cbor2 usr/lib/python3*/site-packages/cbor2* usr/lib64/python3*/site-packages/cbor2* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/cbor2* usr/lib64/python3*/site-packages/cbor2* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-cbor2 -f %{oreon_filedir}/python3-cbor2.list

%changelog

%autochangelog
