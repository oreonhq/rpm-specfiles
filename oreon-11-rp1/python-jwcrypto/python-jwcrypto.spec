%global source0_hash a1e1570da5c2e35dbcd375ec1d2891a24de8eb35ee2c1fe8e91978efb72cfe90
Name:           python-jwcrypto
Version:        1.6.1
Release:        1%{?dist}
Summary:        Implementation of JOSE Web standards
License:        LGPL-3.0-or-later
URL:            https://github.com/latchset/jwcrypto
Source0:        https://files.pythonhosted.org/packages/source/j/jwcrypto/jwcrypto-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-jwcrypto = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-jwcrypto
Summary:        Implementation of JOSE Web standards
# oreon:reqs
Requires:       python3dist(cryptography) >= 49.0.0
Requires:       python3dist(typing-extensions) >= 4.5.0
# /oreon:reqs
%description -n python3-jwcrypto

%prep
%global oreon_srcdir jwcrypto-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-jwcrypto usr/lib/python3*/site-packages/jwcrypto* usr/lib64/python3*/site-packages/jwcrypto* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/jwcrypto* usr/lib64/python3*/site-packages/jwcrypto* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-jwcrypto -f %{oreon_filedir}/python3-jwcrypto.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.4.2-1
- Prepare for Oreon 11 (RP1)
