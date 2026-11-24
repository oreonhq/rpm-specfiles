# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash e38464a49c6c85d7f1351b0126661487a7e0a14a50f1675ec50eb34d4f20ef21
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global pypi_name rsa

Name:           python-%{pypi_name}
Version:        4.9
Release:        1%{?dist}
Summary:        Pure-Python RSA implementation

License:        Apache-2.0
URL:            http://stuvel.eu/rsa
Source0:        https://pypi.python.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Python-RSA is a pure-Python RSA implementation. It supports encryption
and decryption, signing and verifying signatures, and key generation
according to PKCS#1 version 1.5. It can be used as a Python library as
well as on the command-line.

%package -n     python3-%{pypi_name}
Summary:        Pure-Python RSA implementation
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires: oreon-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pyasn1 >= 0.1.3
Requires:       python3-pyasn1 >= 0.1.3
Requires:       python3-setuptools

%description -n python3-%{pypi_name}
Python-RSA is a pure-Python RSA implementation. It supports encryption
and decryption, signing and verifying signatures, and key generation
according to PKCS#1 version 1.5. It can be used as a Python library as
well as on the command-line.

%prep
%oreon_sha256
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install
cp %{buildroot}%{_bindir}/pyrsa-priv2pub %{buildroot}%{_bindir}/pyrsa-priv2pub-3
cp %{buildroot}%{_bindir}/pyrsa-keygen %{buildroot}%{_bindir}/pyrsa-keygen-3
cp %{buildroot}%{_bindir}/pyrsa-encrypt %{buildroot}%{_bindir}/pyrsa-encrypt-3
cp %{buildroot}%{_bindir}/pyrsa-decrypt %{buildroot}%{_bindir}/pyrsa-decrypt-3
cp %{buildroot}%{_bindir}/pyrsa-sign %{buildroot}%{_bindir}/pyrsa-sign-3
cp %{buildroot}%{_bindir}/pyrsa-verify %{buildroot}%{_bindir}/pyrsa-verify-3

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{_bindir}/pyrsa-priv2pub
%{_bindir}/pyrsa-keygen
%{_bindir}/pyrsa-encrypt
%{_bindir}/pyrsa-decrypt
%{_bindir}/pyrsa-sign
%{_bindir}/pyrsa-verify
%{_bindir}/pyrsa-priv2pub-3
%{_bindir}/pyrsa-keygen-3
%{_bindir}/pyrsa-encrypt-3
%{_bindir}/pyrsa-decrypt-3
%{_bindir}/pyrsa-sign-3
%{_bindir}/pyrsa-verify-3
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%check

%changelog
%autochangelog
