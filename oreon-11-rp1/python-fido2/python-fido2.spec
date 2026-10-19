%global source0_hash 85787428a94c3f8eaf72f0ff30afba983b559a1b1b795c93318c81b4ad4062c4
Name:           python-fido2
Version:        2.2.1
Release:        1%{?dist}
Summary:        FIDO2/WebAuthn library for implementing clients and servers.
License:        ...
URL:            https://github.com/Yubico/python-fido2
Source0:        https://files.pythonhosted.org/packages/source/f/fido2/fido2-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) >= 2.0
Requires:       python3-fido2 = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-fido2
Summary:        FIDO2/WebAuthn library for implementing clients and servers.
# oreon:reqs
Requires:       python3dist(flask) < 3
Requires:       python3dist(flask) >= 2.0
# /oreon:reqs
%description -n python3-fido2

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir fido2-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-fido2 usr/lib/python3*/site-packages/fido2* usr/lib64/python3*/site-packages/fido2* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/fido2* usr/lib64/python3*/site-packages/fido2* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-fido2 -f %{oreon_filedir}/python3-fido2.list

%changelog

%autochangelog
