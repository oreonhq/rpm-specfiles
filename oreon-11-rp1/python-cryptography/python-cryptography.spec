%global source0_hash 7b46165bb56eb4704e2eaaf86f3c940d19154535d9b0ca7d6d590b04060e00d5
Name:           python-cryptography
Version:        50.0.2
Release:        1%{?dist}
Summary:        cryptography is a package which provides cryptographic recipes and primitives to Python developers.
License:        Apache-2.0 OR BSD-3-Clause
URL:            https://github.com/pyca/cryptography
Source0:        https://files.pythonhosted.org/packages/source/c/cryptography/cryptography-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(cffi) >= 2.0.0
BuildRequires:  python3dist(cffi) >= 2.1
BuildRequires:  python3dist(maturin) < 2
BuildRequires:  python3dist(maturin) >= 1.14.1
BuildRequires:  python3dist(setuptools)
Requires:       python3-cryptography = %{version}-%{release}
# /oreon:deps
%package -n       python3-cryptography+ssh
Summary:        Metapackage for python3-cryptography ssh extras
Requires:       python3-cryptography = %{version}-%{release}
Requires:       python3dist(bcrypt) >= 3.1.5
Provides:       python3dist(cryptography[ssh]) = %{version}-%{release}

%description -n python3-cryptography+ssh
Metapackage for python3-cryptography ssh extras.

%description

%package -n     python3-cryptography
Summary:        cryptography is a package which provides cryptographic recipes and primitives to Python developers.
# oreon:reqs
Requires:       python3dist(cffi) >= 2.0.0
Requires:       python3dist(typing-extensions) >= 4.13.2
# /oreon:reqs
%description -n python3-cryptography

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir cryptography-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-cryptography usr/lib/python3*/site-packages/cryptography* usr/lib64/python3*/site-packages/cryptography* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/cryptography* usr/lib64/python3*/site-packages/cryptography* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-cryptography -f %{oreon_filedir}/python3-cryptography.list

%changelog

%autochangelog
