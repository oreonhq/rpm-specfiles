%global source0_hash 1fe496356820984f45559b1540c80ff10de448368929b9c60a2b55744cc88acf
Name:           python-mnemonic
Version:        0.21
Release:        1%{?dist}
Summary:        Implementation of Bitcoin BIP-0039
License:        MIT
URL:            ...
Source0:        https://files.pythonhosted.org/packages/source/m/mnemonic/mnemonic-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-mnemonic = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-mnemonic
Summary:        Implementation of Bitcoin BIP-0039
%description -n python3-mnemonic

%prep
%global oreon_srcdir mnemonic-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-mnemonic usr/lib/python3*/site-packages/mnemonic* usr/lib64/python3*/site-packages/mnemonic* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/mnemonic* usr/lib64/python3*/site-packages/mnemonic* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-mnemonic -f %{oreon_filedir}/python3-mnemonic.list

%changelog

%autochangelog
