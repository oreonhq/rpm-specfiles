%global source0_hash 6f5fef59cb5b3708321db7cca56aed8ad7e662853351e7991fcf60ec606d47a4
Name:           python-oscrypto
Version:        1.3.0
Release:        1%{?dist}
Summary:        TLS _SSL_ sockets, key generation, encryption, decryption, signing, verification and KDFs using the OS crypto libraries. Does not require a compiler, and relies on the OS for patching. Works on Windows, OS X and Linux/BSD.
License:        MIT
URL:            https://github.com/wbond/oscrypto
Source0:        https://files.pythonhosted.org/packages/source/o/oscrypto/oscrypto-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-oscrypto = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-oscrypto
Summary:        TLS _SSL_ sockets, key generation, encryption, decryption, signing, verification and KDFs using the OS crypto libraries. Does not require a compiler, and relies on the OS for patching. Works on Windows, OS X and Linux/BSD.
%description -n python3-oscrypto

%prep
%global oreon_srcdir oscrypto-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-oscrypto usr/lib/python3*/site-packages/oscrypto* usr/lib64/python3*/site-packages/oscrypto* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/oscrypto* usr/lib64/python3*/site-packages/oscrypto* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-oscrypto -f %{oreon_filedir}/python3-oscrypto.list

%changelog

%autochangelog
