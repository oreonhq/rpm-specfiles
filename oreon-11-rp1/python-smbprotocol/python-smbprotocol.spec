%global source0_hash bcc27edfff7d727a7eb30424138766e1ee216ae2ffc1af03dab0448f29c4731c
Name:           python-smbprotocol
Version:        1.17.0
Release:        1%{?dist}
Summary:        Interact with a server using the SMB 2/3 Protocol
License:        MIT
URL:            https://github.com/jborean93/smbprotocol
Source0:        https://files.pythonhosted.org/packages/source/s/smbprotocol/smbprotocol-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0.0
Requires:       python3-smbprotocol = %{version}-%{release}
# /oreon:deps
%package -n       python3-smbprotocol+kerberos
Summary:        Metapackage for python3-smbprotocol kerberos extras
Requires:       python3-smbprotocol = %{version}-%{release}
Provides:       python3dist(smbprotocol[kerberos]) = %{version}-%{release}

%description -n python3-smbprotocol+kerberos
Metapackage for python3-smbprotocol kerberos extras.

%description

%package -n     python3-smbprotocol
Summary:        Interact with a server using the SMB 2/3 Protocol
# oreon:reqs
Requires:       python3dist(cryptography) >= 2.0
# /oreon:reqs
%description -n python3-smbprotocol

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir smbprotocol-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-smbprotocol usr/lib/python3*/site-packages/smbprotocol* usr/lib64/python3*/site-packages/smbprotocol* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/smbprotocol* usr/lib64/python3*/site-packages/smbprotocol* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-smbprotocol -f %{oreon_filedir}/python3-smbprotocol.list

%changelog

%autochangelog
