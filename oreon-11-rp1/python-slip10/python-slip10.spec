%global source0_hash d248d3df26f123f08474339c45f0f264254f74ae9a5657234a1d5eb91f0c4d54
Name:           python-slip10
Version:        1.1.0
Release:        1%{?dist}
Summary:        A reference implementation of the SLIP-0010 specification, which generalizes the BIP-0032 derivation scheme for private and public key pairs in hierarchical deterministic wallets for the curves secp256k1, NIST P-256, ed25519 and curve25519.
License:        BSD-3-Clause AND MIT
URL:            https://github.com/trezor/python-slip10
Source0:        https://files.pythonhosted.org/packages/source/s/slip10/slip10-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-slip10 = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-slip10
Summary:        A reference implementation of the SLIP-0010 specification, which generalizes the BIP-0032 derivation scheme for private and public key pairs in hierarchical deterministic wallets for the curves secp256k1, NIST P-256, ed25519 and curve25519.
%description -n python3-slip10

%prep
%global oreon_srcdir slip10-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-slip10 usr/lib/python3*/site-packages/slip10* usr/lib64/python3*/site-packages/slip10* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/slip10* usr/lib64/python3*/site-packages/slip10* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-slip10 -f %{oreon_filedir}/python3-slip10.list

%changelog

%autochangelog
